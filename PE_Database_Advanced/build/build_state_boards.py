"""Render prepared lesson states, with no claim of live engine execution."""
from pathlib import Path
import hashlib,json,re
from PIL import Image,ImageDraw,ImageFont
R=Path(__file__).resolve().parents[1];OUT=R/'assets/state-boards';OUT.mkdir(parents=True,exist_ok=True)
data=json.loads((R/'manifest.json').read_text(encoding='utf-8'))
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',29)
bold=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',33)
small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',25)
def wrap(text,limit=1115):
 words=text.split();lines=[];line=''
 for word in words:
  new=(line+' '+word).strip()
  if font.getlength(new)>limit and line:lines.append(line);line=word
  else:line=new
 if line:lines.append(line)
 return lines
result=[]
for lesson in data['lessons']:
 if not lesson['key']:continue
 text=(R/lesson['path']).read_text(encoding='utf-8-sig')
 m=re.search(r'^## Minh họa theo trạng thái\s*\n(.*?)(?=^## |\Z)',text,re.M|re.S)
 assert m,lesson['id']+' missing state illustration'
 states=[]
 for line in m[1].splitlines():
  n=re.match(r'^\d+\.\s+(.*)',line)
  if n:states.append(n[1].replace('`',''))
  elif re.match(r'^\|\s*\d+\s*\|',line):
   cells=[x.strip() for x in line.strip('|').split('|')]
   states.append(' · '.join(cells[1:]).replace('`',''))
 assert 4<=len(states)<=8,(lesson['id'],len(states))
 layout=[wrap(s) for s in states];heights=[max(96,48+len(lines)*39) for lines in layout]
 width=1380;height=143+sum(heights)+32*(len(states)-1)+38
 image=Image.new('RGB',(width,height),'#f9f8f5');draw=ImageDraw.Draw(image)
 draw.text((38,27),lesson['id']+' / CÁC TRẠNG THÁI CỦA VÍ DỤ',font=bold,fill='#2d3439')
 draw.text((38,77),'Minh họa biên soạn · Không phải lượt chạy engine mới',font=small,fill='#555d63')
 y=135
 for i,(lines,h) in enumerate(zip(layout,heights)):
  draw.rounded_rectangle((37,y,width-37,y+h),radius=12,fill='#fffdf8',outline='#cecac2',width=2)
  draw.rounded_rectangle((54,y+21,114,y+75),radius=9,fill='#f5dfcc')
  draw.text((62,y+27),str(i+1).zfill(2),font=bold,fill='#95431e')
  for j,line in enumerate(lines):draw.text((139,y+24+j*39),line,font=font,fill='#2d3439')
  y+=h
  if i<len(layout)-1:
   draw.line((84,y+3,84,y+24),fill='#77716a',width=3)
   draw.polygon([(77,y+18),(91,y+18),(84,y+28)],fill='#77716a')
  y+=32
 target=OUT/(lesson['id']+'.png');image.save(target,optimize=True)
 result.append({'id':lesson['id'],'path':str(target.relative_to(R)).replace('\\','/'),'states':states,'width':width,'height':height,'lessonSha256':hashlib.sha256((R/lesson['path']).read_bytes()).hexdigest(),'imageSha256':hashlib.sha256(target.read_bytes()).hexdigest(),'mode':'prepared illustration, not runtime trace'})
(R/'qa/state-boards.json').write_text(json.dumps({'count':len(result),'boards':result},ensure_ascii=False,indent=2),encoding='utf-8')
print('State boards:',len(result))
