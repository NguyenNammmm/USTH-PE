"""Read-only rendering of source figures for the analytics semantic review."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'tmp/pdfs/analytics-source'
OUT.mkdir(parents=True,exist_ok=True)
PDF=Path(r'D:/Downloads/Abraham-Silberschatz-Henry-F.-Korth-S.-Sudarshan-Database-System-Concepts-McGraw-Hill-Education-2019.pdf')
PAGES=[551,554,557,558,559,560,561,562,563,568,571,573]

def render(page):
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','1800','-png','-singlefile',str(PDF),str(OUT/f'source-{page}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

with ThreadPoolExecutor(max_workers=2) as pool:
    list(pool.map(render,PAGES))
for i in range(0,len(PAGES),2):
    canvas=Image.new('RGB',(1800,1250),'white')
    draw=ImageDraw.Draw(canvas)
    for j,page in enumerate(PAGES[i:i+2]):
        im=Image.open(OUT/f'source-{page}.png')
        im.thumbnail((885,1200))
        canvas.paste(im,(j*900+(900-im.width)//2,35))
        draw.text((j*900+10,8),f'PDF page {page}',fill='black')
    canvas.save(OUT/f'contact-{i//2+1}.png')
print('Rendered 12 source pages, 6 readable contact sheets.')
