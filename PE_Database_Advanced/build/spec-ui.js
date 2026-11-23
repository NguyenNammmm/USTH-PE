(function(){'use strict';
const D=window.ADVANCED_DATA,M=window.AdvancedModels,$=s=>document.querySelector(s),esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const by=Object.fromEntries([...D.lessons,...(D.supplementalLessons||[])].map(x=>[x.id,x])),old=Object.fromEntries(D.baselineLessons.map(x=>[x.id,x]));let phase=0,states=[],practiceChoice=null,practice=null;const history={};
function inline(s){const code=[];let t=esc(s).replace(/`([^`]+)`/g,(_,v)=>{code.push('<code>'+v+'</code>');return '@@C'+(code.length-1)+'@@'});t=t.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>').replace(/\[([^\]]+)\]\((https?:\/\/[^)]+|(?:\.\.\/)?[^):]+\.(?:md|sql|json))\)/g,'<a href="$2">$1</a>');code.forEach((v,i)=>t=t.replace('@@C'+i+'@@',v));return t}
function markdown(text){const lines=String(text||'').split(/\r?\n/),out=[];let i=0;while(i<lines.length){let l=lines[i++];if(!l.trim())continue;if(/^```/.test(l)){const b=[];while(i<lines.length&&!/^```/.test(lines[i]))b.push(lines[i++]);i++;out.push('<pre><code>'+esc(b.join('\n'))+'</code></pre>');continue}const h=l.match(/^(#{1,6})\s+(.*)/);if(h){const n=Math.min(6,h[1].length);out.push('<h'+n+'>'+inline(h[2])+'</h'+n+'>');continue}if(l.startsWith('|')){const rows=[l];while(i<lines.length&&lines[i].startsWith('|'))rows.push(lines[i++]);const data=rows.filter(r=>!/^\|[\s:|\-]+\|?$/.test(r));out.push('<div class="table-wrap"><table>'+data.map((r,j)=>'<tr>'+r.replace(/^\||\|$/g,'').split('|').map(c=>'<'+(j?'td':'th')+'>'+inline(c.trim())+'</'+(j?'td':'th')+'>').join('')+'</tr>').join('')+'</table></div>');continue}if(/^[-*] /.test(l)){const li=[l.slice(2)];while(i<lines.length&&/^[-*] /.test(lines[i]))li.push(lines[i++].slice(2));out.push('<ul>'+li.map(v=>'<li>'+inline(v)+'</li>').join('')+'</ul>');continue}if(/^\d+\. /.test(l)){out.push('<p>'+inline(l)+'</p>');continue}const p=[l];while(i<lines.length&&lines[i].trim()&&!/^(#|```|\||[-*] |\d+\. )/.test(lines[i]))p.push(lines[i++]);out.push('<p>'+inline(p.join(' '))+'</p>')}return out.join('\n')}
function go(tab){document.querySelectorAll('.panel').forEach(p=>p.hidden=p.id!=='panel-'+tab);document.querySelectorAll('[data-tab]').forEach(b=>b.setAttribute('aria-current',b.dataset.tab===tab?'page':'false'))}
document.querySelectorAll('[data-tab]').forEach(b=>b.addEventListener('click',()=>go(b.dataset.tab)));
function renderCatalog(){const term=$('#search').value.toLocaleLowerCase('vi').trim(),module=$('#module-filter').value,key=$('#key-filter').checked,ls=D.lessons.filter(x=>(!module||x.module===module)&&(!key||x.key)&&(!term||(x.id+' '+x.title+' '+x.focus).toLocaleLowerCase('vi').includes(term)));$('#lesson-count').textContent=ls.length+' / '+D.lessons.length+' bài Advanced';$('#catalog').innerHTML=ls.map(x=>'<article class="lesson"><p class="tag">'+esc(x.id)+(x.key?' · TRỌNG TÂM':'')+'</p><h3>'+esc(x.title)+'</h3><p>'+esc(x.focus)+'</p><details><summary>Nhắc kiến thức cần trước</summary>'+[...x.oldPrereqs,...x.newPrereqs].map(id=>{const p=by[id]||old[id];return '<p><strong>'+esc(id)+'</strong> · '+esc(p?.title||id)+' '+(by[id]?'<button data-open="'+id+'">Ôn trong trang</button>':'<a href="'+esc(p?.path||'#')+'">Mở bài nền</a>')+'</p>'}).join('')+'</details><p class="muted">'+esc(x.webEnvironment||'Theo capability của từng hoạt động')+'</p><div class="tools"><button data-open="'+x.id+'">Mở bài</button><a href="'+x.path+'">Markdown</a></div></article>').join('');$('#catalog').hidden=false;$('#reader').hidden=true}
$('#module-map').innerHTML=D.modules.map(m=>'<button class="module" data-module="'+esc(m.title)+'"><small>'+m.id+' · '+m.lessonIds.length+' bài</small><h3>'+esc(m.title)+'</h3></button>').join('');D.modules.forEach(m=>$('#module-filter').add(new Option(m.title,m.title)));
$('#module-map').addEventListener('click',e=>{const b=e.target.closest('[data-module]');if(b){$('#module-filter').value=b.dataset.module;$('#search').value='';$('#key-filter').checked=false;renderCatalog()}});
['search','module-filter','key-filter'].forEach(id=>$('#'+id).addEventListener(id==='search'?'input':'change',renderCatalog));
$('#supplement-catalog').innerHTML=(D.supplementalLessons||[]).map(x=>'<article class="lesson"><p class="tag">'+esc(x.id)+'</p><h3>'+esc(x.title)+'</h3><p>'+esc(x.focus)+'</p><div class="tools"><button data-open="'+esc(x.id)+'">Mở phần bổ sung</button><a href="'+esc(x.path)+'">Markdown</a></div></article>').join('');
$('#supplement-catalog').addEventListener('click',e=>{const b=e.target.closest('[data-open]');if(b)openLesson(b.dataset.open)});
function openLesson(id){
 const x=by[id];if(!x)return;
 let content=markdown(x.markdown);
 if(x.stateBoard)content=content.replace('<h2>Minh họa theo trạng thái</h2>','<h2>Minh họa theo trạng thái</h2><figure class="lesson-board"><img src="'+x.stateBoard+'" alt="'+esc(id)+' · Sơ đồ các trạng thái của ví dụ. Nội dung từng bước được chép đầy đủ bên dưới."><figcaption>Minh họa biên soạn từ ví dụ; không phải một lượt engine mới chạy.</figcaption></figure>');
 const labs=(D.repoActivities||[]).filter(a=>a.lessonIds.includes(id));
 if(labs.length)content+='<aside class="linked-labs"><h2>Lab đã chọn cho bài này</h2>'+labs.map(a=>'<h3>'+esc(a.id)+' · '+esc(a.title)+'</h3><p>'+esc(a.oracle)+'</p><p><a href="'+esc(a.contractPath)+'">Đề, phần tự làm và tiêu chí kiểm</a> · <a href="'+esc(a.licenseNotice)+'">Nguồn và quyền dùng</a></p>'+(a.id==='REPO-E01'?'<button data-practice-demo="true">Thử ba dạng luyện hỗ trợ</button>':'')).join('')+'</aside>';
 $('#reader-content').innerHTML=content;$('#reader-file').href=x.path;$('#catalog').hidden=true;$('#reader').hidden=false;go('roadmap');$('#reader').scrollIntoView({block:'start',behavior:'auto'});
}
$('#reader-content').addEventListener('click',e=>{if(e.target.closest('[data-practice-demo]')){go('models');$('#practice-prompt').scrollIntoView({block:'start',behavior:'auto'})}});
$('#catalog').addEventListener('click',e=>{const b=e.target.closest('[data-open]');if(b)openLesson(b.dataset.open)});$('#reader-back').addEventListener('click',renderCatalog);
function controls(html){$('#model-controls').innerHTML=html;$('#model-result').innerHTML='';phase=0;states=[]}
const field=(id,label,value,type='text')=>'<label>'+label+'<input id="'+id+'" type="'+type+'" value="'+esc(value)+'"></label>';
function modelUI(){const kind=$('#model-select').value;if(kind==='closure')controls(field('fd-schema','Schema','ABCD')+field('fd-seed','Tập bắt đầu','AD')+'<label class="wide">FDs<textarea id="fd-rules">A->B; B->C</textarea></label><button id="model-run">Tính closure</button>');if(kind==='conflict')controls('<label class="wide">Lịch read/write<textarea id="schedule">r1(A),r2(A),w1(A),w2(A)</textarea></label><button id="model-run">Dựng graph</button>');if(kind==='sort')controls(field('sort-n','Số page N',100,'number')+field('sort-b','Số buffer B',10,'number')+'<button id="model-run">Tính I/O model</button>');if(kind==='optimizer')controls(field('opt-cards','Row count theo thứ tự A,B,C…','2,100,3')+'<button id="model-run">Tính DP</button>');if(kind==='window')controls('<label>Frame<select id="window-mode"><option value="rows">ROWS · ORDER BY day,id</option><option value="range">RANGE · ORDER BY day</option></select></label><button id="model-run">Tính tổng tích lũy</button>');if(kind==='aries')controls('<label>pageLSN P trên storage<select id="aries-p"><option>0</option><option>20</option><option selected>60</option><option>70</option></select></label><label>pageLSN Q trên storage<select id="aries-q"><option selected>0</option><option>40</option></select></label><button id="model-run">Dựng lại recovery model</button>');if(kind==='counter')controls('<label>Replica A: vector<textarea id="counter-a">1,0,0</textarea></label><label>Replica B: vector<textarea id="counter-b">0,1,0</textarea></label><label>Replica C: vector<textarea id="counter-c">0,0,1</textarea></label><button id="model-run">Merge state</button>');$('#model-run').addEventListener('click',runModel);runModel()}
function table(headers,rows){return '<div class="table-wrap"><table><thead><tr>'+headers.map(x=>'<th>'+esc(x)+'</th>').join('')+'</tr></thead><tbody>'+rows.map(r=>'<tr>'+r.map(x=>'<td>'+esc(x)+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>'}
function runModel(){const kind=$('#model-select').value;try{let h='';if(kind==='closure'){const d=M.parseFD($('#fd-schema').value,$('#fd-rules').value),r=M.closure(d.attrs,d.fds,[...new Set($('#fd-seed').value.toUpperCase().match(/[A-Z]/g)||[])]);h='<h3>Closure: {'+esc(r.attributes.join(','))+'}</h3>'+table(['Bước','FD áp dụng','Thuộc tính đã có'],r.steps.map((s,i)=>[i,s.rule===null?'Khởi đầu':d.fds[s.rule].left.join('')+'→'+d.fds[s.rule].right.join(''),s.known.join(',')]))+'<p class="model-note">Dừng khi không có FD thêm thuộc tính. Đây là computed model; xem AD03 để đọc invariant và chứng minh.</p>'}if(kind==='conflict'){const r=M.conflict($('#schedule').value);h='<div class="graph">'+r.vertices.map(v=>'<span class="node">'+v+'</span>').join('')+'</div>'+table(['Cạnh','Cặp thao tác làm chứng','Item'],r.edges.map(e=>[e.from+' → '+e.to,e.witness.join(' và '),e.item]))+'<p class="feedback">'+(r.acyclic?'Không chu trình; một topological order: '+r.order.join(' → '):'Có chu trình; topological sort chưa lấy hết các đỉnh. Không conflict-serializable trong mô hình này.')+'</p><p class="model-note">Không xét commit/recoverability, snapshot versions hoặc trace engine.</p>'}if(kind==='sort'){const r=M.externalSort($('#sort-n').value,$('#sort-b').value);h='<h3>'+r.io+' page I/O theo mô hình</h3>'+table(['Giai đoạn','Số run'],r.runs.map((n,i)=>[i===0?'Tạo run trong RAM':'Merge pass '+i,n]))+'<p class="model-note">'+esc(r.assumption)+'</p>'}if(kind==='optimizer'){const r=M.optimizeChain($('#opt-cards').value.split(',').map(x=>Number(x.trim())));h='<h3>'+esc(r.best.plan)+'</h3><p>Chi phí model: '+r.best.cost+' tuple trung gian.</p>'+table(['Đoạn','Phương án tốt nhất','Chi phí'],r.trace.map(t=>[t.range.map(x=>String.fromCharCode(65+x)).join('..'),t.best.plan,t.best.cost]))+'<p class="model-note">'+esc(r.assumption)+'</p>'}if(kind==='window'){const r=M.windowTotals([{day:1,id:1,value:10},{day:1,id:2,value:20},{day:2,id:3,value:5},{day:4,id:4,value:7}],$('#window-mode').value);h=table(['day','id','value','running total'],r.map(x=>[x.day,x.id,x.value,x.total]))+'<p class="model-note">RANGE gom peer cùng day; ROWS dùng tie-breaker id. Dữ liệu được tính bằng model, không gửi tới SQL engine.</p>'}if(kind==='aries'){const r=M.ariesExample(Number($('#aries-p').value),Number($('#aries-q').value));states=r.states;phase=0;h='<p class="model-note">'+esc(r.assumption)+'</p><div id="aries-state"></div><div class="step-nav"><button id="aries-prev">← Bước trước</button><p id="aries-step"></p><button id="aries-next">Bước tiếp →</button></div>'}if(kind==='counter'){const a=['a','b','c'].map(id=>$('#counter-'+id).value.split(',').map(x=>Number(x.trim()))),r=M.gcounter(a);h=table(['Replica/state','Vector','Giá trị'],a.map((s,i)=>[String.fromCharCode(65+i),s.join(','),s.reduce((a,x)=>a+x,0)]).concat([['Merge',r.merged.join(','),r.value]]))+'<p class="model-note">State-based grow-only counter: merge bằng max từng thành phần, không cộng các delivery trùng. Không tự bảo vệ invariant số dư hoặc quyền đặt vé.</p>'}$('#model-result').innerHTML=h;if(kind==='aries'){const draw=()=>{phase=Math.max(0,Math.min(phase,states.length-1));const s=states[phase];$('#aries-state').innerHTML='<h3>'+esc(s.label)+'</h3>'+table(['Page','pageLSN','Dữ liệu'],Object.entries(s.pages).map(([id,p])=>[id,p.lsn,Object.entries(p).filter(([k])=>k!=='lsn').map(([k,v])=>k+'='+v).join(', ')]))+'<p>'+esc(s.detail)+'</p>';$('#aries-step').textContent=(phase+1)+'/'+states.length;$('#aries-prev').disabled=phase===0;$('#aries-next').disabled=phase===states.length-1};$('#aries-prev').addEventListener('click',()=>{phase--;draw()});$('#aries-next').addEventListener('click',()=>{phase++;draw()});draw()}}catch(e){$('#model-result').innerHTML='<p class="feedback bad" role="alert">'+esc(e.message)+'</p>'}}
$('#model-select').addEventListener('change',modelUI);
const options=['Dự đoán kết quả SQL','Điền expected cho oracle','Chọn phản ví dụ tối thiểu'];
let practiceStorageAvailable=true;
function practiceSeed(value){const n=Number(value);return Number.isFinite(n)&&n>=1?Math.min(2147483647,Math.floor(n)):17}
function practiceIds(rows,predicate){return rows.filter(predicate).map(row=>row.id).sort((a,b)=>a-b)}
function practiceTarget(row,p){return row.category===p.category&&row.price<=p.maxPrice&&row.rating>=p.minRating}
function practiceWithoutCategory(row,p){return row.price<=p.maxPrice&&row.rating>=p.minRating}
function practiceWithoutRating(row,p){return row.category===p.category&&row.price<=p.maxPrice}
function practiceEqual(actual,expected){return actual.length===expected.length&&actual.every((id,i)=>id===expected[i])}
function practiceSupportText(){
  const support=practice.support;
  return ' Mô hình SQL trong browser; chưa chạy engine và không ghi nhận đạt độc lập.'+
    (support.answer?' Seed này đã mở đáp án.':support.hint?' Seed này đã dùng gợi ý.':' Seed này chưa mở gợi ý/đáp án.')+
    (practiceStorageAvailable?'':' Không lưu được lịch sử vào trình duyệt; trạng thái chỉ còn trong phiên này.');
}
function saveSupport(){
  if(!practice)return;
  history[practice.seed]={hint:practice.support.hint===true,answer:practice.support.answer===true};
  try{localStorage.setItem('pe-advanced-practice',JSON.stringify({seed:practice.seed,history}));practiceStorageAvailable=true}
  catch{practiceStorageAvailable=false}
}
function practiceFeedback(message){$('#practice-feedback').textContent=message+practiceSupportText()}
function invalidatePractice(message){
  if(!practice)return;
  practiceChoice=null;
  practice.lastResult=null;
  practiceFeedback(message||'Câu trả lời đã đổi; kết quả đối chiếu trước hết hiệu lực.');
}
function practiceReady(){
  if(!practice)return false;
  if(practice.seedDirty){practiceFeedback('Seed đã đổi. Bấm tạo lại tình huống trước khi đối chiếu hoặc mở hỗ trợ.');return false}
  return true;
}
function practiceQuery(p,omit){
  const clauses=[];
  if(omit!=='category')clauses.push("category = '"+p.category+"'");
  clauses.push('price <= '+p.maxPrice);
  if(omit!=='rating')clauses.push('rating >= '+p.minRating.toFixed(1));
  return 'SELECT id FROM products\nWHERE '+clauses.join('\n  AND ')+'\nORDER BY id;';
}
function makePractice(){
  const seed=practiceSeed($('#practice-seed').value),base=(seed%1000)*10+1;
  const maxPrice=100+(seed%5)*10,minRating=Number((4+(seed%2)*0.2).toFixed(1));
  const support=history[seed]||{};
  practice={seed,format:seed%3,category:seed%2?'stationery':'book',maxPrice,minRating,
    support:{hint:support.hint===true,answer:support.answer===true},seedDirty:false,lastResult:null};
  practice.rows=[
    {id:base,category:practice.category,price:maxPrice,rating:minRating},
    {id:base+1,category:'game',price:maxPrice-10,rating:Number((minRating+0.4).toFixed(1))},
    {id:base+2,category:practice.category,price:maxPrice-20,rating:Number((minRating-0.5).toFixed(1))},
    {id:base+3,category:practice.category,price:maxPrice+1,rating:Number((minRating+0.3).toFixed(1))}
  ];
  practice.expected=practiceIds(practice.rows,row=>practiceTarget(row,practice));
  practice.missingCategory=practiceIds(practice.rows,row=>practiceWithoutCategory(row,practice));
  practice.missingRating=practiceIds(practice.rows,row=>practiceWithoutRating(row,practice));
  practice.witnesses=practice.rows.filter(row=>practiceTarget(row,practice)!==practiceWithoutRating(row,practice));
  practiceChoice=null;
  $('#practice-seed').value=seed;
  const contract='<p>Lọc sản phẩm có <code>category = '+esc(practice.category)+'</code>, <code>price ≤ '+maxPrice+'</code> và <code>rating ≥ '+minRating.toFixed(1)+'</code>. Trả ID tăng dần, đủ và không thừa hàng.</p>';
  const fixture=table(['id · integer','category · text','price · integer','rating · numeric'],practice.rows.map(row=>[row.id,row.category,row.price,row.rating.toFixed(1)]));
  const scope='<p class="model-note">Fixture bốn hàng không NULL; price tính theo nghìn đồng. Đây là mô hình các điều kiện =, ≤, ≥ và AND trên dữ liệu này, không parse hoặc thực thi SQL.</p>';
  let question='',response='';
  if(practice.format===0){
    question='<p>Query sau đã bỏ điều kiện category. Tính chính xác dãy ID nó trả về, gồm cả hàng ngoài category nếu có.</p><pre><code>'+esc(practiceQuery(practice,'category'))+'</code></pre>';
    response='<label for="practice-ids">Dãy ID theo ORDER BY id, ngăn bằng dấu phẩy hoặc khoảng trắng<input id="practice-ids" type="text" autocomplete="off" placeholder="Ví dụ: 10, 11"></label>';
  }else if(practice.format===1){
    question='<p>Hoàn thiện expected để oracle dưới đây nhận đúng kết quả hợp đồng và bắt mutant <code>return []</code>. Hãy tính ID từ fixture rồi điền literal array; không điền mã JavaScript khác.</p><pre><code>'+esc(practiceQuery(practice))+'\n\nconst expected = /* điền array ở ô bên dưới */;\nfunction accepts(actual) {\n  return actual.length === expected.length &&\n    actual.every((id, i) => id === expected[i]);\n}</code></pre><p><code>actual.every(predicate)</code> riêng lẻ là true khi actual rỗng; nó chưa kiểm kết quả phải có đủ hàng.</p>';
    response='<label for="practice-expected">Điền array số nguyên theo cú pháp JSON, ví dụ [10,11]<textarea id="practice-expected" rows="2" autocomplete="off" placeholder="[...]"></textarea></label>';
  }else{
    question='<p>Query mutant dưới bỏ rating. Chọn một tập con <strong>ít hàng nhất</strong> của fixture khiến query mutant và hợp đồng cho kết quả khác nhau, rồi giải thích vì sao. Chỉ chạy hai query trên tập con đã chọn.</p><pre><code>'+esc(practiceQuery(practice,'rating'))+'</code></pre>';
    response='<fieldset><legend>Các hàng đưa vào phản ví dụ</legend>'+practice.rows.map(row=>'<label><input type="checkbox" name="practice-witness" value="'+row.id+'">ID '+row.id+'</label>').join('')+'</fieldset><label for="practice-explanation">Giải thích ngắn: điều kiện nào đạt, điều kiện nào không đạt, hai query khác nhau thế nào?<textarea id="practice-explanation" rows="3"></textarea></label><p class="muted">Máy kiểm tính khác biệt và tối thiểu của tập hàng. Nội dung giải thích được xem theo rubric: category/price, rating và hai kết quả; không tự chấm đúng ngữ nghĩa từ vài từ khóa.</p>';
  }
  $('#practice-prompt').innerHTML='<p><strong>Seed '+seed+' · '+options[practice.format]+'</strong></p>'+contract+fixture+scope+question;
  $('#practice-options').innerHTML=response;
  saveSupport();
  practiceFeedback('Điền câu trả lời rồi đối chiếu trên fixture.');
}
function practiceParseIds(value){
  const text=String(value).trim();
  if(!text||text==='[]')return [];
  if(!/^\d+(?:\s*(?:,\s*|\s+)\d+)*$/.test(text))throw new Error('Nhập các ID nguyên dương, cách nhau bằng dấu phẩy hoặc khoảng trắng; không nhập SQL.');
  const ids=text.split(/[\s,]+/).map(Number);
  if(ids.some(id=>!Number.isSafeInteger(id)||id<1))throw new Error('Mỗi ID phải là số nguyên dương hợp lệ.');
  return ids;
}
function checkPractice(){
  if(!practiceReady())return;
  try{
    let passed=false,message='';
    if(practice.format===0){
      const actual=practiceParseIds($('#practice-ids').value);
      passed=practiceEqual(actual,practice.missingCategory);
      message=passed?'Dãy ID khớp kết quả query thiếu category.':'Dãy ID chưa khớp. Áp price và rating cho từng hàng; query này không còn lọc category. Giữ thứ tự ID và không lặp hàng.';
    }else if(practice.format===1){
      let expected;
      try{expected=JSON.parse($('#practice-expected').value)}catch{throw new Error('Ô expected cần một JSON array, ví dụ [10,11]; không dùng return, tên biến hoặc dấu chấm phẩy.')}
      if(!Array.isArray(expected)||expected.some(id=>!Number.isSafeInteger(id)||id<1))throw new Error('Expected phải là array chỉ chứa ID nguyên dương.');
      const acceptsCorrect=practiceEqual(practice.expected,expected),acceptsEmpty=practiceEqual([],expected);
      passed=acceptsCorrect&&!acceptsEmpty;
      message='Oracle với expected vừa điền: kết quả đúng → '+acceptsCorrect+'; mutant [] → '+acceptsEmpty+'. '+(passed?'Đã nhận đủ kết quả đúng và bác kết quả rỗng.':'Cần nhận kết quả đúng, đồng thời bác []. Tính lại cả ba điều kiện và dãy ID theo thứ tự.');
    }else{
      const selected=[...document.querySelectorAll('input[name="practice-witness"]:checked')].map(input=>Number(input.value));
      const subset=practice.rows.filter(row=>selected.includes(row.id));
      const target=practiceIds(subset,row=>practiceTarget(row,practice)),mutant=practiceIds(subset,row=>practiceWithoutRating(row,practice));
      const differs=!practiceEqual(target,mutant),minimal=differs&&subset.length===1;
      const explanation=$('#practice-explanation').value.trim();
      passed=minimal&&explanation.length>0;
      message='Trên tập con: hợp đồng → '+JSON.stringify(target)+'; mutant → '+JSON.stringify(mutant)+'. ';
      if(!differs)message+='Tập này chưa phân biệt được hai query.';
      else if(!minimal)message+='Đã phân biệt được, nhưng còn có thể bỏ hàng để được tập nhỏ hơn.';
      else if(!explanation)message+='Tập một hàng là tối thiểu. Hãy bổ sung giải thích theo rubric.';
      else message+='Tập một hàng là tối thiểu; đã nhận phần giải thích để xem theo rubric, chưa tự xác nhận lập luận đúng.';
    }
    practice.lastResult={modelCheckPassed:passed,format:practice.format,explanationReview:practice.format===2?'pending':null};
    practiceFeedback(message);
  }catch(error){
    practice.lastResult=null;
    practiceFeedback(error.message);
  }
}
$('#practice-options').addEventListener('input',()=>invalidatePractice());
$('#practice-options').addEventListener('change',()=>invalidatePractice());
$('#practice-seed').addEventListener('input',()=>{
  if(!practice)return;
  practice.seedDirty=practiceSeed($('#practice-seed').value)!==practice.seed;
  invalidatePractice(practice.seedDirty?'Seed đã đổi; bấm tạo lại tình huống.':'Seed trở lại giá trị hiện tại; cần đối chiếu lại câu trả lời.');
});
$('#practice-new').addEventListener('click',makePractice);
$('#practice-check').addEventListener('click',checkPractice);
$('#practice-hint').addEventListener('click',()=>{
  if(!practiceReady())return;
  practice.support.hint=true;
  practice.lastResult=null;
  saveSupport();
  const hints=[
    'Lập bảng đúng/sai cho price và rating của từng hàng. Đừng thêm lại một điều kiện không có trong query.',
    'Áp đủ ba điều kiện cho từng hàng rồi sắp ID. Oracle phải kiểm cả length và từng vị trí, vì every trên [] có thể đúng dù thiếu hết kết quả.',
    'Tìm hàng mà category và price đều đạt nhưng rating không đạt. Với selection từng hàng, một hàng như vậy đã có thể chứng minh hai query khác nhau.'
  ];
  practiceFeedback(hints[practice.format]);
});
$('#practice-answer').addEventListener('click',()=>{
  if(!practiceReady())return;
  practice.support.answer=true;
  practice.lastResult=null;
  saveSupport();
  let answer;
  if(practice.format===0)answer='Đáp án dãy ID: '+JSON.stringify(practice.missingCategory)+'. Query thiếu category vẫn lấy hàng ở category khác nếu price/rating đạt.';
  else if(practice.format===1)answer='Điền expected = '+JSON.stringify(practice.expected)+'. Với exact oracle: kết quả đúng được nhận; [] bị bác vì khác length. Không dùng every(predicate) một mình để kiểm đủ hàng.';
  else{
    const witness=practice.witnesses[0],subset=[witness];
    answer='Một phản ví dụ tối thiểu là chỉ ID '+witness.id+': category đúng, price '+witness.price+' ≤ '+practice.maxPrice+', nhưng rating '+witness.rating.toFixed(1)+' < '+practice.minRating.toFixed(1)+'. Hợp đồng trả '+JSON.stringify(practiceIds(subset,row=>practiceTarget(row,practice)))+'; mutant trả '+JSON.stringify(practiceIds(subset,row=>practiceWithoutRating(row,practice)))+'. Tập rỗng cho cả hai kết quả rỗng nên không phân biệt được. Đây cũng là rubric cho phần giải thích.';
  }
  practiceFeedback(answer);
});
try{
  const saved=JSON.parse(localStorage.getItem('pe-advanced-practice')||'null');
  if(saved&&typeof saved==='object'){
    if(saved.history&&typeof saved.history==='object'&&!Array.isArray(saved.history)){
      for(const [key,value] of Object.entries(saved.history)){
        if(/^\d+$/.test(key)&&value&&typeof value==='object')history[key]={hint:value.hint===true,answer:value.answer===true};
      }
    }
    $('#practice-seed').value=practiceSeed(saved.seed);
  }
}catch{practiceStorageAvailable=false}
$('#repo-cards').innerHTML=D.repos.map(r=>'<article class="repo"><h3>'+esc(r.repository)+'</h3><p class="status">'+esc(r.status)+'</p><p>'+esc(r.role)+'</p><p>'+esc(r.checks)+'</p><p class="muted">License '+esc(r.license)+' · commit '+esc(r.commit)+'</p><a href="'+esc(r.url)+'">Nguồn upstream</a><details><summary>Quyền dùng, thay đổi và giới hạn</summary><p>'+esc(r.commercialFit)+'</p>'+(r.problems||[]).map(x=>'<p>'+esc(x)+'</p>').join('')+'</details></article>').join('');$('#repo-document').innerHTML=markdown(D.docs['repo-quality']||'');
const sections=D.sections;[...new Set(sections.map(s=>s.chapter))].forEach(c=>$('#source-chapter').add(new Option('Chương '+c,c)));
function renderSources(){const c=$('#source-chapter').value,t=$('#source-search').value.toLocaleLowerCase('vi').trim(),ls=sections.filter(s=>(!c||s.chapter===c)&&(!t||(s.section+' '+s.title).toLocaleLowerCase('vi').includes(t)));$('#source-count').textContent=ls.length+' / '+sections.length+' mục/tiểu mục';$('#source-rows').innerHTML=ls.map(s=>'<tr><td>'+esc(s.section)+'</td><td>'+esc(s.title)+'</td><td>'+(s.owners||[]).map(id=>'<button data-source-lesson="'+id+'">'+id+'</button>').join(' ')+'</td><td>'+esc(s.review||'Đã gán nơi học; đọc bản rà độ sâu riêng')+'</td></tr>').join('')}
$('#source-chapter').addEventListener('change',renderSources);$('#source-search').addEventListener('input',renderSources);$('#source-rows').addEventListener('click',e=>{const b=e.target.closest('[data-source-lesson]');if(b)openLesson(b.dataset.sourceLesson)});
$('#source-document').innerHTML=markdown([D.docs['semantic-coverage-status'],D.docs['slide-semantic-coverage-status'],D.docs['coverage-map']].filter(Boolean).join('\n\n'));$('#runtime-document').innerHTML=markdown([D.docs['web-runner-spec'],D.docs['usth67-web-acceptance']].filter(Boolean).join('\n\n'));$('#teaching-document').innerHTML=markdown(D.docs['teaching-contract']||'');$('#labs-document').innerHTML=markdown(D.docs['repo-labs']||'');$('#qa-document').innerHTML=markdown(D.docs['verification-scope']||'');
renderCatalog();renderSources();modelUI();makePractice();
})();
