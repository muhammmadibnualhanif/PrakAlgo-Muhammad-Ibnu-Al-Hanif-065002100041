#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:06:03 2021

@author: hanif
"""

def menghitung_range():
    print("Program menghitung jumlah Range")
    n = input("Masukkan angka pertama: ")
    n = int (n)
    input2=int(input('masukkan angka kedua: '))
    sum = 0
    for i in range(n, input2+1, 1):
        sum = sum+i
    print("Jumlah Range adalah: ", sum )
menghitung_range()
