const fs=require('fs'),path=require('path'),assert=require('assert');
const {JSDOM,VirtualConsole}=require(path.resolve(__dirname,'../../../tmp/database-dom-test/node_modules/jsdom'));
const file='C:/Users/HOME/.codex/visualizations/2026/10/01/01a0f51f-5d06-7570-97a2-ef88fc797c5b/database-advanced-flow.html';
const source=fs.readFileSync(file,'utf8');assert(!/<!doctype|<html|<body/i.test(source));assert(source.length<1000000);assert(!/fetch\(|XMLHttpRequest|WebSocket|\\\\"/.test(source));
const errors=[],saved=[];const vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(e.message));
const dom=new JSDOM(source,{runScripts:'dangerously',virtualConsole:vc,beforeParse(w){w.openai={widgetState:{modelContent:{lessonId:'AD03',reminderId:'D04'}},setWidgetState:async s=>saved.push(s)}}});
const w=dom.window,d=w.document;assert.equal(d.querySelectorAll('#daf-lesson option').length,85);assert(d.querySelector('#daf-detail').textContent.includes('student_id'));
const picker=d.querySelector('#daf-lesson');picker.value='AD42';picker.dispatchEvent(new w.Event('change'));assert(d.querySelector('#daf-before').textContent.includes('AD38'));d.querySelector('[data-remind="AD38"]').click();assert(d.querySelector('#daf-label').textContent.includes('AD38'));assert.equal(saved.at(-1).modelContent.reminderId,'AD38');
for(const option of [...picker.options]){picker.value=option.value;picker.dispatchEvent(new w.Event('change'));assert(d.querySelector('#daf-current').textContent.includes(option.value));assert(d.querySelector('#daf-detail').textContent.trim().length>10)}
assert.deepEqual(errors,[]);
fs.writeFileSync(path.join(__dirname,'inline-flow-verification.json'),JSON.stringify({scope:'DOM logic, all85 selections and reminder/persistence; no browser layout verification',passed:true,sourceBytes:Buffer.byteLength(source),runtimeErrors:errors},null,2));console.log('Inline flow:85 selections, reminder and state persistence pass');w.close();
