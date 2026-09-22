import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
V=[(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]
F=[(0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(1,2,6,5),(0,3,7,4)]
C=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1)]
class CubeCanvas(glcanvas.GLCanvas):
    def __init__(self,parent):
        super().__init__(parent,attribList=[glcanvas.WX_GL_RGBA,glcanvas.WX_GL_DOUBLEBUFFER,glcanvas.WX_GL_DEPTH_SIZE,24,0])
        self.context=glcanvas.GLContext(self); self.ax=20; self.ay=30; self.last=None
        self.Bind(wx.EVT_PAINT,self.paint); self.Bind(wx.EVT_SIZE,self.resize)
        self.Bind(wx.EVT_LEFT_DOWN,self.down); self.Bind(wx.EVT_MOTION,self.motion)
        self.Bind(wx.EVT_KEY_DOWN,self.key)
    def resize(self,event): self.Refresh(False); event.Skip()
    def down(self,event): self.SetFocus(); self.last=event.GetPosition()
    def key(self,event):
        if event.GetKeyCode() in (ord("R"),ord("r")):
            self.ax=0; self.ay=0; self.Refresh(False)
        else: event.Skip()
    def motion(self,event):
        if event.Dragging() and event.LeftIsDown() and self.last is not None:
            p=event.GetPosition(); self.ay+=p.x-self.last.x; self.ax+=p.y-self.last.y; self.last=p; self.Refresh(False)
    def paint(self,event):
        dc=wx.PaintDC(self); self.SetCurrent(self.context)
        w,h=self.GetClientSize()
        if w<=0 or h<=0: return
        glViewport(0,0,w,h); glEnable(GL_DEPTH_TEST); glClearColor(.08,.12,.16,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION); glLoadIdentity(); gluPerspective(45,w/h,.1,100)
        glMatrixMode(GL_MODELVIEW); glLoadIdentity(); glTranslatef(0,0,-6)
        glRotatef(self.ax,1,0,0); glRotatef(self.ay,0,1,0)
        glBegin(GL_QUADS)
        for face,color in zip(F,C):
            glColor3f(*color)
            for i in face: glVertex3f(*V[i])
        glEnd(); self.SwapBuffers()
if __name__=="__main__":
    app=wx.App(False); frame=wx.Frame(None,title="OpenGL cube",size=(600,450)); CubeCanvas(frame); frame.Show(); app.MainLoop()
