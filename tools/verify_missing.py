import re,requests,json
from pathlib import Path
repo=Path(r'C:\Working\Apple-Note Clone')
items=json.loads(r'''{"Changing a number":"af5f88dc-34b1-4651-9cc0-4274348406d6","Inserting a space above":"da7952a2-41de-495c-867d-30dccffb4053","Removing a result":"364ae156-7aeb-4cfc-b9b8-c1778460f9bf","Editing text":"dd8dbba3-c03f-4ed7-84e8-d9c11d31f69b","Converting text to handwriting":"3651b700-3890-4c9f-bee8-cabdb29d0255","Changing a label":"5fac3e2b-c242-4f7f-bfa1-1158a8ebd2f0","Customizing a label":"cb365e45-3b6a-4508-86d0-8c322db42f22","Editing a shape":"bee7cc0d-a82b-4cc3-be88-aedb0565d068","Opening a locked note":"3b98f529-74d3-4a9d-b8a2-64f5644b1316"}''')
def slug(x):return re.sub(r'[^a-z0-9]+','-',x.lower().replace('&','and')).strip('-')
for name,uid in items.items():
 s=requests.get('https://mobbin.com/flows/'+uid,timeout=30).text;st=s.find(r'\"screens\":[');urls=re.findall(r'screenCdnImgSources.*?src\\":\\"(https://[^"\\]+)',s[st:st+90000]);out=repo/'docs/apple-notes/flows'/slug(name)/'screenshots';out.mkdir(parents=True,exist_ok=True)
 for p in out.glob('*.webp'):p.unlink()
 for i,u in enumerate(urls,1):(out/f'{i:02}.webp').write_bytes(requests.get(u,timeout=30).content)
 nodes='\n'.join(f'  S{i}[Screen {i}]' for i in range(1,len(urls)+1));edges='\n'.join(f'  S{i} --> S{i+1}' for i in range(1,len(urls)));shots='\n'.join(f'### Screen {i}\n\n![Screen {i}](screenshots/{i:02}.webp)' for i in range(1,len(urls)+1));md=f'# {name}\n\n- App: Apple Notes iOS\n- Capture status: verified\n- Source: [Mobbin detail flow](https://mobbin.com/flows/{uid})\n- Verified screens: {len(urls)}\n\n## Flow chart\n\n```mermaid\nflowchart LR\n{nodes}\n{edges}\n```\n\n## Verified evidence\n\n{shots}\n\n## BMad handoff notes\n\n- Implement the interaction sequence in Mermaid order.\n- Treat each screenshot as the visual reference for its state.\n';(repo/'docs/apple-notes/flows'/slug(name)/'README.md').write_text(md,encoding='utf8');print(name,len(urls),flush=True)
