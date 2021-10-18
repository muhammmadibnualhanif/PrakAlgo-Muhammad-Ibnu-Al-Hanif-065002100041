#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 22:45:47 2021

@author: hanif
"""

print ("@  @    @    @   @   @   @@@")
print ("@  @   @ @   @@  @   @   @  ")
print ("@@@@  @@@@@  @ @ @   @   @@ ")
print ("@  @ @     @ @   @   @   @  ")

hanif=0
while hanif==0:
    a=input('masukan list angka: ')
    genap=[]
    ganjil=[]
    for a in a.split():

        if int(a)%2==0:
                print('terdapat bilangan genap')
                break
        if int(a)%2==1:
            
            genap.append(int(a))
            print('terdapat bilangan genap')
            break

        else:
            print('tidak terdapat bilangan genap')
