// PBZ Loadout — data-driven rendering from /data/weapons.json
// Launch-day workflow: edit weapons.json → push → CI deploys. No HTML surgery.
(function () {
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  }
  function badge(b) {
    return '<span class="status-flag ' + (b === 'OFFICIAL' ? 'confirmed' : b === 'COMMUNITY' ? 'confirmed' : 'pending') + '">' + esc(b) + '</span>';
  }
  function statCell(v) {
    return v == null ? '<span class="status-flag pending">POST-LAUNCH</span>' : esc(v);
  }
  window.PBZ = {
    renderWeaponsTable: function (mountId) {
      fetch('/data/weapons.json').then(r => r.json()).then(d => {
        var el = document.getElementById(mountId);
        if (!el) return;
        var rows = d.weapons.map(function (w) {
          var s = w.stats || {};
          return '<tr><td><a href="/weapons/' + esc(w.slug) + '/">' + esc(w.name) + '</a></td>'
            + '<td>' + statCell(w.type) + '</td>'
            + '<td>' + statCell(s.attack) + '</td>'
            + '<td>' + statCell(s.speed) + '</td>'
            + '<td>' + statCell(s.effect) + '</td>'
            + '<td>' + badge(w.badge) + '</td></tr>';
        }).join('');
        el.innerHTML = '<table><tr><th>Weapon</th><th>Type</th><th>Attack</th><th>Speed</th><th>Effect</th><th>Status</th></tr>' + rows + '</table>';
      });
    },
    renderBossesList: function (mountId) {
      fetch('/data/weapons.json').then(r => r.json()).then(d => {
        var el = document.getElementById(mountId);
        if (!el) return;
        var rows = d.bosses.map(function (b, i) {
          if (!b.slug) return '';
          return '<tr><td>' + (i) + '</td><td>' + esc(b.name) + '</td><td>' + statCell(b.location) + '</td><td>' + badge(b.badge) + '</td></tr>';
        }).join('');
        el.innerHTML = rows
          ? '<table><tr><th>#</th><th>Boss</th><th>Location</th><th>Status</th></tr>' + rows + '</table>'
          : '<p><span class="status-flag pending">POST-LAUNCH</span> Full boss list is being verified in-game. Check back on launch day (Oct 29).</p>';
      });
    }
  };
})();
