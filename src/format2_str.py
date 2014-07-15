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
#create a tuple with coordinates data
t = (4.598889, -74.080833)

#access an item of an iterable object, {name[index_item]}
#to access object's attribute, {name.attribute_name}
s = 'latitude: {0[0]}, longitude: {0[1]}'.format(t)
print(s)

#the field be left-aligned within the available space
s = '{:<50}'.format('left aligned text')
print(s)

#the field be right-aligned within the available space
s = '{:>50}'.format('right aligned text')
print(s)

#the field be centered within the available space.
s = '{:^50}'.format('centered text')
print(s)

#the field be centered within the available space, use '-' as a fill char.
s = '{:-^50}'.format('centered text')
print(s)

#sign should be used for both positive as well as negative numbers.
s = '{:+f}; {:+f}'.format(3.1416, -3.1416)
print(s)

#sign should be used only for negative numbers (default)
s = '{:-f}; {:-f}'.format(3.1416, -3.1416)
print(s)
