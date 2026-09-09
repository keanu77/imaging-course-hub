"""Refresh the directory from current syllabuses, retaining dated verification metadata."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
repos = {"knee":"knee-imaging-course-design", "hip":"hip-imaging-course", "ankle-foot":"ankle-foot-imaging-course", "shoulder":"shoulder-ultrasound-course", "cervical":"cervical-imaging-course", "lumbar":"lumbar-imaging-course", "wrist-hand":"wrist-hand-imaging-course"}
inventory = json.loads((ROOT.parent / 'imaging-course-review-2026-09-09/video-inventory.json').read_text())
lookup = {}
for site, repo in repos.items():
    source = json.loads((ROOT.parent / repo / 'course/data/syllabus.json').read_text())
    for chapter in source['chapters']:
        for unit in chapter['units']:
            videos = unit.get('drills', []) + unit.get('lessons', [])
            if unit.get('lesson'):
                videos.append(unit['lesson'])
            for video in videos:
                match = re.search(r'(?:v=|youtu\.be/)([\w-]{11})', video['url'])
                assert match, video['url']
                lookup[site, unit['id'], match[1]] = (unit, video)
records = []
fields = ['site','site_title','unit_id','unit_name','chapter','unit_review_status','video_id','name','url','channel','presenter','presenter_qualification','qualification_evidence_url','learning_tier','why','scope_note','diagnostic_segment_range','classic_exception_reason','verified_title','verified_channel','verified_upload_date','original_content_date','date_note','age_basis_date','date_basis','age_group','metadata_checked_at','availability','qualification_gap','source_authority']
for old in inventory['placements']:
    key = old['site'], old['unit_id'], old['video_id']
    assert key in lookup, key
    unit, video = lookup.pop(key)
    assert video.get('learning_tier', 'extension') == old['learning_tier'], key
    row = {field:old.get(field) for field in fields}
    for field in ['name','why','scope_note','presenter','presenter_qualification','qualification_evidence_url','diagnostic_segment_range','classic_exception_reason']:
        if field in video:
            row[field] = video[field]
    row['unit_name'] = unit['name']
    row['unit_review_status'] = unit.get('review_status', 'draft')
    row['qualification_gap'] = not row['presenter'] or not row['qualification_evidence_url']
    records.append(row)
assert not lookup, list(lookup)[:5]
(ROOT / 'video-sources.json').write_text(json.dumps({'prepared_at':'2026-09-10','metadata_snapshot_date':inventory['as_of'],'date_cutoff':inventory['cutoff'],'records':records},ensure_ascii=False,indent=2))
print('records',len(records),'core',sum(r['learning_tier']=='core' for r in records),Counter(r['site'] for r in records))
