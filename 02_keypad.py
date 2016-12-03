#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016

Puzzle #2, part 1
"""

fname = '02_input.txt'
lines = []

keycodes = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
horizontal = {'L': -1, 'R': 1}
vertical = {'U': -1, 'D': 1}

x = 1  # rows
y = 1  # columns

result = []

with open(fname) as fn:
    for line in fn:
        lines.append(line)

for line in lines:
    for l in line:
        if l in horizontal:
            if not (x + (horizontal[l]) > 2 or x + (horizontal[l]) < 0):
                x += horizontal[l]
        if l in vertical:
            if not (y + (vertical[l]) > 2 or y + (vertical[l]) < 0):
                y += vertical[l]
    result.append(keycodes[y][x])

print('key combination: {}'.format(''.join(str(r) for r in result)))
