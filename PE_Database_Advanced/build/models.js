(function(root){
'use strict';
// Finite teaching models. None of these functions executes MySQL or PostgreSQL.
function closure(attrs,fds,seed){
 const domain=new Set(attrs),known=new Set(seed);if([...known].some(x=>!domain.has(x)))throw Error('Thuộc tính đầu vào ngoài schema');
 for(const f of fds)if([...f.left,...f.right].some(x=>!domain.has(x)))throw Error('FD dùng thuộc tính ngoài schema');
 const steps=[{known:[...known].sort(),rule:null}];let changed=true;
 while(changed){changed=false;for(let i=0;i<fds.length;i++){const f=fds[i];if(f.left.every(x=>known.has(x))){const added=f.right.filter(x=>!known.has(x));if(added.length){added.forEach(x=>known.add(x));steps.push({known:[...known].sort(),rule:i,added});changed=true}}}}
 return {attributes:[...known].sort(),steps};
}
function parseFD(schema,text){
 const attrs=[...new Set(schema.toUpperCase().match(/[A-Z]/g)||[])];if(!attrs.length||attrs.length>8)throw Error('Dùng từ1 đến8 thuộc tính A–Z');
 const fds=text.split(/[;\n]+/).filter(x=>x.trim()).map(part=>{const p=part.trim().toUpperCase().split(/->|→/);if(p.length!==2)throw Error('Viết FD dạng AB->C; dùng dấu ; để ngăn cách');const left=[...new Set(p[0].match(/[A-Z]/g)||[])],right=[...new Set(p[1].match(/[A-Z]/g)||[])];if(!right.length)throw Error('Vế phải cần thuộc tính');return {left,right}});return {attrs,fds};
}
function topo(vertices,edges){const indeg=Object.fromEntries(vertices.map(v=>[v,0]));for(const [a,b] of edges){if(!(a in indeg)||!(b in indeg))throw Error('Đỉnh không có trong schema graph');indeg[b]++}const queue=vertices.filter(v=>indeg[v]===0),order=[];while(queue.length){queue.sort();const v=queue.shift();order.push(v);for(const [a,b] of edges)if(a===v&&!--indeg[b])queue.push(b)}return {acyclic:order.length===vertices.length,order,remaining:vertices.filter(v=>!order.includes(v))}}
function conflict(schedule){
 const ops=schedule.split(/[,;\n]+/).filter(x=>x.trim()).map(s=>{const m=s.trim().match(/^([rw])(\d+)\(([A-Za-z][A-Za-z0-9]*)\)$/i);if(!m)throw Error('Dùng r1(A),w2(A); model chỉ xét read/write single-version');return {kind:m[1].toLowerCase(),tx:'T'+m[2],item:m[3].toUpperCase()}});if(ops.length>30)throw Error('Tối đa30 thao tác cho model');
 const vertices=[...new Set(ops.map(o=>o.tx))].sort(),map=new Map();for(let i=0;i<ops.length;i++)for(let j=i+1;j<ops.length;j++){const a=ops[i],b=ops[j];if(a.tx!==b.tx&&a.item===b.item&&(a.kind==='w'||b.kind==='w')){const key=a.tx+'>'+b.tx;if(!map.has(key))map.set(key,{from:a.tx,to:b.tx,witness:[i+1,j+1],item:a.item})}}
 const edges=[...map.values()];return {ops,vertices,edges,...topo(vertices,edges.map(e=>[e.from,e.to]))};
}
function externalSort(pages,buffers){
 pages=Number(pages);buffers=Number(buffers);if(!Number.isInteger(pages)||pages<1||pages>1e6||!Number.isInteger(buffers)||buffers<3||buffers>1e4)throw Error('Dùng N=1..1.000.000 page và B=3..10.000 buffer');
 const fanIn=buffers-1,runs=[Math.ceil(pages/buffers)];while(runs[runs.length-1]>1)runs.push(Math.ceil(runs[runs.length-1]/fanIn));return {pages,buffers,fanIn,runs,mergePasses:runs.length-1,io:2*pages*runs.length,assumption:'Mỗi pass đọc+ghi N page; không tính final pipelining, CPU hoặc cache. Đây là I/O model.'};
}
function optimizeChain(cards){
 if(!Array.isArray(cards)||cards.length<2||cards.length>6||cards.some(x=>!Number.isInteger(x)||x<1||x>1e4))throw Error('Dùng2..6 relation có1..10.000 row');
 // Cross product model, logical order fixed, associative interval parenthesization.
 // Cost: intermediate output tuple count; scan cost omitted equally. No engine optimizer claim.
 const n=cards.length,dp=Array.from({length:n},()=>Array(n).fill(null)),trace=[];for(let i=0;i<n;i++)dp[i][i]={cost:0,rows:cards[i],plan:String.fromCharCode(65+i)};
 for(let len=2;len<=n;len++)for(let i=0;i+len<=n;i++){const j=i+len-1,candidates=[];for(let k=i;k<j;k++){const l=dp[i][k],r=dp[k+1][j],rows=l.rows*r.rows,cost=l.cost+r.cost+rows;candidates.push({split:k,rows,cost,plan:'('+l.plan+'×'+r.plan+')'})}dp[i][j]=candidates.reduce((a,b)=>a.cost<=b.cost?a:b);trace.push({range:[i,j],candidates,best:dp[i][j]})}return {best:dp[0][n-1],trace,assumption:'Mô hình tích Descartes theo thứ tự A..N, chi phí là tổng tuple trung gian. Không có selectivity/properties/physical cost; không phải plan MySQL.'};
}
function windowTotals(rows,mode){
 const sorted=rows.map(r=>({...r})).sort((a,b)=>a.day-b.day||a.id-b.id);let sum=0;
 if(mode==='rows')return sorted.map(r=>({...r,total:(sum+=r.value)}));
 if(mode!=='range')throw Error('Chọn ROWS hoặc RANGE');
 return sorted.map(r=>({...r,total:sorted.filter(x=>x.day<=r.day).reduce((a,x)=>a+x.value,0)}));
}
function merkleDiff(a,b){if(a.length!==b.length||a.length<1||a.length>16||((a.length&(a.length-1))!==0))throw Error('Dùng cùng sốleaf làlũythừa2, tốiđa16');const visits=[],different=[];function go(lo,hi){const equal=a.slice(lo,hi).every((v,i)=>v===b[lo+i]);visits.push({lo,hi,equal});if(equal)return;if(hi-lo===1){different.push(lo);return}const mid=(lo+hi)/2;go(lo,mid);go(mid,hi)}go(0,a.length);return {visits,different,assumption:'So giá trị leaf trực tiếp làm oracle giảng dạy; không tính hash mật mã. Merkle protocol thật cần canonicalization và hash assumptions.'}}
function gcounter(states){if(!states.length||states.some(s=>s.length!==states[0].length||s.some(x=>!Number.isSafeInteger(x)||x<0)))throw Error('Vector không hợp lệ');const merged=states[0].map((_,i)=>Math.max(...states.map(s=>s[i])));return {merged,value:merged.reduce((a,x)=>a+x,0)}}
function ariesExample(pageP, pageQ){
 if(![0,20,60,70].includes(pageP)||![0,40,80].includes(pageQ))throw Error('Chọn pageLSN từcácmốc cótrongvídụ');
 const log=[{lsn:20,tx:'T1',page:'P',field:'A',value:10,kind:'update'},{lsn:40,tx:'T2',page:'Q',field:'B',value:20,kind:'update'},{lsn:60,tx:'T2',page:'P',field:'C',value:30,kind:'update'},{lsn:70,tx:'T2',page:'P',field:'C',value:0,kind:'clr',undoNext:40}];
 // All durable records through CLR70; storage versions chosen from valid prefixes.
 const pages={P:{lsn:pageP,A:pageP>=20?10:0,C:pageP===60?30:0},Q:{lsn:pageQ,B:pageQ===40?20:0}};
 if(pageQ===80)throw Error('CLR80 chưa có trong log bền tới70; chọn Q0 hoặcQ40');
 const states=[{label:'Sauanalysis',pages:JSON.parse(JSON.stringify(pages)),detail:'DPT P:20,Q:40; T1 winner, T2 loser; lastLSN T2=70.'}];
 for(const r of log){const skip=pages[r.page].lsn>=r.lsn;if(!skip){pages[r.page][r.field]=r.value;pages[r.page].lsn=r.lsn}states.push({label:(skip?'Bỏredo ':'Redo ')+r.lsn,pages:JSON.parse(JSON.stringify(pages)),detail:skip?'pageLSN đã bao record.':(r.kind==='clr'?'Áp hành động bù đã ghi bền.':'Lặp lại update của lịch sử.')})}
 states.push({label:'Undo gặpCLR70',pages:JSON.parse(JSON.stringify(pages)),detail:'KhôngundoCLR; theo undoNextLSN=40.'});pages.Q.B=0;pages.Q.lsn=80;states.push({label:'CLR80 bùupdate40',pages:JSON.parse(JSON.stringify(pages)),detail:'GhiCLR80 vớiundoNextLSN=30, tuânWAL; T2 kếtthúc, A10,B0,C0.'});return {states,assumption:'Mô hình ARIES của AD44, log bền tớiCLR70; khôngchạy/crash InnoDB. TrạngtháiP/Q phải thuộc cácprefix hợp lệ đãđịnh nghĩa.'};
}
const api={closure,parseFD,topo,conflict,externalSort,optimizeChain,windowTotals,merkleDiff,gcounter,ariesExample};
if(typeof module==='object'&&module.exports)module.exports=api;else root.AdvancedModels=api;
})(typeof window!=='undefined'?window:globalThis);
