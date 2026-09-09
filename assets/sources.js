(() => {
 const site=document.querySelector('#source-site'),tier=document.querySelector('#source-tier'),search=document.querySelector('#source-search');
 const records=[...document.querySelectorAll('.video-record')],texts=new Map(records.map(r=>[r,r.textContent.normalize('NFKC').toLowerCase()]));
 let channel=null;
 const normalize=t=>t.normalize('NFKC').trim().toLowerCase();
 function apply(){const query=normalize(search.value);let count=0;const unique=new Set();records.forEach(r=>{const show=(site.value==='all'||r.dataset.site===site.value)&&(tier.value==='all'||r.dataset.tier===tier.value)&&(!channel||r.dataset.channel===channel)&&(!query||texts.get(r).includes(query));r.hidden=!show;if(show){count++;unique.add(r.dataset.videoId);}});document.querySelector('#source-results').textContent=`顯示 ${count} 筆收錄 · ${unique.size} 支不重複影片${channel?' · '+channel:''}`;document.querySelector('#source-empty').hidden=count>0;}
 document.querySelector('.source-controls').hidden=false;
 const initial=new URLSearchParams(location.search).get('site');if([...site.options].some(o=>o.value===initial))site.value=initial;
 for(const control of [site,tier,search])control.addEventListener('input',()=>{channel=null;apply();});
 document.querySelector('#source-reset').addEventListener('click',()=>{site.value='all';tier.value='core';search.value='';channel=null;apply();search.focus();});
 document.querySelectorAll('[data-source-channel]').forEach(a=>a.addEventListener('click',event=>{event.preventDefault();channel=a.dataset.sourceChannel;site.value='all';tier.value='core';search.value='';apply();const title=document.querySelector('#videos-title');title.focus({preventScroll:true});document.querySelector('#videos').scrollIntoView({block:'start'});history.replaceState(null,'','#videos');}));apply();
})();
