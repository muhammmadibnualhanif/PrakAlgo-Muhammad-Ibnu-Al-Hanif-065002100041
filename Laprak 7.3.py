#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 23:36:09 2021

@author: hanif
"""

print ("@  @    @    @   @   @   @@@")
print ("@  @   @ @   @@  @   @   @  ")
print ("@@@@  @@@@@  @ @ @   @   @@ ")
print ("@  @ @     @ @   @   @   @  ")

def main(n):
    if n %3==0:
        n**3 
        print ("Hasilnya adalah",n**3)
    else:
        cek(num)
def cek(n):
    if n %3!=0:
        print ("False")
num=int(input("Masukkan nilai: "))
main(num)