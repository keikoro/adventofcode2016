#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016

Puzzle #2, part 2
"""

fname = '02_input.txt'
lines = []

keycodes = [(None, None, 1, None, None),
            (None, 2, 3, 4, None),
            (5, 6, 7, 8, 9),
            (None, 'A', 'B', 'C', None),
            (None, None, 'D', None, None)]
horizontal = {'L': -1, 'R': 1}
vertical = {'U': -1, 'D': 1}

a = 2  # rows
b = 0  # columns

result = []

with open(fname) as fn:
    for line in fn:
        lines.append(line)

for line in lines:
    for l in line:
        if l in horizontal:
            if (0 <= b + horizontal[l] <= 4 and
                keycodes[a][b + horizontal[l]] is not None):
                b += horizontal[l]
        if l in vertical:
            if (0 <= a + vertical[l] <= 4 and
                keycodes[a + vertical[l]][b] is not None):
                a += vertical[l]
    result.append(keycodes[a][b])

print('key combination: {}'.format(''.join(str(r) for r in result)))
