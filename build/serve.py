#!/usr/bin/env python3
"""Local preview server that never caches, so edits show up on a plain reload.

    python3 build/serve.py          → http://127.0.0.1:8777
    python3 build/serve.py 3000     → another port

It also answers /admin/save.php the way PHP will on the client's hosting, so
the panel can be tried end to end here — same password, same file written,
same backup left behind. Nothing but this file knows about that: on a real
host the PHP script does the work and this one is not deployed at all.
"""
import functools, http.server, json, os, re, socketserver, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8777

SAVE_PHP = os.path.join(ROOT, "admin", "save.php")
PROMOS = os.path.join(ROOT, "assets", "promos.json")
BACKUP = os.path.join(ROOT, "assets", "promos.backup.json")
PLACEHOLDER = "ЗАМЕНИТЕ-ЭТОТ-ПАРОЛЬ"


def password():
    """The same two places PHP looks: admin/password.php first — the file that
    stays out of the repository — then the constant in save.php. So this asks
    for exactly what the hosting will, with nothing kept in step by hand."""
    secret = os.path.join(ROOT, "admin", "password.php")
    try:
        found = re.search(r"return\s*'([^']*)'", open(secret, encoding="utf-8").read())
        if found and found.group(1).strip():
            return found.group(1).strip()
    except OSError:
        pass
    try:
        found = re.search(r"\$PASSWORD = '([^']*)'", open(SAVE_PHP, encoding="utf-8").read())
        return found.group(1) if found else None
    except OSError:
        return None


def clean(doc):
    """The same narrowing save.php does: only what the panel writes is kept."""
    out = {"promos": []}
    for i, p in enumerate(doc.get("promos") or []):
        text = p.get("text") or {}
        mt = p.get("mt") if isinstance(p.get("mt"), dict) else {}
        out["promos"].append({
            "id": str(p.get("id") or "promo-%d" % (i + 1)),
            "active": bool(p.get("active")),
            "from": str(p.get("from") or ""),
            "to": str(p.get("to") or ""),
            "link": str(p.get("link") or ""),
            # отпечаток текста, с которого панель переводила — её же пометка
            "mt": {k: str(v)[:32] for k, v in mt.items() if k in ("ru", "en", "es") and v},
            "text": {
                lang: {k: str((text.get(lang) or {}).get(k) or "").strip()
                       for k in ("tag", "title", "body", "cta")}
                for lang in ("ru", "en", "es")
            },
        })
    return out


class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        super().end_headers()

    def log_message(self, *a):
        pass

    # ---- the panel's save endpoint, stood in for while there is no PHP ----
    def is_save(self):
        return self.path.split("?")[0].endswith("/admin/save.php")

    def reply(self, code, body):
        raw = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        if self.is_save():
            word = password()
            return self.reply(200, {"ok": True, "configured": bool(word) and word != PLACEHOLDER,
                                    "writable": True})
        super().do_GET()

    def do_POST(self):
        if not self.is_save():
            return self.reply(405, {"ok": False, "error": "Ожидается GET."})
        word = password()
        try:
            sent = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
        except ValueError:
            return self.reply(400, {"ok": False, "error": "Не удалось прочитать запрос."})
        if not word or word == PLACEHOLDER:
            return self.reply(403, {"ok": False, "error":
                "Пароль не изменён. Откройте admin/save.php и впишите свой пароль в строке PASSWORD."})
        if sent.get("password") != word:
            return self.reply(403, {"ok": False, "error": "Неверный пароль."})
        doc = sent.get("doc")
        if not isinstance(doc, dict) or not isinstance(doc.get("promos"), list):
            return self.reply(400, {"ok": False, "error": "В запросе нет списка акций."})

        out = clean(doc)
        if os.path.isfile(PROMOS):
            open(BACKUP, "w", encoding="utf-8").write(open(PROMOS, encoding="utf-8").read())
        tmp = PROMOS + ".tmp"
        open(tmp, "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
        os.replace(tmp, PROMOS)
        self.reply(200, {"ok": True, "count": len(out["promos"])})


socketserver.TCPServer.allow_reuse_address = True
handler = functools.partial(NoCache, directory=ROOT)
with socketserver.TCPServer(("127.0.0.1", PORT), handler) as httpd:
    print(f"Dr. Dobby → http://127.0.0.1:{PORT}   (ctrl-c to stop)")
    print(f"панель акций → http://127.0.0.1:{PORT}/admin/")
    httpd.serve_forever()
