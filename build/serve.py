#!/usr/bin/env python3
"""Local preview server that never caches, so edits show up on a plain reload.

    python3 build/serve.py          → http://127.0.0.1:8777
    python3 build/serve.py 3000     → another port
"""
import functools, http.server, os, socketserver, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8777


class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        super().end_headers()

    def log_message(self, *a):
        pass


socketserver.TCPServer.allow_reuse_address = True
handler = functools.partial(NoCache, directory=ROOT)
with socketserver.TCPServer(("127.0.0.1", PORT), handler) as httpd:
    print(f"Dr. Dobby → http://127.0.0.1:{PORT}   (ctrl-c to stop)")
    httpd.serve_forever()
