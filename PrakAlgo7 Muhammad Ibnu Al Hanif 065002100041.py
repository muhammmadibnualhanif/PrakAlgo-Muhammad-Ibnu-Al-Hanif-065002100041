#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 09:04:09 2021

@author: hanif
"""

print ("@  @    @    @   @   @   @@@")
print ("@  @   @ @   @@  @   @   @  ")
print ("@@@@  @@@@@  @ @ @   @   @@ ")
print ("@  @ @     @ @   @   @   @  ")

def hanif (a):
    hanif =1
    
    for i in range(1,a + 1):
        hanif = hanif*i
    print("Faktor dari",a,"adalah",hanif)
num = int(input("Nilai: "))
hanif(num)
