from pathlib import Path
import json
from PIL import Image,ImageDraw,ImageFont
import pypdfium2 as pdfium
R=Path(__file__).resolve().parents[1]
v=json.loads((R/'qa/pdf-verification.json').read_text(encoding='utf-8'))
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',19)
items=v['rendered'];sheets=[]
for base in range(0,len(items),12):
 group=items[base:base+12];sheet=Image.new('RGB',(960,4*476),'#d7d9da');d=ImageDraw.Draw(sheet)
 for i,row in enumerate(group):
  im=Image.open(R/row['path']);im.thumbnail((300,440));x=(i%3)*320+10;y=(i//3)*476+27
  sheet.paste(im,(x,y));d.text((x,y-25),'Trang '+str(row['page']),font=font,fill='#20252a')
 target=R/'qa/pdf-render'/('contact-'+str(base//12+1)+'.png');sheet.save(target);sheets.append(str(target.relative_to(R)).replace('\\','/'))
pdf=pdfium.PdfDocument(str(R/'Database-Advanced-PE.pdf'));outside=[];empty=[];rects=0
for i in range(len(pdf)):
 page=pdf[i];tp=page.get_textpage();n=tp.count_rects();rects+=n
 if tp.count_chars()<60:empty.append(i+1)
 width,height=page.get_size()
 for j in range(n):
  left,bottom,right,top=tp.get_rect(j)
  if left<25 or right>width-24 or bottom<12 or top>height-12:outside.append({'page':i+1,'rect':j,'bbox':[left,bottom,right,top]})
 tp.close();page.close()
pdf.close()
result={'scope':'All-page text rectangle bounds plus selected contact sheets, not a replacement for visual inspection.','pages':v['pages'],'textRectanglesChecked':rects,'outOfBounds':outside,'sparseTextPages':empty,'contactSheets':sheets}
(R/'qa/pdf-layout-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'rectangles':rects,'outOfBounds':len(outside),'sparsePages':empty,'contactSheets':len(sheets)}));assert not outside,outside[:8]
