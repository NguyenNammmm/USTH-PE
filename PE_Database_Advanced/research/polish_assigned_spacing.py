"""Repair joined Vietnamese prose in assigned files; do not touch fences/inline code/URLs."""
from pathlib import Path
import collections,math,re,json,unicodedata
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent/'database-pe';rx=re.compile(r'[^\W\d_]+',re.UNICODE)
def syllable_like(w):
 if w.isascii():return True
 n=unicodedata.normalize('NFD',w.lower());base=''.join(c for c in n if not unicodedata.combining(c))
 groups=re.findall('[aeiouy]+',base)
 tones=sum(c in '\u0300\u0301\u0303\u0309\u0323' for c in n)
 return len(groups)<=1 and tones<=1 and all(len(g)<=3 for g in groups)
words=collections.Counter(t.lower() for p in (BASE/'lessons').glob('*.md') for t in rx.findall(p.read_text(encoding='utf-8')) if syllable_like(t))
extra='recompute probe spill scalar aggregate empty correlation correlated decorrelation semijoin antijoin flatten rewrite parameterized invalidation witness COUNTscalar NULLextended buildside nestedloop intrabucket statistics stats Histogram Histograms predicates domains pairs counts full output input processing updater retention field model expected actual bitmap allocation free request hash depth ordered duplicate multiset multiplicity total conflict selectivity cost skew theorem key keys indexed loop join frame invariant operator prefix suffix predicate comparator cardinality estimate frequency exact oracle datarow lifecycle delay fault boundary acknowledgement ACK ackless failure timeout proof semigroup partition buffer path syntax runtime prerequisite version compiler compile test trace prepare commit rollback dataset FD row rowid RID RIDs ID IDs API CPU RAM SSD HDD WAL ARIES LSM CLOCK LRU MRU XOR RAID NULL TRUE FALSE UNKNOWN AND OR NOT DISTINCT UNION ALL INTERSECT EXCEPT SUM COUNT AVG MIN MAX ORDER GROUP BY WITH TIES PE MySQL InnoDB PostgreSQL GiST NVMe SATA PCIe index datatype schema physical logical plane profiler metadata pointer nullable payload property properties fresh stale conditional probability hot cold worker workers benchmark capacity topology coalesced NULLsafe COUNTamount MAXamount MAXNULL COUNTNULL'.split()
for w in extra:words[w.lower()]+=25
def split_token(token):
 low=token.lower()
 if low in words and syllable_like(token) or len(token)<4:return token
 if token.isascii():
  parts=re.findall(r'[A-Z]+(?=[A-Z][a-z]|$)|[A-Z]?[a-z]+',token)
  if ''.join(parts)==token and len(parts)>1 and all(p.lower() in words for p in parts):return ' '.join(parts)
  return token
 n=len(token);dp=[None]*(n+1);dp[0]=(0,[])
 for i in range(n):
  if dp[i] is None:continue
  for j in range(i+1,min(n,i+32)+1):
   w=low[i:j];piece=token[i:j]
   if w not in words:continue
   if len(w)==1 and piece.isascii() and not piece.isupper() and w not in {'a','i','k','m','n','p','q','r','s','t','v','x','y'}:continue
   cost=dp[i][0]+2+math.log1p(1200/words[w])
   if dp[j] is None or cost<dp[j][0]:dp[j]=(cost,dp[i][1]+[piece])
 if dp[n] and len(dp[n][1])>1:return ' '.join(dp[n][1])
 return token
repairs={'int ra bucket':'intrabucket','cá cs ta ts':'các stats','s ta ts':'stats','khóau ni quenhãn':'khóa unique; chỉ một nhãn','cá cs':'các','củarow':'của row','fullrecompute':'full recompute','nestedloop':'nested loop','buildside':'build side','outputsize':'output size','rowidentity':'row identity','MAYBEchưaexact':'MAYBE chưa kiểm exact'}
ids=list(range(23,38))+list(range(74,81));changes=[];unresolved=[]
for ident in ids:
 p=ROOT/'lessons'/f'AD{ident:02}.md'
 if not p.exists():continue
 out=[];fence=False
 for line in p.read_text(encoding='utf-8').splitlines():
  if line.startswith('```'):fence=not fence;out.append(line);continue
  if fence:out.append(line);continue
  chunks=re.split(r'(`[^`]*`|https?://[^\s)]+)',line)
  for i in range(0,len(chunks),2):
   for a,b in repairs.items():chunks[i]=chunks[i].replace(a,b)
   def sub(m):
    old=m[0];new=split_token(old)
    if new!=old:changes.append({'lesson':p.stem,'old':old,'new':new})
    elif not syllable_like(old) and len(old)>6:unresolved.append({'lesson':p.stem,'token':old})
    return new
   chunks[i]=rx.sub(sub,chunks[i])
   chunks[i]=re.sub(r'(?<=[A-Za-zÀ-ỹ])(?=\d)', ' ', chunks[i]);chunks[i]=re.sub(r'(?<=\d)(?=[A-Za-zÀ-ỹ])', ' ', chunks[i])
   chunks[i]=re.sub(r'(AD|Q|I|S|D|O|P|M|T|Z|F)\s+(\d+)',r'\1\2',chunks[i]);chunks[i]=chunks[i].replace('DSC 7 e','DSC7e')
   chunks[i]=re.sub(r'(?<=[a-zÀ-ỹ])(AD\d+|Q\d+|I\d+)',r' \1',chunks[i])
  out.append(''.join(chunks))
 p.write_text('\n'.join(out)+'\n',encoding='utf-8')
report={'changes':changes,'unresolved':unresolved}
(ROOT/'research/assigned-spacing-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'changes':len(changes),'unresolved':unresolved[:80]},ensure_ascii=False))
