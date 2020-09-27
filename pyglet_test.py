import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()
window.set_caption("Test")

image = pyglet.resource.image("kitten.png")
label = pyglet.text.Label("Hello, world!", font_name="Times New Roman", font_size=36, x=window.width//2, y=window.height//4, anchor_x="center", anchor_y="center", color=(30, 30, 45, 255))

music = pyglet.resource.media("title_theme.mp3")
music.play()

event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("The left mouse button was pressed here:", (x, y))

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print("The 'A' key was pressed")

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    label.draw()

pyglet.app.run()
