#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2016

Puzzle #1
"""

fname = '01_input.txt'

with open(fname) as f:
    contents = f.read()

# convert input text to list of directions
directions = contents.split(', ')
print(directions)