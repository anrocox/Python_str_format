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

#create a str using the format() method.
s = 'Today is {}, {}'.format('Jul 14', '2014')
print(s)

#defining the order of the arguments to be shown in the result.
s = '{2}, {0} and {1}'.format('first', 'second', 'third')
print(s)

#unpacking argument sequence
s = 'vowels are: {0}, {1}, {2}, {3} and {4}'.format(*'aeiou')
print(s)

#arguments can be repeated
s = '{0}, {1}, {0}, {1}.'.format('red lorry', 'yellow lorry')
print(s)

#create a str using the format() method with key-value format.
s = 'Tom eats {food} in {site}'.format(food='hamburger', site='McDonalds')
print(s)

#create a dict
d = {'dog': 'Buz', 'cat': 'Darco'}

#unpacking argument sequence
s = 'My pets are {dog} and {cat}'.format(**d)
print(s)

#combining the types of arguments
s = '{name} gets in spanish {0} and {1} in social '.format(4, 5, name='Clark')
print(s)
