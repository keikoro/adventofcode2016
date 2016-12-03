#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2016

Puzzle #3, part 2
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


def shift_lists(collection, split_by):
    """
    Create new lists from existing lists.

    Shift values of existing lists in such a way that
    - the first values of them all form a new list,
    - the second values of them all form another new list
    etc.

    :return: a list containing sub lists with 'split_by' elements each
    """
    collection_copy = collection[:]
    no = split_by
    new_collection = []

    # count how often to iterate over the supplied list
    # round down to prevent iteration over non-existent 'rows'/sub lists
    count = int(len(collection_copy)/no)

    for c in range(0, count):
        # start each iteration at a new sublist
        # -> split_by rows 'down' from the previous list
        # NB! iteration starts at 0, start/stop calc needs to start at 1!
        start = (c+1)*no-no
        stop = (c+1)*no
        generator = (collection_copy[x] for x in range(start, stop))
        shift = zip(*generator)

        # convert zip object to list of lists;
        # NB list(shift) alone would result in a list of tuples
        shift = [list(x) for x in list(shift)]

        # add lists together instead of appending to 'merge' lists;
        # NB appending would result in lists withing lists
        new_collection += shift

    return new_collection

fname = '03_input.txt'
triangles_cnt = 0
sides_cnt = 3

converted_lines = []

with open(fname) as f:
    for line in f:
        values = line.split()  # NB! input values are strings!
        values = [int(x) for x in values]
        converted_lines.append(values)

shifted = shift_lists(converted_lines, sides_cnt)
# debug
# print(shifted[0:6])
# print(len(shifted))

for l in shifted:
    # debug
    # print(l)
    if find_triangle(l):
        triangles_cnt += 1

# number of triangles
print('No. of triangles: {}'.format(triangles_cnt))
