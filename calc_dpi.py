#!/usr/bin/env python
# -*- coding=utf-8; -*-

"""
Calculate monitor DPI.
"""

from math import sqrt

def dpi(x, y, diag):
  return sqrt(x*x + y*y) / diag 

hor_res = input('Horizontal resolution: ')
vert_res = input('Vertical resolution: ')
diag = input('Diagonal size: ')

result = dpi(hor_res, vert_res, diag)
print 'DPI: {0}'.format(result)