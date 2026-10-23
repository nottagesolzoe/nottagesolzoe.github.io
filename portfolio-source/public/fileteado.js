(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  if (reduced.matches || !matchMedia('(pointer: fine)').matches) return;
  const canvas = document.createElement('canvas');
  canvas.className = 'fileteado-pointer';
  canvas.setAttribute('aria-hidden', 'true');
  document.body.appendChild(canvas);
  const ctx = canvas.getContext('2d');
  if (!ctx) { canvas.remove(); return; }
  let flourishes = [], frame = 0, previous = null, last = 0;
  function resize() {
    const scale = Math.min(devicePixelRatio || 1, 2);
    canvas.width = innerWidth * scale;
    canvas.height = innerHeight * scale;
    canvas.style.width = `${innerWidth}px`;
    canvas.style.height = `${innerHeight}px`;
    ctx.setTransform(scale, 0, 0, scale, 0, 0);
  }
  function curl(x, y, angle, opacity) {
    ctx.save(); ctx.translate(x, y); ctx.rotate(angle);
    ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    ctx.globalAlpha = opacity * .55;
    for (const [color, mirror] of [['#C7353C', 1], ['#5B20D6', -1]]) {
      ctx.save(); ctx.scale(1, mirror); ctx.strokeStyle = color;
      ctx.lineWidth = 1.4;
      ctx.beginPath(); ctx.moveTo(-44, 10);
      ctx.bezierCurveTo(-20, 31, 3, 15, 17, -6);
      ctx.bezierCurveTo(30, -26, 51, -20, 48, -6);
      ctx.bezierCurveTo(45, 8, 29, 2, 35, -6);
      ctx.bezierCurveTo(39, -12, 45, -7, 41, -3); ctx.stroke();
      ctx.lineWidth = .7; ctx.beginPath(); ctx.moveTo(-42, 15);
      ctx.bezierCurveTo(-18, 35, 8, 16, 21, -4); ctx.stroke();
      ctx.fillStyle = color; ctx.beginPath(); ctx.moveTo(4, 11);
      ctx.quadraticCurveTo(-1, -6, 16, -12);
      ctx.quadraticCurveTo(17, 3, 4, 11); ctx.fill(); ctx.restore();
    }
    ctx.restore();
  }
  function draw(now) {
    ctx.clearRect(0, 0, innerWidth, innerHeight);
    flourishes = flourishes.filter(f => now - f.born < 850);
    for (const f of flourishes) curl(f.x, f.y, f.angle, 1 - (now - f.born) / 850);
    frame = flourishes.length ? requestAnimationFrame(draw) : 0;
  }
  function move(event) {
    if (reduced.matches || event.pointerType !== 'mouse') return;
    const now = performance.now();
    if (!previous) { previous = {x:event.clientX, y:event.clientY}; return; }
    const dx = event.clientX - previous.x, dy = event.clientY - previous.y;
    if (now - last < 180 || Math.hypot(dx,dy) < 38) return;
    // Keep decoration in open space, away from reading and interactive controls.
    if (!event.target.closest('a,button,input,iframe,p,h1,h2,h3')) {
      flourishes.push({x:event.clientX, y:event.clientY, angle:Math.atan2(dy,dx), born:now});
      flourishes = flourishes.slice(-5);
      if (!frame) frame = requestAnimationFrame(draw);
    }
    previous = {x:event.clientX, y:event.clientY}; last = now;
  }
  document.addEventListener('pointermove', move, {passive:true});
  document.addEventListener('pointerleave', () => {previous = null;});
  reduced.addEventListener('change', () => {
    if (reduced.matches) { cancelAnimationFrame(frame); frame = 0; flourishes = []; ctx.clearRect(0,0,innerWidth,innerHeight); }
  });
  addEventListener('resize', resize); resize();
})();
