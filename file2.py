# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:33:34 2024

@author: LENOVO
"""

def convert(m):
    if m == 'cm to m':
        k = int(input('Enter the value in cm: '))
        return ('Value in m is: ', k/100)
    elif m == 'inch to cm':
        k = float(input('Enter the value in inches: '))
        return k*2.54
    elif m == 'F to C':
        k = float(input('Enter the temperature in Farenheit: '))
        return ('Temperature in Celsius is, ',(k-32)*(5/9))