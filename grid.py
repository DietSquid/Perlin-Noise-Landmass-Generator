import random
import pyglet
from noise import pnoise2, snoise2

octaves = 5
freq = 16.0 * octaves
seed = random.randint(1,999)
class Terrain:
    def __init__(self, window_width, window_height, scale):
        self.grid_width = int(window_width / scale)
        self.grid_height = int(window_height / scale)
        self.scale = scale
        self.cells = []
        self.generate_cells()

    def recalc(self):
        self.cells = []
        self.generate_cells()

    def generate_cells(self):
        #offset ensures randomness of map
        offsetx = random.randrange(1, 99999)
        offsety = random.randrange(1, 99999)
        for row in range(0, self.grid_height):
            self.cells.append([])
            for col in range(0, self.grid_width):
                #where the magic happens ;-)
                self.cells[row].append(int(snoise2(col / freq + offsetx, row / freq + offsety, octaves) * 127.0 + 128.0))


    def draw(self):


        for row in range(0, self.grid_height):
            for col in range(0, self.grid_width):

                    #Drawing a square
                    #But actually drawing two triangles mirrored off the backs of each other
                    #Because this is more efficient somehow???
                    #Both triangles share 2 coordinates, so we need 8 integers instead of 12
                    #(0, 0) (0, 10) (10, 0) (10, 10)
                    square_coords = (row * self.scale, col * self.scale,
                    row * self.scale, col * self.scale + self.scale,
                    row * self.scale + self.scale, col * self.scale,
                    row * self.scale + self.scale, col * self.scale + self.scale)

                    #defining colors
                    #the program defaults to a heightmap along 0 and 255
                    #but by forcing certain values to be colored differently,
                    #We can make fun terrain stuff!
                    #For instance, everything below our threshold becomes water
                    if self.cells[row][col] < 80:
                        rgb = [0, 22, 193]
                    elif self.cells[row][col] < 130:
                        rgb = [0, 0, 255]

                    #Values close to the threshold become sand
                    elif self.cells[row][col] > 129 and self.cells[row][col] < 138:
                        rgb = [255, 255, 204]

                    #various shades of land
                    elif self.cells[row][col] > 137 and self.cells[row][col] < 150:
                        rgb = [30, 94, 33]

                    elif self.cells[row][col] > 149 and self.cells[row][col] < 170:
                        rgb = [37, 122, 42]

                    elif self.cells[row][col] > 169 and self.cells[row][col] < 180:
                        rgb = [49, 145, 54]

                    elif self.cells[row][col] > 179 and self.cells[row][col] < 190:
                        rgb = [118, 224, 124]

                    elif self.cells[row][col] > 189 and self.cells[row][col] < 205:
                        rgb = [207, 249, 209]

                    elif self.cells[row][col] > 204 and self.cells[row][col] < 256:
                        rgb = [230, 239, 230]
                    #if no other parameters, default to color map
                    else:
                        rgb = [0, self.cells[row][col], 0]
                        r = 0
                        g = self.cells[row][col]
                        b = 0
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                        [0, 1, 2, 1, 2, 3],
                                        ('v2i', square_coords),
                                        ('c3B', (rgb[0], rgb[1], rgb[2], rgb[0], rgb[1], rgb[2], rgb[0], rgb[1], rgb[2], rgb[0], rgb[1], rgb[2])))
                                        #Remember, RGB values need to be assigned to EACH VERTICES
