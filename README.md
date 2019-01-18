# UPDATE 0.02:
- Added keyboard input
- Added arrow key navigation along the grid
- Added a "re-seed" button with ```space bar```
- Added a heightmap mode with the ```H``` key
# Perlin-Noise-Landmass-Generator
I didn't see any landmass generation tools on Github for python, so I learned a little bit about perlin noise and implemented it into a rudimentary terrain generator. Mostly for educational purposes to teach myself how to use the noise and pyglet libraries, but In the near future I would like to expand its features and usability, a couple potential feature expansions are listed below.

the script generates a grid of variable size, and applies the perlin noise algorithm to every cell on the grid one at a time, assigning it an 8-bit integer that, when viewed alongside the rest of the grid, creates smooth, pseudorandom noise, which the code then uses as a heightmap of sorts. In the final step, the code sections off different depths on the heightmap and associates them with static colors(blue for sea, green for basic land, white for mountains, etc), before passing those values off to OpenGL to draw to the screen.

![alt text](https://files.catbox.moe/dyp0j4.png)

# Requirements
This generator at this time only requires two non-default libraries, ```pyglet``` and ```noise```, both of which can easily be installed using pip:

```pip install pyglet``` or ```pip3 install pyglet``` depending on your setup and pip version.

# Use 
Use the arrow keys to scroll the map in any direction, and use the ```space bar``` to "regen" the map(move you to a random XY coordinate).

Press the ```H``` key to change to heightmap mode! While not particularly useful or fun to look at, it does help you understand how perlin noise works by unrevealing the raw output underneath the terrain color function.

The nature of the algorithm can be edited in both files, particularly the window size, the scale of the pixels(```Terrain.scale```, set to 5 by default), and the octaves the noise is generated with. 

# Known Issues / Future Plans

I am still really interested in this project and hope to continue working on it over the next few weeks or months. Here are some issues or missig features I need to implement:

- ~~Perhaps most obviously, the program needs to be killed and started again to generate another map. A simple keyboard input command should fix this.~~ FIXED: V 0.02
- A proper user interface needs to be added to make the configuration of the algorithm easier. Either a GUI within the window itself, or even a terminal-based UI.
- The option to export the heightmap as either a greyscale image or an array file for future use would be far more useful and should be added.
- ~~A button to toggle the "landscape mode" and the "heightmap mode" would be neat, wouldn't it?~~ FIXED: V 0.02
- Parts of the code could use some prettying up, as well as additional documentation.
- Ideally, the generator should default to changing the values of the edges of the grid to water, so landmasses aren't cut off halfway.
- As is, the program is incredibly inefficient when it comes to processing, but it's also written in Python, so saying this is an "issue" is kind of irrelevant to the point of the program. That being said, there's a TON of room for optimization in the code, so improved speeds when re-seeding and scrolling the view are definitely possible to implement in the future.
