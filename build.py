"""Build a dependency-free course directory; previews never overwrite public links."""
import argparse
import json
import shutil
import os
import subprocess
from html import escape
from pathlib import Path
from source_pages import render_sources

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--preview', action='store_true')
args = parser.parse_args()
data = json.loads((ROOT / 'courses.json').read_text())
cards = []
groups = {key: [] for key in ("upper", "lower", "spine")}
for number, course in enumerate(data, 1):
    url = f'http://127.0.0.1:{course["previewPort"]}/?tab=home' if args.preview else course['url']
    topics = ''.join(f'<li>{escape(t)}</li>' for t in course['topics'])
    cards.append(f'''<article class="course-card" data-region="{course['region']}" id="course-{course['id']}">
      <div class="card-top"><span class="course-number">{number:02}</span><span>{course['regionLabel']}</span></div>
      <p class="course-english" lang="en">{course['english']}</p>
      <h4><a class="course-link" href="{escape(url)}">{course['name']}影像課程<span aria-hidden="true">↗</span></a></h4>
      <p class="course-description">{course['description']}</p>
      <ul>{topics}</ul>
      <div class="card-bottom"><p class="modalities">{course['modalities']}</p><p class="course-status">{course['status']}</p></div>
    </article>''')
    groups[course['region']].append(cards[-1])
labels = {"upper": "上肢影像", "lower": "下肢影像", "spine": "脊椎影像"}
sections = ''.join(f'<section class="course-group" data-region-group="{key}" aria-labelledby="group-{key}"><h3 id="group-{key}">{labels[key]}</h3><div class="group-grid">' + ''.join(group) + '</div></section>' for key, group in groups.items())
html = (ROOT / 'index.template.html').read_text().replace('{{COURSES}}', sections)
html = html.replace('{{PREVIEW}}', '<div class="preview-note">設計預覽 · 課程入口連往本機新版，尚未發布</div>' if args.preview else '')
out = ROOT / ('preview' if args.preview else 'dist')
out.mkdir(exist_ok=True)
source_intro = render_sources(out, data, args.preview)
html = html.replace('{{SOURCES}}', source_intro)
(out / 'index.html').write_text(html)
shutil.copytree(ROOT / 'assets', out / 'assets', dirs_exist_ok=True)
for name in ('_headers', 'robots.txt'):
    shutil.copy2(ROOT / name, out / name)
sha = os.environ.get('CF_PAGES_COMMIT_SHA')
if not sha:
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True)
    sha = result.stdout.strip() if result.returncode == 0 else 'uncommitted'
(out / 'version.json').write_text(json.dumps({'sha': sha}))
print(f'{out}: {len(cards)} courses')
