"""Native smoke tests, separate from visual/interaction acceptance."""
import os,sys,json,importlib.util,traceback
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=HERE if (HERE/'lesson_bank.json').exists() else HERE.parents[2]/'output/pdf/PE_Python_v2'
if os.environ.get('PE_QA_DEPS'):sys.path.insert(0,os.environ['PE_QA_DEPS'])
def load(ident):
    path=BASE/'answers'/ident/'reference.py';spec=importlib.util.spec_from_file_location('gfx_'+ident,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
results=[]
def check(name,fn):
    try:results.append(dict(name=name,status='PASS',detail=fn()))
    except Exception:results.append(dict(name=name,status='NOT_VERIFIED',reason=traceback.format_exc()))
    print(results[-1]['name'],results[-1]['status'],flush=True)
    (BASE/'QA_graphics_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')

def wx_controls():
    import wx
    app=wx.App(False);a=load('A21');frame,w=a.build_frame()
    try:
        assert frame.GetTitle()=='PE wx' and w['check'].GetValue() is False and w['radio'].GetSelection()==0
        event=wx.CommandEvent(wx.EVT_BUTTON.typeId,w['button'].GetId());w['button'].ProcessWindowEvent(event)
        assert w['text'].GetValue()=='Clicked\n'
        b=load('A23');other=wx.Frame(None);panel=b.TiledPanel(other)
        assert panel.tile.GetWidth()==8 and panel.tile.GetHeight()==8
        other.Destroy();app.ProcessPendingEvents()
        return wx.version()+'; construction, button event, state and bitmap resource verified; resize/paint visual protocol separate.'
    finally:frame.Destroy();app.ProcessPendingEvents();app.Destroy()
if '--wx' in sys.argv: check('wx control events and bitmap',wx_controls)

def pyglet_shader():
    import pyglet
    from pyglet.gl import GL_TRIANGLES,GL_DEPTH_TEST,glEnable,glFinish
    from pyglet.graphics.shader import Shader,ShaderProgram
    a=load('A25');window=pyglet.window.Window(320,240,visible=False)
    try:
        program=ShaderProgram(Shader(a.VS,'vertex'),Shader(a.FS,'fragment'))
        mesh=program.vertex_list(3,GL_TRIANGLES,position=('f',[-1,-1,0,1,-1,0,0,1,0]),color=('f',[1,0,0,0,1,0,0,0,1]))
        window.switch_to();window.clear();glEnable(GL_DEPTH_TEST);program.use();program['angle']=0.3;program['aspect']=320/240
        mesh.draw(GL_TRIANGLES);glFinish()
        folder=BASE/'qa_scratch';folder.mkdir(exist_ok=True)
        pyglet.image.get_buffer_manager().get_color_buffer().save(str(folder/'shader_probe.png'))
        program.stop();mesh.delete();program.delete()
        return 'Shader compiled/linked, attributes/uniforms set and native GL draw captured. Full cube motion/manual protocol separate.'
    finally:window.close()
if '--pyglet' in sys.argv: check('Pyglet shader native draw',pyglet_shader)
(BASE/'QA_graphics_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
