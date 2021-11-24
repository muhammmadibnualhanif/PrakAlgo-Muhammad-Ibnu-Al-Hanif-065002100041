#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 13:18:33 2021

@author: hanif
"""

import sys

def main():
    print("j : Jabodetabek\nd : Dalam Jawa\nl : Luar Jawab\nq : quit")
    hasil=input1("Tujuan = ")
    berat=input2("Berat barang = ")

def input1(n):
    while True:
        global a
        global harga_
        hasil=input(n)    
        if hasil == "j":
            a="Jabodetabek"
            harga_=10000
            break
        elif hasil == "d":
            a="Dalam Jawa"
            harga_=25000
            break
        elif hasil == "l":
            a="Luar Jawa"
            harga_=50000
            break
        elif hasil=="q":
            exit()
    return harga_

def input2(n):
    while True:
        global berat
        global harga1
        berat=int(input(n))
        if berat >0 and berat <= 20:
            harga1 = 15000
            break
        elif berat > 20:
            harga1 = 15000 +((berat-20)*1500)
            break
    return harga1

def Rincian():
    print("============== Rincian Biaya ==============")
    print(f'1.tujuan  = ({a}) Rp.{harga_}')
    print(f'2.Berat   = ({berat}kg)Rp.{harga1}')
    print(f'3.PPN 10% = Rp.{int((harga_+harga1)*(10/100))}')
    print(f'4.Total   = Rp.{int(harga_+harga1+(harga_+harga1)*(10/100))}')
    print("===========================================")

loop = True
while(loop):
    main()
    Rincian()