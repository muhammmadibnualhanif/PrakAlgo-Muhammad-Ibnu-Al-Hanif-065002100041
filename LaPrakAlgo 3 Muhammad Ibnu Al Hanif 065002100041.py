# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:49:52 2021

@author: USER
"""

print ("@  @    @    @   @   @   @@@")
print ("@  @   @ @   @@  @   @   @  ")
print ("@@@@  @@@@@  @ @ @   @   @@ ")
print ("@  @ @     @ @   @   @   @  ")

a = int (input("masukkan total harga belanja anda = "))
b = int (input("masukkan jumlah uang anda = "))
kembalian = (b-a)
print ("kembalian anda sejumlah = ", "Rp. ", kembalian)
uang_pecahan = [100000, 50000, 2000, 10000, 5000, 2000, 1000]
jumlah_pecahan = {}
sisa = kembalian
for pecahan in uang_pecahan:
    if sisa<pecahan:
        continue
    banyak_pecahan = int (sisa/pecahan)
    sisa = sisa-(pecahan*banyak_pecahan)
    print('uang kertas {} sebanyak {} lembar' .format (pecahan, banyak_pecahan))
