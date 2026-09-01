/* ============================================================
   Dr. Dobby — shared behaviour for index.html / es.html / ru.html
   Language is read from <html lang>. Nothing else differs.
   ============================================================ */
(() => {
  const LANG = (document.documentElement.lang || 'en').slice(0, 2);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const T = {
    en: {
      open: h => `Open now <b>· until ${h}</b>`,
      shutToday: h => `Closed <b>· opens today ${h}</b>`,
      shut: (d, h) => `Closed <b>· opens ${d} ${h}</b>`,
      formError: 'Add your name and email and accept the Privacy Policy, then send again.',
      formOk: 'Thank you — we will call you back during opening hours.'
    },
    es: {
      open: h => `Abierto ahora <b>· hasta las ${h}</b>`,
      shutToday: h => `Cerrado <b>· abre hoy a las ${h}</b>`,
      shut: (d, h) => `Cerrado <b>· abre el ${d} a las ${h}</b>`,
      formError: 'Escribe tu nombre y tu email y acepta la política de privacidad, y vuelve a enviar.',
      formOk: 'Gracias — te llamamos dentro del horario de apertura.'
    },
    ru: {
      open: h => `Открыто <b>· до ${h}</b>`,
      shutToday: h => `Закрыто <b>· откроется сегодня в ${h}</b>`,
      shut: (d, h) => `Закрыто <b>· откроется в ${d} в ${h}</b>`,
      formError: 'Укажите имя и email и примите политику конфиденциальности, затем отправьте снова.',
      formOk: 'Спасибо — мы перезвоним вам в рабочие часы.'
    }
  }[LANG] || {};

  /* ---- scroll progress + sticky header ---- */
  const bar = document.getElementById('progress');
  const hdr = document.getElementById('hdr');
  let ticking = false;
  const onScroll = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    bar.style.transform = `scaleX(${max > 0 ? scrollY / max : 0})`;
    hdr.classList.toggle('is-stuck', scrollY > 8);
    ticking = false;
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  /* ---- mobile nav ---- */
  const burger = document.getElementById('burger'), nav = document.getElementById('nav');
  const setNav = open => { burger.setAttribute('aria-expanded', open); nav.classList.toggle('is-open', open); };
  burger.addEventListener('click', () => setNav(burger.getAttribute('aria-expanded') !== 'true'));
  nav.addEventListener('click', e => { if (e.target.tagName === 'A') setNav(false); });
  addEventListener('keydown', e => { if (e.key === 'Escape') setNav(false); });

  /* ---- scroll reveal ---- */
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); obs.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -12% 0px', threshold: .08 });
  document.querySelectorAll('[data-reveal]').forEach(el => io.observe(el));

  /* ---- open / closed, in clinic local time ---- */
  const HOURS = { 1: [540, 1230], 2: [540, 1230], 3: [540, 1230], 4: [540, 1230], 5: [540, 1230], 6: [630, 810] };
  const hhmm = m => String(Math.floor(m / 60)).padStart(2, '0') + ':' + String(m % 60).padStart(2, '0');
  const dayName = i => new Intl.DateTimeFormat(LANG, { weekday: 'long' })
    .format(new Date(Date.UTC(2024, 0, 7 + i)));           // 2024-01-07 was a Sunday
  const badges = [...document.querySelectorAll('[data-open]')];
  const paintState = () => {
    const parts = new Intl.DateTimeFormat('en-GB', {
      timeZone: 'Europe/Madrid', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false
    }).formatToParts(new Date());
    const get = t => parts.find(p => p.type === t).value;
    const day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(get('weekday'));
    const now = (+get('hour') % 24) * 60 + (+get('minute'));
    const today = HOURS[day];
    let cls, html;
    if (today && now >= today[0] && now < today[1]) {
      cls = 'dot is-open';
      html = T.open(hhmm(today[1]));
    } else {
      for (let i = 0; i < 8; i++) {
        const d = (day + i) % 7, h = HOURS[d];
        if (!h || (i === 0 && now >= h[0])) continue;
        cls = 'dot is-shut';
        html = i === 0 ? T.shutToday(hhmm(h[0])) : T.shut(dayName(d), hhmm(h[0]));
        break;
      }
    }
    badges.forEach(el => { el.className = cls; el.innerHTML = html; });
  };
  if (badges.length) { paintState(); setInterval(paintState, 60000); }

  /* ---- service filters ---- */
  const chips = [...document.querySelectorAll('.chip')];
  const rows = [...document.querySelectorAll('.row')];
  chips.forEach(chip => chip.addEventListener('click', () => {
    const f = chip.dataset.filter;
    chips.forEach(c => c.setAttribute('aria-pressed', c === chip));
    rows.forEach(r => { r.hidden = !(f === 'all' || r.dataset.cat === f); });
  }));

  /* ---- contact form (front-end only until a backend is wired up) ---- */
  const form = document.getElementById('form'), note = document.getElementById('formNote');
  if (form) form.addEventListener('submit', e => {
    e.preventDefault();
    form.querySelectorAll('[aria-invalid]').forEach(i => i.removeAttribute('aria-invalid'));
    const missing = [...form.querySelectorAll('[required]')]
      .find(i => i.type === 'checkbox' ? !i.checked : !i.value.trim());
    note.hidden = false;
    if (missing) {
      missing.setAttribute('aria-invalid', 'true');
      note.classList.add('is-err');
      note.textContent = T.formError;
      missing.focus();
      return;
    }
    note.classList.remove('is-err');
    note.textContent = T.formOk;
    form.reset();
  });

  /* ============================================================
     3D LOGO
     The doberman is inflated from the logo's own outline: a signed
     distance field turns the flat silhouette into a rounded body,
     so the outline stays exactly the logo's while the surface is a
     smooth, high-polygon volume. Three.js WebGPURenderer (WebGL2
     fallback is automatic), materials in TSL.
     ============================================================ */
  const stage = document.getElementById('stage');
  const canvas = document.getElementById('dobbyCanvas');
  const saveData = navigator.connection && navigator.connection.saveData;
  if (!stage || reduce || saveData) return;   // flat SVG stays — no 660 KB download

  let started = false;
  const start = () => { if (!started) { started = true; boot(); } };
  const near = () => { const r = stage.getBoundingClientRect(); return r.top < innerHeight + 300 && r.bottom > -300; };
  if (near()) start();
  else new IntersectionObserver((en, obs) => {
    if (en[0].isIntersecting) { obs.disconnect(); start(); }
  }, { rootMargin: '300px' }).observe(stage);

  /* ---------- the sculpted dog ----------
     The silhouette becomes a signed distance field; the field drives a
     rounded height profile, so the outline stays exactly the logo's while
     the body becomes a smooth, high-polygon volume. The shape is then split
     at the line where the legs part company with the chest: the torso is
     built once, the legs are built once and instanced on both flanks, so the
     model is a real four-legged dog rather than an inflated cut-out.
     Normals are analytic, so the shading is smooth with no welding pass. */
  function buildDoberman(THREE, poly, cells) {
    const CAP = 13;                       // distance only matters near the rim
    const E = poly.length;

    let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
    for (const [x, y] of poly) {
      if (x < minX) minX = x; if (x > maxX) maxX = x;
      if (y < minY) minY = y; if (y > maxY) maxY = y;
    }
    const pad = 1.2;
    const x0 = minX - pad, y0 = minY - pad;
    const w = (maxX - minX) + pad * 2, h = (maxY - minY) + pad * 2;
    const nx = cells, ny = Math.max(4, Math.round(cells * h / w));
    const dx = w / nx, dy = h / ny;
    const gw = nx + 1, gh = ny + 1, gn = gw * gh;

    // edges, flattened
    const eAx = new Float64Array(E), eAy = new Float64Array(E);
    const eVx = new Float64Array(E), eVy = new Float64Array(E), eInv = new Float64Array(E);
    for (let e = 0; e < E; e++) {
      const a = poly[e], b = poly[(e + 1) % E];
      eAx[e] = a[0]; eAy[e] = a[1];
      eVx[e] = b[0] - a[0]; eVy[e] = b[1] - a[1];
      const L = eVx[e] * eVx[e] + eVy[e] * eVy[e];
      eInv[e] = L > 0 ? 1 / L : 0;
    }

    // spatial bins, searched as expanding rings
    const B = 5;
    const bx = Math.ceil(w / B), by = Math.ceil(h / B);
    const bins = Array.from({ length: bx * by }, () => []);
    for (let e = 0; e < E; e++) {
      const lox = Math.min(eAx[e], eAx[e] + eVx[e]), hix = Math.max(eAx[e], eAx[e] + eVx[e]);
      const loy = Math.min(eAy[e], eAy[e] + eVy[e]), hiy = Math.max(eAy[e], eAy[e] + eVy[e]);
      const i0 = Math.max(0, Math.floor((lox - x0) / B)), i1 = Math.min(bx - 1, Math.floor((hix - x0) / B));
      const j0 = Math.max(0, Math.floor((loy - y0) / B)), j1 = Math.min(by - 1, Math.floor((hiy - y0) / B));
      for (let j = j0; j <= j1; j++) for (let i = i0; i <= i1; i++) bins[j * bx + i].push(e);
    }

    // where does a horizontal line cross the outline?
    const crossings = py => {
      const xs = [];
      for (let e = 0; e < E; e++) {
        const ay = eAy[e], by2 = ay + eVy[e];
        if ((ay > py) !== (by2 > py)) xs.push(eAx[e] + (py - ay) * eVx[e] / eVy[e]);
      }
      xs.sort((p, q) => p - q);
      const out = [];
      for (let k = 0; k + 1 < xs.length; k += 2) out.push([xs[k], xs[k + 1]]);
      return out;
    };

    // inside/outside, one scanline per grid row
    const inside = new Uint8Array(gn);
    for (let jy = 0; jy < gh; jy++) {
      for (const [a, b] of crossings(y0 + jy * dy)) {
        const iA = Math.max(0, Math.ceil((a - x0) / dx));
        const iB = Math.min(gw - 1, Math.floor((b - x0) / dx));
        for (let ix = iA; ix <= iB; ix++) inside[jy * gw + ix] = 1;
      }
    }

    // signed distance
    const dist = new Float32Array(gn);
    const maxRing = Math.ceil(CAP / B);
    for (let jy = 0; jy < gh; jy++) {
      const py = y0 + jy * dy;
      const jb = Math.min(by - 1, Math.max(0, Math.floor((py - y0) / B)));
      for (let ix = 0; ix < gw; ix++) {
        const px = x0 + ix * dx;
        const ib = Math.min(bx - 1, Math.max(0, Math.floor((px - x0) / B)));
        let best = CAP * CAP;
        for (let r = 0; r <= maxRing; r++) {
          for (let jj = jb - r; jj <= jb + r; jj++) {
            if (jj < 0 || jj >= by) continue;
            const edge = (jj === jb - r || jj === jb + r);
            for (let ii = ib - r; ii <= ib + r; ii++) {
              if (ii < 0 || ii >= bx) continue;
              if (!edge && ii !== ib - r && ii !== ib + r) continue;   // ring only
              const list = bins[jj * bx + ii];
              for (let n = 0; n < list.length; n++) {
                const e = list[n];
                const wx = px - eAx[e], wy = py - eAy[e];
                let t = (wx * eVx[e] + wy * eVy[e]) * eInv[e];
                t = t < 0 ? 0 : t > 1 ? 1 : t;
                const qx = wx - t * eVx[e], qy = wy - t * eVy[e];
                const d2 = qx * qx + qy * qy;
                if (d2 < best) best = d2;
              }
            }
          }
          const reach = r * B;
          if (best <= reach * reach) break;
        }
        const d = Math.min(Math.sqrt(best), CAP);
        dist[jy * gw + ix] = inside[jy * gw + ix] ? d : -d;
      }
    }

    // field gradient → analytic normals
    const gx = new Float32Array(gn), gy = new Float32Array(gn);
    for (let jy = 0; jy < gh; jy++) for (let ix = 0; ix < gw; ix++) {
      const i0 = ix > 0 ? ix - 1 : 0, i1 = ix < gw - 1 ? ix + 1 : gw - 1;
      const j0 = jy > 0 ? jy - 1 : 0, j1 = jy < gh - 1 ? jy + 1 : gh - 1;
      gx[jy * gw + ix] = (dist[jy * gw + i1] - dist[jy * gw + i0]) / ((i1 - i0) * dx);
      gy[jy * gw + ix] = (dist[j1 * gw + ix] - dist[j0 * gw + ix]) / ((j1 - j0) * dy);
    }
    const tmp = new Float32Array(gn);
    const blur = arr => {
      for (let jy = 0; jy < gh; jy++) {
        const row = jy * gw;
        for (let ix = 0; ix < gw; ix++) {
          const a0 = arr[row + (ix > 0 ? ix - 1 : 0)];
          const a2 = arr[row + (ix < gw - 1 ? ix + 1 : gw - 1)];
          tmp[row + ix] = (a0 + arr[row + ix] + a2) / 3;
        }
      }
      for (let jy = 0; jy < gh; jy++) {
        const row = jy * gw;
        const up = (jy > 0 ? jy - 1 : 0) * gw, dn = (jy < gh - 1 ? jy + 1 : gh - 1) * gw;
        for (let ix = 0; ix < gw; ix++) arr[row + ix] = (tmp[up + ix] + tmp[row + ix] + tmp[dn + ix]) / 3;
      }
    };
    blur(gx); blur(gy); blur(gx); blur(gy);

    /* --- where do the legs leave the body? the first line below the chest
           that cuts two spans, both already leg-narrow --- */
    let cutY = minY + (maxY - minY) * 0.72;
    for (let py = minY + (maxY - minY) * 0.45; py < maxY; py += 0.5) {
      const sp = crossings(py);
      if (sp.length === 2 && sp.every(([a, b]) => b - a < (maxX - minX) * 0.17)) { cutY = py; break; }
    }
    const legWindows = crossings(cutY).map(([a, b]) => [a - 2, b + 2]);
    const legTopY = cutY - 14;                    // legs run up inside the torso
    const cutRow = Math.min(ny, Math.max(0, Math.round((cutY - y0) / dy)));
    const legTopRow = Math.min(ny, Math.max(0, Math.round((legTopY - y0) / dy)));
    const legCol = new Uint8Array(gw);            // which columns a leg may occupy
    for (let ix = 0; ix < gw; ix++) {
      const px = x0 + ix * dx;
      legCol[ix] = legWindows.some(([a, b]) => px >= a && px <= b) ? 1 : 0;
    }

    let dmax = 0, legMax = 0;
    for (let jy = 0; jy < gh; jy++) for (let ix = 0; ix < gw; ix++) {
      const d = dist[jy * gw + ix];
      if (d > dmax) dmax = d;
      if (d > legMax && y0 + jy * dy > cutY + 4) legMax = d;
    }
    const R_BODY = Math.min(Math.max(dmax * 0.92, 8), 12), D_BODY = 9.4;
    const R_LEG = Math.min(Math.max(legMax * 0.95, 2.2), 3.4), D_LEG = R_LEG;

    const cx = (minX + maxX) / 2, cy = (minY + maxY) / 2;

    // profile shared by both parts, so V8 only warms one copy
    const hgtOf = (d, R, D) => {
      const t = d <= 0 ? 0 : d >= R ? 1 : d / R;
      const u = 1 - t;
      return D * Math.sqrt(1 - u * u);
    };
    const slopeOf = (d, R, D) => {
      let t = d <= 0 ? 0.0025 : d >= R ? 1 : d / R;
      if (t < 0.0025) t = 0.0025;
      const u = 1 - t;
      const sq = Math.sqrt(1 - u * u);
      return sq > 1e-5 ? (D * u) / (R * sq) : 0;
    };

    /* --- mesh one part: clip every cell against d ≥ 0 and the part's own
           mask, then emit a front and a back shell --- */
    function emit(rowFrom, rowTo, maskUntilRow, R, D) {
      let pos = new Float32Array(1 << 15), nor = new Float32Array(1 << 15), pn = 0;
      let idx = new Uint32Array(1 << 15), inl = 0;
      const growV = () => {
        const cap = pos.length * 2;
        const p2 = new Float32Array(cap); p2.set(pos); pos = p2;
        const n2 = new Float32Array(cap); n2.set(nor); nor = n2;
      };
      const tri = (a, b, c) => {
        if (inl + 3 > idx.length) { const i2 = new Uint32Array(idx.length * 2); i2.set(idx); idx = i2; }
        idx[inl++] = a; idx[inl++] = b; idx[inl++] = c;
      };
      const push = (px, py, d, ggx, ggy, flip) => {
        const z = hgtOf(d, R, D), s = slopeOf(d, R, D);
        const nX = -s * ggx, nY = s * ggy, nZ = 1;
        const L = Math.sqrt(nX * nX + nY * nY + 1) || 1;
        if (pn + 3 > pos.length) growV();
        const id = pn / 3;
        pos[pn] = px - cx; pos[pn + 1] = cy - py; pos[pn + 2] = flip ? -z : z;
        nor[pn] = nX / L; nor[pn + 1] = nY / L; nor[pn + 2] = (flip ? -nZ : nZ) / L;
        pn += 3;
        return id;
      };

      const nodeF = new Int32Array(gn).fill(-1);
      const nodeB = new Int32Array(gn).fill(-1);
      const edgeH = new Int32Array(gn).fill(-1);
      const edgeV = new Int32Array(gn).fill(-1);
      const oKind = new Int32Array(8), oKey = new Int32Array(8);
      const oPx = new Float64Array(8), oPy = new Float64Array(8);
      const oD = new Float64Array(8), oGx = new Float64Array(8), oGy = new Float64Array(8);
      const vF = new Int32Array(8), vB = new Int32Array(8);
      const cN = new Int32Array(4);

      for (let jy = rowFrom; jy < rowTo; jy++) {
        const columnLimited = jy < maskUntilRow;
        for (let ix = 0; ix < nx; ix++) {
          if (columnLimited && !legCol[ix] && !legCol[ix + 1]) continue;
          cN[0] = jy * gw + ix;
          cN[1] = jy * gw + ix + 1;
          cN[2] = (jy + 1) * gw + ix + 1;
          cN[3] = (jy + 1) * gw + ix;
          if (dist[cN[0]] < 0 && dist[cN[1]] < 0 && dist[cN[2]] < 0 && dist[cN[3]] < 0) continue;

          let m = 0;
          for (let k = 0; k < 4; k++) {
            const A = cN[k], Bn = cN[(k + 1) % 4];
            const dA = dist[A], dB = dist[Bn];
            if (dA >= 0) {
              oKind[m] = 0; oKey[m] = A;
              oPx[m] = x0 + (A % gw) * dx; oPy[m] = y0 + ((A / gw) | 0) * dy;
              oD[m] = dA; oGx[m] = gx[A]; oGy[m] = gy[A]; m++;
            }
            if ((dA >= 0) !== (dB >= 0)) {
              const t = dA / (dA - dB);
              const axp = x0 + (A % gw) * dx, ayp = y0 + ((A / gw) | 0) * dy;
              const bxp = x0 + (Bn % gw) * dx, byp = y0 + ((Bn / gw) | 0) * dy;
              oKind[m] = k === 0 || k === 2 ? 1 : 2;
              oKey[m] = k === 0 ? cN[0] : k === 1 ? cN[1] : k === 2 ? cN[3] : cN[0];
              oPx[m] = axp + (bxp - axp) * t; oPy[m] = ayp + (byp - ayp) * t;
              oD[m] = 0;
              oGx[m] = gx[A] + (gx[Bn] - gx[A]) * t;
              oGy[m] = gy[A] + (gy[Bn] - gy[A]) * t;
              m++;
            }
          }
          if (m < 3) continue;

          for (let k = 0; k < m; k++) {
            if (oKind[k] === 0) {
              const A = oKey[k];
              if (nodeF[A] < 0) {
                nodeF[A] = push(oPx[k], oPy[k], oD[k], oGx[k], oGy[k], false);
                nodeB[A] = oD[k] > 1e-4 ? push(oPx[k], oPy[k], oD[k], oGx[k], oGy[k], true) : nodeF[A];
              }
              vF[k] = nodeF[A]; vB[k] = nodeB[A];
            } else {
              const store = oKind[k] === 1 ? edgeH : edgeV;
              const A = oKey[k];
              if (store[A] < 0) store[A] = push(oPx[k], oPy[k], 0, oGx[k], oGy[k], false);
              vF[k] = vB[k] = store[A];
            }
          }
          for (let k = 1; k + 1 < m; k++) {
            tri(vF[0], vF[k], vF[k + 1]);
            tri(vB[0], vB[k + 1], vB[k]);
          }
        }
      }

      const g = new THREE.BufferGeometry();
      g.setAttribute('position', new THREE.BufferAttribute(pos.slice(0, pn), 3));
      g.setAttribute('normal', new THREE.BufferAttribute(nor.slice(0, pn), 3));
      g.setIndex(new THREE.BufferAttribute(idx.slice(0, inl), 1));
      g.computeBoundingSphere();
      return { geometry: g, triangles: inl / 3 };
    }

    const torso = emit(0, cutRow, 0, R_BODY, D_BODY);
    const legs = emit(legTopRow, ny, cutRow, R_LEG, D_LEG);

    return {
      torso: torso.geometry,
      legs: legs.geometry,
      legZ: D_BODY * 0.58,
      triangles: torso.triangles + legs.triangles * 2
    };
  }

  async function boot() {
    let THREE, TSL;
    try {
      [THREE, TSL] = await Promise.all([import('three/webgpu'), import('three/tsl')]);
    } catch (err) { console.warn('[dobby] 3D unavailable, keeping flat mark', err); return; }

    const { color, float } = TSL;

    const renderer = new THREE.WebGPURenderer({ canvas, antialias: true, alpha: true });
    renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    try { await renderer.init(); }
    catch (err) { console.warn('[dobby] renderer init failed', err); return; }

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(34, 1, 0.1, 100);
    camera.position.set(0, 0, 6.1);

    // the outline, straight out of the inline <symbol>
    const d = document.getElementById('dobbyPath').getAttribute('d');
    const nums = d.match(/-?\d*\.?\d+/g).map(Number);
    const poly = [];
    for (let i = 0; i + 1 < nums.length; i += 2) poly.push([nums[i], nums[i + 1]]);

    const t0build = performance.now();
    const built = buildDoberman(THREE, poly, innerWidth < 700 ? 165 : 240);
    console.debug(`[dobby] ${built.triangles} triangles, built in ${Math.round(performance.now() - t0build)} ms`);

    // black, like the silhouette in the logo — the volume reads through
    // specular alone, so nothing tints the dog itself
    const mat = new THREE.MeshPhysicalNodeMaterial();
    mat.colorNode = color(0x000000);
    mat.roughnessNode = float(0.24);
    mat.metalnessNode = float(0.0);
    mat.clearcoatNode = float(0.95);
    mat.clearcoatRoughnessNode = float(0.09);
    mat.side = THREE.DoubleSide;

    const dog = new THREE.Group();
    dog.add(new THREE.Mesh(built.torso, mat));
    const near = new THREE.Mesh(built.legs, mat);
    near.position.z = built.legZ;
    const far = new THREE.Mesh(built.legs, mat);
    far.position.set(1.4, 0, -built.legZ);          // the off-side pair, a step behind
    dog.add(near, far);
    dog.scale.setScalar(0.0245);
    const group = new THREE.Group();
    group.add(dog);
    scene.add(group);

    scene.add(new THREE.HemisphereLight(0xffffff, 0xffffff, 0.28));
    const key = new THREE.DirectionalLight(0xfff6ee, 3.6); key.position.set(3.2, 4.2, 5); scene.add(key);
    const top = new THREE.DirectionalLight(0xffffff, 1.45); top.position.set(-1.4, 3.4, 1.6); scene.add(top);
    const rim = new THREE.DirectionalLight(0xffffff, 0.9); rim.position.set(-5, 1.4, -2.2); scene.add(rim);
    const fill = new THREE.DirectionalLight(0xf8b07c, 0.35); fill.position.set(2.5, -2.8, 2.2); scene.add(fill);

    const resize = () => {
      const r = stage.getBoundingClientRect();
      if (!r.width) return;
      renderer.setSize(r.width, r.height, false);
      camera.aspect = r.width / r.height;
      camera.updateProjectionMatrix();
    };
    new ResizeObserver(resize).observe(stage);
    resize();

    const target = { x: 0, y: 0 }, cur = { x: 0, y: 0 };
    const hero = stage.closest('.hero');
    hero.addEventListener('pointermove', e => {
      const r = hero.getBoundingClientRect();
      target.x = ((e.clientX - r.left) / r.width - 0.5) * 2;
      target.y = ((e.clientY - r.top) / r.height - 0.5) * 2;
    }, { passive: true });
    hero.addEventListener('pointerleave', () => { target.x = target.y = 0; });

    let visible = true;
    new IntersectionObserver(en => { visible = en[0].isIntersecting; }).observe(stage);

    const t0 = performance.now();
    const pose = t => {
      const intro = Math.min(t / 1.3, 1);
      const ease = 1 - Math.pow(1 - intro, 3);

      cur.x += (target.x - cur.x) * 0.06;
      cur.y += (target.y - cur.y) * 0.06;

      const scroll = Math.max(0, Math.min(1, -stage.getBoundingClientRect().top / innerHeight));

      group.rotation.y = 0.34 + (1 - ease) * -1.05 + cur.x * 0.42 + Math.sin(t * 0.36) * 0.09 + scroll * 0.9;
      group.rotation.x = -0.06 + cur.y * 0.2 + Math.sin(t * 0.5) * 0.035;
      group.rotation.z = Math.sin(t * 0.42) * 0.02;
      group.position.y = 0.07 + Math.sin(t * 0.62) * 0.09 - (1 - ease) * 0.3;
      group.scale.setScalar(0.88 + 0.12 * ease);
    };

    // first paint is awaited so the shader pipeline is ready before we cross-fade
    pose(0);
    await renderer.renderAsync(scene, camera);
    stage.classList.add('is-live');

    renderer.setAnimationLoop(() => {
      if (!visible) return;
      pose((performance.now() - t0) / 1000);
      renderer.render(scene, camera);
    });
  }
})();
