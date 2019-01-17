# Perlin-Noise-Landmass-Generator
I didn't see any landmass generation tools on Github for python, so I learned a little bit about perlin noise and implemented it into a rudimentary terrain generator. Mostly for educational purposes to teach myself how to use the noise and pyglet libraries, but In the near future I would like to expand its features and usability, a couple potential feature expansions are listed below.

the script generates a grid of variable size, and applies the perlin noise algorithm to every cell on the grid one at a time, assigning it an 8-bit integer that, when viewed alongside the rest of the grid, creates smooth, pseudorandom noise, which the code then uses as a heightmap of sorts. In the final step, the code sections off different depths on the heightmap and associates them with static colors(blue for sea, green for basic land, white for mountains, etc), before passing those values off to OpenGL to draw to the screen.

# Requirements
This generator at this time only requires two non-default libraries, ```pyglet``` and ```noise```, both of which can easily be installed using pip:

```pip install pyglet``` or ```pip3 install pyglet``` depending on your setup and pip version.

# Use 
At the moment, all you can do it load the script from ```main.py``` and look at the pretty world it generates. The nature of the algorithm can be edited in both files, particularly the window size, the scale of the pixels(```Terrain.scale```, set to 5 by default), and the octaves the noise is generated with. If you want to generate another map, you need to relaunch the program, exclusively because I'm not smart enough to have figured out how to make Pyglet accept keyboard input.

# Known Issues / Future Plans

I am still really interested in this project and hope to continue working on it over the next few weeks or months. Here are some issues or missig features I need to implement:

- Perhaps most obviously, the program needs to be killed and started again to generate another map. A simple jeyboard input command should fix this.
- A proper user interface needs to be added to make the configuration of the algorithm easier. Either a GUI within the window itself, or even a terminal-based UI.
- The option to export the heightmap as either a greyscale image or an array file for future use would be far more useful and should be added.
- A button to toggle the "landscape mode" and the "heightmap mode" would be neat, wouldn't it?
- Parts of the code could use some prettying up, as well as additional documentation.
