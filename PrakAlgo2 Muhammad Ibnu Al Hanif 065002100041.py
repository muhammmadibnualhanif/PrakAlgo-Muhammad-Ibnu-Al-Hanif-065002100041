# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:25:37 2021

@author: USER
"""

a = ("@  @    @    @   @   @   @@@")
b = ("@  @   @ @   @@  @   @   @  ")
c = ("@@@@  @@@@@  @ @ @   @   @@ ")
d = ("@  @ @     @ @   @   @   @  ")
print (a)
print (b)
print (c)
print (d)

#kalkulator pytagoras
from math import sqrt
cara = input ('sisi mana yang dihitung = ')

if cara == 'c' :
    a = int (input('masukkan panjang a = '))
    b = int (input('masukkan panjang b = '))
    
    c = sqrt (a * a + b * b )
    print ('panjang c adalah', c)