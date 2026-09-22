import pyglet
from reference import advance
window=pyglet.window.Window(400,300,"Bounce",resizable=True)
square=pyglet.shapes.Rectangle(20,20,20,20,color=(255,0,0))
vx,vy=80,60
paused=False
def update(dt):
    global vx,vy
    square.x,vx=advance(min(square.x,max(1,window.width-20)),vx,dt,max(1,window.width-20))
    square.y,vy=advance(min(square.y,max(1,window.height-20)),vy,dt,max(1,window.height-20))
@window.event
def on_draw():
    window.clear(); square.draw()
@window.event
def on_key_press(symbol,modifiers):
    global paused
    if symbol==pyglet.window.key.SPACE:
        paused=not paused
        pyglet.clock.unschedule(update)
        if not paused: pyglet.clock.schedule_interval(update,1/60)
@window.event
def on_close():
    pyglet.clock.unschedule(update); window.close()
pyglet.clock.schedule_interval(update,1/60)
pyglet.app.run()
