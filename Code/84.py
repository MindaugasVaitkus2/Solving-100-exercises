#Please use the pyglet library to create a Hello world application

# I never heard about pyglet before, so:
# https://pypi.python.org/pypi/pyglet/1.2.4
# https://pypi.python.org/pypi/pyglet/1.2.4
# http://pyglet.readthedocs.io/en/pyglet-1.2-maintenance/programming_guide/quickstart.html

import pyglet

# call the default constructor
window = pyglet.window.Window()

# create a label to display text
label = pyglet.text.Label('Hello, world',
						font_name = 'Arial',
						font_size = 36,
						x = window.width//2, y = window.height//2,
						anchor_x = 'center', anchor_y = 'center')

# Use a decorator to attach even handler to object
# on_draw() handler will clear the window tot he default background color (black) and label is drawn
@window.event
def on_draw():
	window.clear()
	label.draw()

pyglet.app.run()
