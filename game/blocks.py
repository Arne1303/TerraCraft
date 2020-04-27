#!/bin/python3

"""
 ________                                        ______                       ______     __
|        \                                      /      \                     /      \   |  \ 
 \$$$$$$$$______    ______    ______   ______  |  $$$$$$\  ______   ______  |  $$$$$$\ _| $$_
   | $$  /      \  /      \  /      \ |      \ | $$   \$$ /      \ |      \ | $$_  \$$|   $$ \ 
   | $$ |  $$$$$$\|  $$$$$$\|  $$$$$$\ \$$$$$$\| $$      |  $$$$$$\ \$$$$$$\| $$ \     \$$$$$$
   | $$ | $$    $$| $$   \$$| $$   \$$/      $$| $$   __ | $$   \$$/      $$| $$$$      | $$ __
   | $$ | $$$$$$$$| $$      | $$     |  $$$$$$$| $$__/  \| $$     |  $$$$$$$| $$        | $$|  \ 
   | $$  \$$     \| $$      | $$      \$$    $$ \$$    $$| $$      \$$    $$| $$         \$$  $$
    \$$   \$$$$$$$ \$$       \$$       \$$$$$$$  \$$$$$$  \$$       \$$$$$$$ \$$          \$$$$


Copyright (C) 2013 Michael Fogleman
Copyright (C) 2018/2019 Stefano Peris <xenonlab.develop@gmail.com>

Github repository: <https://github.com/XenonLab-Studio/TerraCraft>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


def _tex_coord(x, y, n=8):
    """ Return the bounding vertices of the texture square.

    """
    m = 1.0 / n
    dx = x * m
    dy = y * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m


def _tex_coords(top, bottom, side):
    """ Return a list of the texture squares for the top, bottom and side.

    """
    top = _tex_coord(*top)
    bottom = _tex_coord(*bottom)
    side = _tex_coord(*side)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)
    return result


class Block:
    __slots__ = ('name', 'tex_coords')

    def __init__(self, name, tex_coords):
        """A class for Blocks

        :param name: The name of the Block material.
        :param tex_coords: The texture coordinates for this material.
        """
        self.name = name
        self.numeric_tex_coords = tex_coords
        self.tex_coords = _tex_coords(*tex_coords)

    def get_block_image(self):
        block_image = pyglet.resource.image('textures.png')
        block_image = block_image.get_region(
            self.numeric_tex_coords[2][0]*16,self.numeric_tex_coords[2][1]*16, 16, 16)
        return block_image


DIRT = Block('dirt', ((0, 1), (0, 1), (0, 1)))
DIRT_WITH_GRASS = Block('dirt_with_grass', ((1, 0), (0, 1), (0, 0)))
SAND = Block('sand', ((1, 1), (1, 1), (1, 1)))
COBBLESTONE = Block('cobblestone', ((2, 0), (2, 0), (2, 0)))
BRICK_COBBLESTONE = Block('brick_cobblestone', ((3, 0), (3, 0), (3, 0)))
BRICK = Block('brick', ((3, 1), (3, 1), (3, 1)))
BEDSTONE = Block('bedstone', ((2, 1), (2, 1), (2, 1)))
TREE = Block('tree', ((1, 2), (1, 2), (0, 2)))
LEAVES = Block('leaves', ((2, 2), (2, 2), (2, 2)))
SNOW = Block('snow', ((1, 3), (0, 1), (0, 3)))
WOODEN_PLANKS = Block('wooden_planks', ((2, 3), (2, 3), (2, 3)))
SMOOTH_BRICK = Block('smooth_brick', ((2, 4), (2, 4), (1, 4)))
SMOOTH_STACK = Block('smooth_stack', ((2, 4), (2, 4), (0, 4)))

# A reference to the 6 faces (sides) of the blocks:
FACES = [(0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0), (0, 0, 1), (0, 0, -1)]
