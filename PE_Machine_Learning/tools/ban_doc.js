(() => {
  'use strict';
  const course = JSON.parse(document.querySelector('#course-data').textContent);
  const storageKey = 'pe-primm-2026-v2';
  let saved = {};
  try { saved = JSON.parse(localStorage.getItem(storageKey) || '{}') || {}; } catch {}
  let storeWarningShown = false;
  function persist() {
    try { localStorage.setItem(storageKey, JSON.stringify(saved)); }
    catch {
      if (!storeWarningShown) {
        storeWarningShown = true;
        const message = document.createElement('p');
        message.className = 'web gate';
        message.textContent = 'Trình duyệt chưa lưu được tiến độ. Bài làm vẫn còn trong thẻ hiện tại.';
        document.querySelector('.toolbar').after(message);
      }
    }
  }
  function stateFor(id) {
    if (!saved[id]) saved[id] = { sets:{}, notes:{}, editors:{} };
    return saved[id];
  }
  function equal(actual, expected, eps) {
    if (Array.isArray(expected)) return Array.isArray(actual) && actual.length === expected.length &&
      expected.every((v,i) => equal(actual[i],v,eps));
    if (typeof expected === 'number') return typeof actual === 'number' &&
      Number.isFinite(actual) && Math.abs(actual-expected) <= eps;
    return actual === expected;
  }
  function pcaEqual(actual, expected, eps) {
    if (!Array.isArray(actual) || actual.length !== 3 || !equal(actual[0],expected[0],eps) ||
      !equal(actual[2],expected[2],eps)) return false;
    const U=actual[1], V=expected[1];
    if (!Array.isArray(U) || U.length !== V.length ||
      !U.every((row,i) => Array.isArray(row) && row.length === V[i].length &&
        row.every(n => typeof n === 'number' && Number.isFinite(n)))) return false;
    return V[0].every((_,j) => [1,-1].some(sign => V.every((row,i) => Math.abs(U[i][j]-sign*row[j]) <= eps)));
  }
  function output(el,message,cls='') { el.replaceChildren(); el.classList.remove('ok','bad');
    if (cls) el.classList.add(cls); el.textContent=message;
  }
  function displaySet(sheet, box) {
    const id=sheet.id, label=box.dataset.set, record=stateFor(id).sets[label];
    const form=box.querySelector('form'), msg=box.querySelector('.result'), reveal=box.querySelector('.reveal');
    form.elements.answer.value=record?.value || '';
    const waiting=label[0]==='R' && !stateFor(id).sets['E'+label[1]]?.submitted;
    const frozen=Boolean(record?.revealed || record?.ok || waiting);
    reveal.hidden=!record?.submitted || (label[0]==='R' && !record.ok);
    form.elements.answer.disabled=frozen;
    form.querySelector('button').disabled=frozen;
    if (waiting) {output(msg,'Nộp E'+label[1]+' trước để mở bộ làm lại này.');return}
    if (!record?.submitted) { output(msg,''); return; }
    const info=course.lessons[id];
    let txt=record.ok ? 'Đúng. Đã ghi kết quả cho '+label+'.' : 'Chưa khớp. '+(label.endsWith('2')?info.hint:info.general);
    if (record.revealed) txt+=' Kết quả đối chiếu '+JSON.stringify(info.keys[label])+'.';
    if (record.revealed && !record.ok && label[0]==='E') txt+=' Hãy làm R'+label[1]+' để kiểm lại vị trí này.';
    if(label==='S' && record.firstAt) txt+=' Lần nộp đầu '+new Date(record.firstAt).toLocaleDateString('vi-VN')+
      (record.firstOk?' · đúng.':' · cần ôn.')+' Số lần nộp: '+record.attempts+'.';
    if(record.revealed) reveal.hidden=true;
    output(msg,txt,record.ok?'ok':'bad');
  }
  function gate(sheet) {
    const s=stateFor(sheet.id).sets;
    const points=[1,2,3,4].map(i=>Boolean(s['E'+i]?.ok || s['R'+i]?.ok));
    const score=points.filter(Boolean).length, open=score>=3 && points[1];
    sheet.querySelector('.transfer').hidden=!open;
    sheet.querySelector('.locked-note').hidden=open;
    sheet.querySelector('.gate').textContent=(open?'Đã mở F. ':'Mốc mở F · ')+
      'Đã đạt '+score+'/4 vị trí. Vị trí 2 '+(points[1]?'đã đạt.':'cần đạt.')+
      ' Mỗi vị trí tính một lần từ Ei hoặc Ri, cần ít nhất 3/4.';
  }
  const initialized=new Set();
  function initSheet(sheet) {
    if (initialized.has(sheet.id)) return;
    initialized.add(sheet.id);
    const state=stateFor(sheet.id), data=course.lessons[sheet.id];
    sheet.querySelectorAll('[data-note]').forEach(n=>{
      n.value=state.notes[n.dataset.note] || '';
      n.addEventListener('input',()=>{state.notes[n.dataset.note]=n.value;persist()});
    });
    sheet.querySelectorAll('.editor').forEach(ed=>{
      const k=ed.dataset.editor, box=ed.querySelector('textarea');
      box.value=state.editors[k] ?? (k==='sample'?data.sample:data.starter);
      box.addEventListener('input',()=>{state.editors[k]=box.value;persist()});
    });
    sheet.querySelectorAll('[data-set]').forEach(box=>{
      displaySet(sheet,box);
      box.querySelector('input').addEventListener('focus',()=>{
        sheet.querySelector('.sample-code').open=false;
        sheet.querySelector('.sample-result').open=false;
      });
    });
    const future=sheet.querySelector('.future');
    future.open=Boolean(state.sets.S?.submitted);
    future.addEventListener('toggle',()=>{if(future.open){sheet.querySelector('.sample-code').open=false;sheet.querySelector('.sample-result').open=false;}});
    sheet.querySelector('.f-key').hidden=!state.transferSubmitted;
    const sampleResult=sheet.querySelector('.sample-result summary');
    sampleResult.addEventListener('click',e=>{
      if(!(state.notes.predict || '').trim()){
        e.preventDefault();
        const msg=sheet.querySelector('.prediction-msg');
        if(msg)msg.textContent='Ghi dự đoán của bạn rồi mở kết quả để so.';
        sheet.querySelector('[data-note=predict]').focus();
      }
    });
    gate(sheet);
  }
  // Only local course data is rendered as HTML. Learner submissions use textContent.
  function showReview(box,entry) {
    const q=course.questions[box.dataset.q], msg=box.querySelector('.q-output');
    if (!entry?.submitted) return;
    msg.replaceChildren();
    if(q.type==='mcq'){
      const chosen=box.querySelector('input[value="'+entry.value+'"]');
      if(chosen)chosen.checked=true;
      const line=document.createElement('p');
      line.textContent=(q.correct===entry.value?'Đúng. ':'Chưa đúng. ')+(q.notes[entry.value] || '');
      line.className=q.correct===entry.value?'ok':'bad';msg.append(line);
    } else {box.querySelector('textarea').value=entry.value; }
    const details=document.createElement('details'),summary=document.createElement('summary'),body=document.createElement('div');
    summary.textContent='Đối chiếu lời giải';body.innerHTML=q.answer;details.append(summary,body);msg.append(details);
  }
  function initBank(panel){
    if(initialized.has(panel.id))return;
    initialized.add(panel.id);const history=saved.review || {};
    panel.querySelectorAll('[data-q]').forEach(box=>showReview(box,history[box.dataset.q]));
  }
  function route(){
    let id=decodeURIComponent(location.hash.slice(1) || 'start');
    const target=document.getElementById(id),panel=target?.closest('.panel') || document.getElementById('start');
    document.querySelectorAll('.panel').forEach(item=>item.hidden=item!==panel);
    document.getElementById('route').value=panel.id;
    if(panel.classList.contains('sheet'))initSheet(panel);
    if(panel.classList.contains('bank'))initBank(panel);
    if(target && target!==panel) target.scrollIntoView({block:'start'}); else window.scrollTo(0,0);
  }
  document.getElementById('route').addEventListener('change',e=>{location.hash=e.target.value});
  document.getElementById('print').addEventListener('click',()=>window.print());
  addEventListener('hashchange',route);
  let printDetails=[];
  function printOpen(){printDetails=[];document.querySelectorAll('.repairs,.terms,.worked-example details').forEach(el=>{if(!el.open){el.open=true;printDetails.push(el)}})}
  addEventListener('beforeprint',printOpen);addEventListener('afterprint',()=>{printDetails.forEach(el=>el.open=false);printDetails=[]});
  document.addEventListener('submit',e=>{
    e.preventDefault();
    const form=e.target,sheet=form.closest('.sheet'), set=form.closest('[data-set]');
    if(sheet && set){
      const label=set.dataset.set,state=stateFor(sheet.id),raw=form.elements.answer.value.trim();
      const last=state.sets[label];
      if(!raw || last?.revealed || last?.ok || (label[0]==='R' && !state.sets['E'+label[1]]?.submitted))return;
      let value;
      try{value=JSON.parse(raw);}catch{output(set.querySelector('.result'),'Dùng số hoặc danh sách như [1.25,0.65]. Với chuỗi, dùng dấu ngoặc kép.','bad');return}
      const expected=course.lessons[sheet.id].keys[label];
      const good=sheet.id==='ML25'?pcaEqual(value,expected,1e-6):equal(value,expected,sheet.id==='ML05'?1e-9:1e-6);
      state.sets[label]={value:raw,submitted:true,ok:good,revealed:false,
        firstAt:last?.firstAt || Date.now(),firstOk:last?.firstOk ?? good,attempts:(last?.attempts || 0)+1};
      persist();displaySet(sheet,set);
      if(label[0]==='E')displaySet(sheet,sheet.querySelector('[data-set="R'+label[1]+'"]'));
      gate(sheet);return;
    }
    const box=form.closest('[data-q]');
    if(!box)return;
    const id=box.dataset.q,q=course.questions[id];
    const value=q.type==='mcq'?form.querySelector('input:checked')?.value:form.elements.attempt.value.trim();
    if(!value){output(box.querySelector('.q-output'),'Hãy ghi bài làm hoặc chọn một phương án trước khi nộp.');return}
    saved.review ||= {};saved.review[id]={value,submitted:true};persist();showReview(box,saved.review[id]);
  });
  function pythonLiteral(x){if(Array.isArray(x))return '['+x.map(pythonLiteral).join(', ')+']';return typeof x==='string'?JSON.stringify(x):String(x);}
  const runtimeBase='https://cdn.jsdelivr.net/pyodide/v0.27.7/full/';
  function pythonWorker(){
    const body=String.raw`
      let runtime;
      async function init(){
        if(!runtime){
          importScripts(base+'pyodide.js');
          runtime=await loadPyodide({indexURL:base});
          await runtime.loadPackage('numpy');
        }
        return runtime;
      }
      onmessage=async event=>{
        const messages=[];
        try{
          const py=await init();
          py.setStdout({batched:s=>messages.push(s)});py.setStderr({batched:s=>messages.push(s)});
          const ns=py.toPy({__name__:'__main__',_pe_source:event.data});
          let failed=false;
          try{
            await py.runPythonAsync([
              '_pe_status = 0',
              'try:',
              '    exec(compile(_pe_source, "<bai-hoc>", "exec"), globals())',
              'except SystemExit as stopped:',
              '    code = stopped.code',
              '    _pe_status = 0 if code is None else code',
              '    if code is not None and not isinstance(code, int):',
              '        print(code)'
            ].join('\n'),{globals:ns});
            failed=Boolean(ns.get('_pe_status'));
          }finally{ns.destroy();}
          postMessage({txt:messages.join('\n') || 'Mã đã chạy xong.',error:failed});
        }catch(err){postMessage({txt:messages.concat([String(err)]).join('\n'),error:true});}
      };`;
    const url=URL.createObjectURL(new Blob(['const base='+JSON.stringify(runtimeBase)+';\n',body],{type:'text/javascript'}));
    const worker=new Worker(url);URL.revokeObjectURL(url);return worker;
  }
  let worker=null, busy=false;
  function runPython(ed,source){
    const consoleBox=ed.querySelector('.console');
    consoleBox.hidden=false;
    if(busy){output(consoleBox,'Một đoạn mã đang chạy. Hãy đợi kết quả rồi chạy lại.');return}
    busy=true;const previous=ed.querySelector('[data-action=run]');previous.disabled=true;
    output(consoleBox,'Đang chuẩn bị Python và NumPy…');
    let timer;
    function done(text,error,stop){clearTimeout(timer);if(stop && worker){worker.terminate();worker=null}busy=false;previous.disabled=false;output(consoleBox,text,error?'bad':'')}
    try{
      if(!worker)worker=pythonWorker();
      worker.onmessage=e=>done(e.data.txt,Boolean(e.data.error),false);
      worker.onerror=()=>done('Không tải được bộ chạy Python. Kiểm tra Internet hoặc tải mã .py để chạy bằng Python có NumPy.',true,true);
      timer=setTimeout(()=>done('Đã dừng lượt chạy sau 90 giây. Kiểm tra kết nối hoặc vòng lặp rồi thử lại.',true,true),90000);
      worker.postMessage(source);
    }catch{done('Trình duyệt chưa khởi động được Python. Bạn có thể tải mã .py để chạy trên máy.',true,true)}
  }
  document.addEventListener('click',e=>{
    const btn=e.target.closest('button');if(!btn)return;
    const sheet=btn.closest('.sheet');if(!sheet)return;
    const id=sheet.id,state=stateFor(id), data=course.lessons[id];
    if(btn.matches('.reveal')){
      const box=btn.closest('[data-set]'),record=state.sets[box.dataset.set];
      if(!record?.submitted || (box.dataset.set[0]==='R' && !record.ok))return;
      record.revealed=true;persist();displaySet(sheet,box);return;
    }
    if(btn.dataset.load){
      const args=data.sets[btn.dataset.load];
      const source='import numpy as np\n\n'+data.function+'\n\n'+data.parameters.map((k,i)=>k+' = '+pythonLiteral(args[i])).join('\n')+'\nprint('+data.name+'('+data.parameters.join(', ')+'))';
      const ed=sheet.querySelector('[data-editor=sample] textarea');
      sheet.querySelector('.sample-code').open=true;ed.value=source;ed.dispatchEvent(new Event('input'));ed.focus();ed.scrollIntoView({block:'center'});return;
    }
    if(btn.dataset.action==='finish-f'){
      const msg=sheet.querySelector('.f-status');
      if(!(state.notes.transfer || '').trim()){output(msg,'Ghi lời giải hoặc giải thích của bạn trước khi nộp.');return}
      state.transferSubmitted=true;persist();sheet.querySelector('.f-key').hidden=false;
      output(msg,'Đã lưu bài vận dụng. Bạn có thể mở lời giải để tự đối chiếu.','ok');return;
    }
    const ed=btn.closest('.editor');if(!ed)return;
    const src=ed.querySelector('textarea').value;
    if(btn.dataset.action==='run')runPython(ed,src);
    if(btn.dataset.action==='save'){
      const url=URL.createObjectURL(new Blob([src],{type:'text/x-python;charset=utf-8'})),a=document.createElement('a');
      a.href=url;a.download=id+(ed.dataset.editor==='sample'?'_mau':'')+'.py';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
    }
  });
  route();
})();
