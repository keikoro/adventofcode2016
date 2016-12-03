#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016

Puzzle #3, part 1
"""


def find_triangle(sides):
    """
    Compare three values to see if they could form a triangle.

    In a triangle, the length of any two sides combined must be
    greater than* the length of the remaining side.

    *(actually, ≥ greater than or equal...)

    :return: False if any value is greater than or equal the sum
             of the other two values, otherwise True.
    """
    result = True
    for s in sides:
        # print(s)  # current list item
        remaining = sides[:]
        remaining.remove(s)
        if s >= sum(remaining):
            result = False  # stop trying with this array
            break
    return result

fname = '03_input.txt'
triangles_cnt = 0

with open(fname) as f:
    for line in f:
        values = line.split()  # NB! input values are strings!
        values = [int(x) for x in values]
        if find_triangle(values):
            triangles_cnt += 1

# number of triangles
print('No. of triangles: {}'.format(triangles_cnt))
