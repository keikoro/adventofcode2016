#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016

Puzzle #1, part 2
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

# all_coordinates = OrderedDict()
all_coordinates = []

for elem in directions:
    walking_dir = elem[0].lower()
    next_c = move[walking_dir]

    # account for compass array only being 4 elements long
    cp = (cp + next_c) % 4
    axis, direction = compass[cp]

    move_for = int(elem[1:]) * direction

    if axis == 'x':
        i = x
        while i != (x + move_for):
            all_coordinates.append((i, y))
            if cp == 1:
                i += 1
            else:
                i -= 1
        x += move_for
    if axis == 'y':
        k = y
        while k != (y + move_for):
            all_coordinates.append((x, k))
            if cp == 0:
                k += 1
            else:
                k -= 1
        y += move_for

# debug
# print(all_coordinates)

coords_collected = {}
for c in all_coordinates:
    if c in coords_collected:
        # print first pair of coordinates traversed more than once
        break
    else:
        coords_collected[c] = 1

x = c[0]
y = c[1]
print('final coordinates: x: {}, y: {}'.format(x, y))
print('blocks: {}'.format(abs(x) + abs(y)))
