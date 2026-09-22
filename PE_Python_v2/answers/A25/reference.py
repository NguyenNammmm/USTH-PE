import math,pyglet
from pyglet.gl import GL_TRIANGLES,GL_DEPTH_TEST,glEnable
from pyglet.graphics.shader import Shader,ShaderProgram
VS="""#version 330 core
in vec3 position; in vec3 color; out vec3 tint;
uniform float angle; uniform float aspect;
void main(){
  float c=cos(angle),s=sin(angle);
  vec3 p=vec3(c*position.x+s*position.z,position.y,-s*position.x+c*position.z);
  p=vec3(p.x,0.94*p.y-0.342*p.z,0.342*p.y+0.94*p.z);
  p.z-=5.0; float f=2.41421356;
  gl_Position=vec4(f*p.x/aspect,f*p.y,-1.002002*p.z-0.2002002,-p.z);
  tint=color;
}"""
FS="""#version 330 core
in vec3 tint; out vec4 outputColor;
void main(){outputColor=vec4(tint,1.0);}
"""
def main():
    window=pyglet.window.Window(640,480,"PE shader cube",resizable=True)
    program=ShaderProgram(Shader(VS,"vertex"),Shader(FS,"fragment"))
    vertices=[(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]
    faces=[(0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(1,2,6,5),(0,3,7,4)]
    palette=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1)]
    positions=[]; colors=[]
    for face,color in zip(faces,palette):
        for j in (0,1,2,0,2,3): positions.extend(vertices[face[j]]); colors.extend(color)
    mesh=program.vertex_list(36,GL_TRIANGLES,position=("f",positions),color=("f",colors))
    keys=pyglet.window.key.KeyStateHandler(); window.push_handlers(keys); angle=0.0
    def update(dt):
        nonlocal angle
        direction=int(keys[pyglet.window.key.RIGHT])-int(keys[pyglet.window.key.LEFT])
        angle=(angle+direction*math.pi/2*dt)%(2*math.pi)
    @window.event
    def on_draw():
        window.clear(); glEnable(GL_DEPTH_TEST); program.use()
        program["angle"]=angle; program["aspect"]=window.width/max(1,window.height)
        mesh.draw(GL_TRIANGLES); program.stop()
    @window.event
    def on_close():
        pyglet.clock.unschedule(update); mesh.delete(); program.delete(); window.close()
    pyglet.clock.schedule_interval(update,1/60); pyglet.app.run()
if __name__=="__main__": main()
