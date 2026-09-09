const {chromium}=require('/Users/ethanstudio/.agents/skills/fb-post/node_modules/playwright');const fs=require('fs'),assert=require('node:assert/strict');
(async()=>{const b=await chromium.launch({headless:true});const results=[];fs.mkdirSync(__dirname+'/docs/screens',{recursive:true});const p=await b.newPage({viewport:{width:1440,height:1000}});const errors=[];p.on('pageerror',e=>errors.push(e.message));
await p.goto('http://127.0.0.1:8940/dist/');await p.locator('.filter-row').waitFor();
for(const theme of ['light','dark'])for(const width of [320,390,820,1440]){
 await p.setViewportSize({width,height:1000});await p.evaluate(t=>document.documentElement.dataset.theme=t,theme);
 const layout=await p.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,cards:[...document.querySelectorAll('.course-card')].map(e=>e.scrollWidth>e.clientWidth+1),h1:document.querySelectorAll('h1').length,theme:getComputedStyle(document.documentElement).colorScheme}));
 assert.equal(layout.overflow,false);assert.ok(layout.cards.every(v=>!v));assert.equal(layout.h1,1);assert.equal(layout.theme,theme);results.push({theme,width,...layout});
 if([390,1440].includes(width))await p.screenshot({path:__dirname+`/docs/screens/${theme}-${width}.png`,fullPage:width===1440});
}
for(const [filter,count] of [['upper',2],['lower',3],['spine',2],['all',7]]){await p.locator(`[data-filter="${filter}"]`).click();assert.equal(await p.locator('.course-card:visible').count(),count);assert.equal(await p.locator(`[data-filter="${filter}"]`).getAttribute('aria-pressed'),'true');results.push({filter,count});}
await p.locator('[data-quick-filter="lower"]').click();assert.equal(await p.locator('.course-card:visible').count(),3);assert.equal(await p.evaluate(()=>document.activeElement.id),'courses-title');
await p.locator('.hero-actions a[href="#courses"]').click();assert.equal(await p.locator('.course-card:visible').count(),7);
const expected=JSON.parse(fs.readFileSync(__dirname+'/courses.json')).map(c=>c.url);assert.deepEqual(await p.locator('.course-link').evaluateAll(es=>es.map(e=>e.href)),expected);
const social=await p.locator('.social-links>a').evaluateAll(es=>es.map(e=>({url:e.href,rel:e.rel})));assert.equal(social.length,3);assert.ok(social.every(e=>e.rel.includes('noopener')));
await p.locator('.theme-toggle').click();const theme=await p.evaluate(()=>document.documentElement.dataset.theme);await p.reload();await p.locator('.filter-row').waitFor();assert.equal(await p.evaluate(()=>document.documentElement.dataset.theme),theme);
await p.locator('.SkipLink,.skip').focus();await p.keyboard.press('Enter');assert.equal(await p.evaluate(()=>document.activeElement.id),'main');
const c=await b.newContext({javaScriptEnabled:false});const n=await c.newPage();await n.goto('http://127.0.0.1:8940/dist/');assert.equal(await n.locator('.course-link:visible').count(),7);assert.equal(await n.locator('.filters:visible').count(),0);await c.close();
await p.goto('http://127.0.0.1:8940/preview/');assert.ok((await p.locator('.course-link').evaluateAll(es=>es.map(e=>e.href))).every(u=>u.startsWith('http://127.0.0.1:893')));
assert.deepEqual(errors,[]);fs.writeFileSync(__dirname+'/docs/validation.json',JSON.stringify({layouts:results,links:expected,social,checks:['quick filter and focus','all courses reset','theme reload','skip link','no-JS course access','local preview links separated'],errors},null,2));await b.close();console.log('PASS hub responsive, filters, links, themes, keyboard, no-JS');})().catch(e=>{console.error(e);process.exit(1)});
