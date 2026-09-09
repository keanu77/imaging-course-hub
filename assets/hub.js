(() => {
  const root=document.documentElement,themeButton=document.querySelector('.theme-toggle');
  const systemDark=matchMedia('(prefers-color-scheme: dark)');
  const syncTheme=()=>{const dark=(root.dataset.theme|| (systemDark.matches?'dark':'light'))==='dark';themeButton.setAttribute('aria-pressed',String(dark));themeButton.setAttribute('aria-label',dark?'切換淺色模式':'切換深色模式');};
  try {const saved=localStorage.getItem('imaging-hub:theme');if(saved==='light'||saved==='dark')root.dataset.theme=saved;} catch {}
  themeButton.hidden=false;syncTheme();systemDark.addEventListener('change',syncTheme);
  themeButton.addEventListener('click',()=>{const next=themeButton.getAttribute('aria-pressed')==='true'?'light':'dark';root.dataset.theme=next;try{localStorage.setItem('imaging-hub:theme',next);}catch{}syncTheme();});
  const filters=[...document.querySelectorAll('[data-filter]')],cards=[...document.querySelectorAll('.course-card')];
  if(!cards.length) return;
  document.querySelector('.filter-row').hidden=false;
  const apply=key=>{if(!['all','upper','lower','spine'].includes(key))key='all';filters.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.filter===key)));cards.forEach(c=>c.hidden=key!=='all'&&c.dataset.region!==key);document.querySelectorAll('[data-region-group]').forEach(g=>g.hidden=key!=='all'&&g.dataset.regionGroup!==key);document.querySelector('#result-count').textContent=`顯示 ${cards.filter(c=>!c.hidden).length} 個課程`;};
  filters.forEach(b=>b.addEventListener('click',()=>apply(b.dataset.filter)));
  document.querySelectorAll('[data-quick-filter]').forEach(a=>a.addEventListener('click',event=>{event.preventDefault();apply(a.dataset.quickFilter);document.querySelector('#courses-title').focus({preventScroll:true});document.querySelector('#courses').scrollIntoView({block:'start'});history.replaceState(null,'','#courses');}));
  document.querySelectorAll('a[href="#courses"]:not([data-quick-filter])').forEach(a=>a.addEventListener('click',()=>apply('all')));
})();
