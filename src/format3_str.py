#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 14, 2014

@author: anroco

How to working the format method of a python str?

¿Como funciona el metodo format de un string en python?
'''

#
#review https://docs.python.org/3/library/string.html#formatstrings
#

#Using the comma as a thousands separator (numeric types)
s = '{:,}'.format(1049378473)
print(s)

#converting the value to different bases (only for integer)
s = 'int: {0:d}; hex: {0:x};  oct: {0:o};  bin: {0:b}'.format(62)
print(s)

#adds the prefix respective '0b', '0o', or '0x' to the output value.
s = 'hex: {0:#x};  oct: {0:#o};  bin: {0:#b}'.format(32)
print(s)

#Displays the number as a fixed-point number, with 4 decimal places
s = '{:.4f}'.format(24 / 53)
print(s)

#Displays the number as a percentage, with 2 decimal places
s = '{:.2%}'.format(24 / 53)
print(s)

#Displays the number in exponent notation, with 2 decimal places
s = '{:e}'.format(24 / 53)
print(s)
