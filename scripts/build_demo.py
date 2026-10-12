"""Generate version-pinned real-I/O demo input; no wallet or RPC writes."""
import hashlib
import json
from pathlib import Path
import re
import sys
root=Path(__file__).resolve().parents[1]
commit=sys.argv[1]
assert re.fullmatch('[0-9a-f]{40}',commit), 'provide the exact fixture commit'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
p={'dataset_id':'DailyTemperature','version':'2026.1','artifact_sha256':sha(root/'fixtures/derived.csv'),
   'sources':[{'dataset_id':'StationObservations','version':'1.0','artifact_sha256':sha(root/'fixtures/source.csv')}],
   'transformation':'Group all rows by UTC date and compute the arithmetic mean of temperature_c in Celsius; no filtering or enrichment.', 'evidence':[]}
for role,subject,file in [('release','DailyTemperature','release.md'),('source','StationObservations','source.md'),('transform','DailyTemperature','transform.md'),('policy','DailyTemperature','policy.md')]:
    path=root/'fixtures'/file
    p['evidence'].append({'role':role,'subject':subject,'url':f'https://raw.githubusercontent.com/haris4587/LineageSeal/{commit}/fixtures/{file}','sha256':sha(path),'bytes':path.stat().st_size})
(root/'evidence/demo_verified.json').write_text(json.dumps(p,indent=2)+'\n')
p['sources'][0]['version']='2.0'
(root/'evidence/demo_conflicting.json').write_text(json.dumps(p,indent=2)+'\n')
print(json.dumps(p,separators=(',',':')))
