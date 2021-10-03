# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:34:16 2021

@author: USER
"""


a = int(input('Masukkan nilai a: '))
b = int(input('Masukkan nilai b: '))
c = int(input('Masukkan nilai c: '))

if a > b and a > c:
  print('A yang terbesar')
elif b > a and b > c:
  print('B yang terbesar')
else:
  print('C yang terbesar')