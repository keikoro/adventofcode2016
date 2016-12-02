#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016

Puzzle #1, part 1
"""

fname = '01_input.txt'

with open(fname) as f:
    contents = f.read()

# convert input text to list of directions
directions = contents.split(', ')

# initial coordinates
x = 0
y = 0

# corresponds to N, E, S, W and how moving in a direction affects the axes
compass = [('y', 1), ('x', 1), ('y', -1), ('x', -1)]

# ['N', 'E', 'S', 'W']
# initial cardinal point is North -> 0
cp = 0

# walking direction corresponds to moving left/right within compass array
move = {'l': -1, 'r': 1}

for elem in directions:
    walking_dir = elem[0].lower()
    next_c = move[walking_dir]

    # account for compass array only being 4 elements long
    cp = (cp + next_c) % 4
    axis, direction = compass[cp]

    if axis == 'x':
        x += (int(elem[1:]) * direction)
    if axis == 'y':
        y += (int(elem[1:]) * direction)

print('final coordinates: x: {}, y: {}'.format(x, y))
print('blocks: {}'.format(abs(x) + abs(y)))
