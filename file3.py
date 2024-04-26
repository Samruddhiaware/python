# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:24:12 2024

@author: LENOVO
"""

user_req= input('What do you want to do today? ')

if (user_req == 'Calculate area'):
    import file1
    k = input('Specify shape of which area is required: ')
    print(file1.area(k))
    
if (user_req == 'Conversion'):
    import file2
    m = input('Specify which conversion you want to do: ')
    print(file2.convert(m))






