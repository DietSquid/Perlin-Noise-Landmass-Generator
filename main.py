import pyglet
from grid import Terrain


class Window(pyglet.window.Window):
    def __init__(self):
        super(Window,self).__init__(950, 950)
        self.terrain = Terrain(self.get_size()[0], self.get_size()[1], 5)

    def on_draw(self):
        self.clear()
        self.terrain.draw()
        # resketch = input("Redraw?(y/n)")
        # if resketch == "y":
        # self.terrain.recalc()
        # self.terrain.draw()

if __name__ == '__main__':
    window = Window()
    pyglet.app.run()
