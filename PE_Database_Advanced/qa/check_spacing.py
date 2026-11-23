"""Find accidentally joined prose tokens. Never alters code or upstream sources."""
from pathlib import Path
import argparse,collections,difflib,json,re
R=Path(__file__).resolve().parents[1];BASE=R.parent/'database-pe/lessons'
vocab=collections.Counter()
for p in BASE.glob('*.md'):
 text=p.read_text(encoding='utf-8-sig');text=re.sub(r'```.*?```','',text,flags=re.S)
 for token in re.findall(r'[^\W_]+',text):vocab[token.casefold()]+=1
vocab.update({'model':50,'worker':50,'record':50,'flush':50,'page':50,'snapshot':50,'prefix':50,'checkpoint':50,'commit':50,'epoch':50,'mapping':50,'delta':50,'ownership':50,'source':50,'semijoin':50,'local':50,'output':50,'operation':50,'prototype':50,'publication':50,'class':50,'duplicate':50,'capability':50,'retry':50,'CLR':50})
def split(token):
 if token.casefold() in vocab or not re.search(r'[À-ỹĐđ]',token) or len(token)<5:return token
 n=len(token);best={n:(0,[])}
 for i in range(n-1,-1,-1):
  choices=[]
  for j in range(i+1,n+1):
   part=token[i:j];key=part.casefold()
   if key not in vocab or j not in best:continue
   # Avoid arbitrary one-letter Latin fragments; retain genuine Vietnamese short words.
   if len(part)==1 and not re.search(r'[À-ỹĐđ]',part):continue
   score=best[j][0]+10-min(vocab[key],50)/100
   choices.append((score,[part]+best[j][1]))
  if choices:best[i]=min(choices,key=lambda x:x[0])
 return ' '.join(best[0][1]) if 0 in best else token
def repair(text):
 changes=collections.Counter();out=[];fenced=False
 for line in text.splitlines(keepends=True):
  if line.lstrip().startswith('```'):fenced=not fenced;out.append(line);continue
  if fenced:out.append(line);continue
  parts=re.split(r'(`[^`]*`|https?://\S+|\]\([^)]*\))',line)
  for i,part in enumerate(parts):
   if i%2:continue
   def replace(m):
    old=m[0];new=split(old)
    if old!=new:changes[(old,new)]+=1
    return new
   parts[i]=re.sub(r'[^\W_]+',replace,part)
  out.append(''.join(parts))
 return ''.join(out),changes
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');parser.add_argument('ids',nargs='+');a=parser.parse_args();report=[]
 for id in a.ids:
  p=R/'lessons'/f'{id}.md'
  if not p.exists():continue
  old=p.read_text(encoding='utf-8-sig');new,c=repair(old)
  report.append({'id':id,'changedOccurrences':sum(c.values()),'tokens':[{'before':x,'after':y,'count':n} for (x,y),n in c.most_common()]})
  if a.apply:p.write_text(new,encoding='utf-8')
 (R/'qa/spacing-preview.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False,indent=2))
