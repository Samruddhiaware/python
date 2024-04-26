# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:29:59 2024

@author: LENOVO
"""

def area(shape):
    if shape == 'square':
        a = int(input('Enter side of square: '))
        return a*a
    elif shape == 'rectangle':
        a = int(input('Enter length of rectangle: '))
        b = int(input('Enter breadth of rectangle: '))
        return a*b
    elif shape == 'triangle':
        b = int(input('Enter breadth of triangle: '))
        h = int(input('Enter height of triangle: '))
        return 0.5*b*h