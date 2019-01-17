import pyglet
from grid import Terrain
from pyglet.window import key


class Window(pyglet.window.Window):
    def __init__(self):
        super(Window,self).__init__(800, 800)
        self.terrain = Terrain(self.get_size()[0], self.get_size()[1], 10)

    def on_draw(self):
        self.clear()
        self.terrain.draw()
        # resketch = input("Redraw?(y/n)")
        # if resketch == "y":
        # self.terrain.recalc()
        # self.terrain.draw()

    def on_key_press(self, symbol, modification):
        if symbol == key.SPACE:
            self.terrain.recalc()
            print("New World Generated.")
        if symbol == key.UP:
            self.terrain.moveup()
        if symbol == key.DOWN:
            self.terrain.movedown()
        if symbol == key.LEFT:
            self.terrain.moveleft()
        if symbol == key.RIGHT:
            self.terrain.moveright()
        if symbol == key.H:
            self.terrain.heightmaptoggle()

@Window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        print("G!!!!!!!")
    else:
        print("A Keyy!!!")

if __name__ == '__main__':
    window = Window()
    pyglet.app.run()
