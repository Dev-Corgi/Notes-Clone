import re, requests
from pathlib import Path
repo=Path(r'C:\Working\Apple-Note Clone')
items=[('adding-a-sticker','Adding a sticker','65cd95f0-c0c6-495a-a1d5-1df4bd8b2b23'),('duplicating-a-sticker','Duplicating a sticker','f5d2199f-39c6-4182-b256-0708db73448f'),('removing-a-sticker','Removing a sticker','f99da23f-1d02-445a-be0e-74b41e575d13'),('adding-text','Adding text','0d12c95c-5b90-4cd2-8bdb-ed60d63ba686'),('changing-text-color','Changing text color','5fa24d03-03a3-4cc6-bc0f-29a765504f1b')]
for slug,name,uid in items:
 s=requests.get(f'https://mobbin.com/flows/{uid}',timeout=30).text
 st=s.find(r'\"screens\":['); chunk=s[st:st+80000]
 urls=re.findall(r'screenCdnImgSources.*?src\\":\\"(https://[^"\\]+)',chunk)
 out=repo/'docs/apple-notes/flows'/slug/'screenshots'; out.mkdir(parents=True,exist_ok=True)
 for p in out.glob('*.webp'): p.unlink()
 for i,u in enumerate(urls,1): (out/f'{i:02}.webp').write_bytes(requests.get(u,timeout=30).content)
 nodes='\n'.join(f'  S{i}[Screen {i}]' for i in range(1,len(urls)+1)); edges='\n'.join(f'  S{i} --> S{i+1}' for i in range(1,len(urls))); shots='\n'.join(f'### Screen {i}\n\n![Screen {i}](screenshots/{i:02}.webp)' for i in range(1,len(urls)+1))
 md=f'''# {name}\n\n- App: Apple Notes iOS\n- Capture status: verified\n- Source: [Mobbin detail flow](https://mobbin.com/flows/{uid})\n- Verified screens: {len(urls)}\n\n## Flow chart\n\n```mermaid\nflowchart LR\n{nodes}\n{edges}\n```\n\n## Verified evidence\n\nThe screenshots below are downloaded from the Mobbin detail page for this exact flow.\n\n{shots}\n\n## BMad handoff notes\n\n- Implement the interaction sequence in the Mermaid order.\n- Treat each screenshot as the visual reference for its corresponding state.\n'''
 (repo/'docs/apple-notes/flows'/slug/'README.md').write_text(md,encoding='utf-8'); print(name,len(urls),flush=True)
