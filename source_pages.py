"""Render auditable, searchable video references without changing course data."""
import csv
import json
from collections import Counter
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def e(value):
    return escape(str(value or ''), quote=True)

def render_sources(out, courses, preview=False):
    payload = json.loads((ROOT / 'video-sources.json').read_text())
    rows = payload['records']
    core = [r for r in rows if r['learning_tier'] == 'core']
    by_site = {c['id']:c for c in courses}
    profiles = json.loads((ROOT / 'source-profiles.json').read_text())
    profile_html = []
    for p in profiles:
        selected = [r for r in core if r['verified_channel'] in p['channels']]
        sites = '、'.join(c['name'] for c in courses if any(r['site'] == c['id'] for r in selected))
        additional = f' · <a href="{e(p["additional_url"])}">The Ultrasound Site 教育頁</a>' if p.get('additional_url') else ''
        profile_html.append(f'<article class="source-profile"><p class="eyebrow">{e(p["role"])}</p><h3>{e(p["name"])}</h3><p>{e(p["importance"])}</p><p class="source-boundary">{e(p["boundary"])}</p><p class="source-meta">收錄於：{sites}</p><a href="{e(p["url"])}">發布單位／講者網站 ↗</a>{additional}</article>')
    site_overview = []
    options = ['<option value="all">全部部位</option>']
    for c in courses:
        group = [r for r in core if r['site'] == c['id']]
        channels = Counter(r['verified_channel'] for r in group)
        options.append(f'<option value="{c["id"]}">{c["name"]}</option>')
        site_overview.append(f'<li><a href="sources.html?site={c["id"]}#videos"><strong>{c["name"]}</strong><span>{len(group)} 筆核心收錄 · {len(channels)} 個發布頻道</span><small>{e("、".join(name for name,_ in channels.most_common(3)))}</small><b aria-hidden="true">↗</b></a></li>')
    intro = f'''<section class="source-home wrap" id="sources"><div class="section-head"><div><p class="eyebrow" lang="en">SOURCES & LEARNING VALUE</p><h2>主要影片從哪裡來？</h2></div><a class="text-link" href="sources.html">完整來源與逐片重要性 ↗</a></div><p class="source-intro">依七站既有「核心必看」標記整理，共 {len(core)} 筆收錄、{len(set(r['video_id'] for r in core))} 支不重複影片。從專業學會的掃描框架，到具名講者的影像細節與病例討論，逐支說明其教學用途。</p><ul class="source-site-list">{''.join(site_overview)}</ul><p class="catalog-note">「核心」是課程學習順序，不代表證據等級或臨床背書。完整清單保留年份、講者、診斷選段與待補查標示。</p></section>'''
    directory = []
    channel_profiles = json.loads((ROOT / 'channel-profiles.json').read_text())['channels']
    profile_by_channel = {p['channel']: p for p in channel_profiles}
    assert set(profile_by_channel) == {r['verified_channel'] for r in core}
    for channel in sorted({r['verified_channel'] for r in core}, key=str.casefold):
        p = profile_by_channel[channel]
        selected = [r for r in core if r['verified_channel'] == channel]
        titles = list(dict.fromkeys(r['name'] for r in selected))[:3]
        sites = '、'.join(c['name'] for c in courses if any(r['site'] == c['id'] for r in selected))
        boundary = f'<p class="source-boundary">{e(p["boundary_zh"])}</p>' if p['boundary_zh'] else ''
        directory.append(f'<details class="provider-record"><summary><strong>{e(p["name_zh"])}</strong><span class="provider-original" lang="en">{e(channel)}</span><span>{len(selected)} 筆核心收錄</span></summary><p class="provider-background"><strong>來源背景：</strong>{e(p["background_zh"])}</p><p class="provider-importance"><strong>為什麼值得看：</strong>{e(p["importance_zh"])}</p><p><strong>適合何時看：</strong>{e(p["when_zh"])}</p><p>收錄部位：{sites}</p><p>課程用途舉例：{e("；".join(titles))}。</p>{boundary}<div class="source-actions"><a href="#videos" data-source-channel="{e(channel)}">查看此頻道的主要影片 ↓</a><a href="{e(p["reference_url"])}" target="_blank" rel="noopener">{e(p["reference_label"])}（新分頁）↗</a></div></details>')
    video_html = []
    statuses = {'approved':'已通過策展審閱','draft':'待審閱','medical-review':'審閱中'}
    for r in sorted(rows, key=lambda r:(list(by_site).index(r['site']),r['learning_tier']!='core',r['chapter'],r['unit_id'])):
        course = by_site[r['site']]
        course_url = f'http://127.0.0.1:{course["previewPort"]}/' if preview else course['url']
        tier = '核心必看' if r['learning_tier'] == 'core' else '延伸學習'
        qualification = f'<a href="{e(r["qualification_evidence_url"])}">課程所列講者／資格資料 ↗</a>' if r['qualification_evidence_url'] else '未提供資格資料連結'
        gap = '<p class="source-gap">待補查：講者姓名或資格資料欄位不完整；不因列為核心而視為已核實。</p>' if r['qualification_gap'] else ''
        scope = e(r['scope_note']) or '以原單元所列診斷範圍為準。'
        segment = f'<p><strong>診斷選段：</strong>{e(r["diagnostic_segment_range"])}。外部原片不會自動停止在選段結尾。</p>' if r['diagnostic_segment_range'] else ''
        classic = f'<p><strong>原課程經典收錄理由：</strong>{e(r["classic_exception_reason"])}</p>' if r['classic_exception_reason'] else ''
        video_html.append(f'''<details class="video-record" data-video-id="{r['video_id']}" data-site="{r['site']}" data-tier="{r['learning_tier']}" data-channel="{e(r['verified_channel'])}"><summary><span class="video-title">{e(r['name'])}</span><span class="video-caption">{course['name']} · {tier} · {e(r['verified_channel'])} · {e(r['verified_upload_date'])}</span></summary><div class="video-detail"><p class="original-title" lang="en">{e(r['verified_title'])}</p><p><strong>教學重要性｜原課程收錄理由：</strong>{e(r['why'])}</p><dl><dt>發布來源</dt><dd>{e(r['verified_channel'])}</dd><dt>講者</dt><dd>{e(r['presenter']) or '尚未具名'}；{qualification}</dd><dt>原單元</dt><dd>{e(r['unit_name'])} · {statuses.get(r['unit_review_status'],e(r['unit_review_status']))}</dd><dt>日期</dt><dd>上傳 {e(r['verified_upload_date'])}；{e(r['age_group'])}。{e(r['date_basis'])}</dd></dl>{gap}<p><strong>使用範圍：</strong>{scope}</p>{segment}{classic}<div class="source-actions"><a href="{e(course_url+'#'+r['unit_id'])}">進入對應課程單元</a><a href="{e(r['url'])}" target="_blank" rel="noopener">觀看 YouTube 原片（新分頁）↗</a></div></div></details>''')
    template = (ROOT / 'sources.template.html').read_text()
    replacements = {'{{PROFILES}}':''.join(profile_html),'{{PROVIDERS}}':''.join(directory),'{{VIDEOS}}':''.join(video_html),'{{SITE_OPTIONS}}':''.join(options),'{{CORE_COUNT}}':str(len(core)),'{{UNIQUE_CORE}}':str(len({r['video_id'] for r in core})),'{{ALL_COUNT}}':str(len(rows)),'{{CHANNEL_COUNT}}':str(len(directory))}
    for key,value in replacements.items():
        template = template.replace(key,value)
    (out / 'sources.html').write_text(template)
    columns = ['site_title','learning_tier','name','verified_title','verified_channel','presenter','verified_upload_date','why','scope_note','diagnostic_segment_range','qualification_evidence_url','qualification_gap','url']
    for filename, selected in [('all-video-sources.csv',rows),('core-video-sources.csv',core)]:
        with (out / filename).open('w',encoding='utf-8-sig',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=columns);writer.writeheader()
            for r in selected:
                values={k:str(r.get(k) or '') for k in columns}
                writer.writerow({k:("'"+v if v.startswith(('=','+','-','@')) else v) for k,v in values.items()})
    return intro
