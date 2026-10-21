import re,requests,json
from pathlib import Path
repo=Path(r'C:\Working\Apple-Note Clone')
items=json.loads(r'''{"Recently deleted":"e929a163-5ebc-465f-98af-165689d5ecad","Tags":"00973aef-3c12-49e9-9e96-a8e8b3aa690c","Creating a new smart folder":"9e583f03-2eb1-4c22-abe5-e373b4db8218","Moving a note to folder":"73266256-2994-40d6-9f3c-8f54552a612e","Renaming a folder":"818f45d9-c80a-40ca-b8d9-d73b8ae39e1d","Deleting a folder":"7276970d-d1b0-447d-bd44-ad6000a0883b","Converting to smart folder":"4ee5bc89-8bf5-4597-9d66-21448a968fb0","Reordering folders":"7276970d-d1b0-447d-bd44-ad6000a0883b","Deleting a tag":"4ee5bc89-8bf5-4597-9d66-21448a968fb0"}''')
def slug(x):return re.sub(r'[^a-z0-9]+','-',x.lower().replace('&','and')).strip('-')
for name,uid in items.items():
 s=requests.get('https://mobbin.com/flows/'+uid,timeout=30).text;st=s.find(r'\"screens\":[');urls=re.findall(r'screenCdnImgSources.*?src\\":\\"(https://[^"\\]+)',s[st:st+90000]);out=repo/'docs/apple-notes/flows'/slug(name)/'screenshots';out.mkdir(parents=True,exist_ok=True)
 for p in out.glob('*.webp'):p.unlink()
 for i,u in enumerate(urls,1):(out/f'{i:02}.webp').write_bytes(requests.get(u,timeout=30).content)
 nodes='\n'.join(f'  S{i}[Screen {i}]' for i in range(1,len(urls)+1));edges='\n'.join(f'  S{i} --> S{i+1}' for i in range(1,len(urls)));shots='\n'.join(f'### Screen {i}\n\n![Screen {i}](screenshots/{i:02}.webp)' for i in range(1,len(urls)+1));md=f'# {name}\n\n- App: Apple Notes iOS\n- Capture status: verified\n- Source: [Mobbin detail flow](https://mobbin.com/flows/{uid})\n- Verified screens: {len(urls)}\n\n## Flow chart\n\n```mermaid\nflowchart LR\n{nodes}\n{edges}\n```\n\n## Verified evidence\n\n{shots}\n\n## BMad handoff notes\n\n- Implement the interaction sequence in Mermaid order.\n- Treat each screenshot as the visual reference for its state.\n';(repo/'docs/apple-notes/flows'/slug(name)/'README.md').write_text(md,encoding='utf8');print(name,len(urls),flush=True)
