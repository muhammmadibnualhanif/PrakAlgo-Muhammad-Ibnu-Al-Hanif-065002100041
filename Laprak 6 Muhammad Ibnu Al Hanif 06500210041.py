#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 18:54:04 2021

@author: rafi
"""

print ("@  @    @    @   @   @   @@@")
print ("@  @   @ @   @@  @   @   @  ")
print ("@@@@  @@@@@  @ @ @   @   @@ ")
print ("@  @ @     @ @   @   @   @  ")

loop=1
while loop ==1:
    def fungsiKubus (a):
        print("sisi=",a,"luas=",6*a)
        return 6*a
    def fungsiBalok(a,b,c):
        print('hasilnya adalah',(2*(a*b)) + (2*(a*c)) + (2*(b*c)))
        return (2*(a*b)) + (2*(a*c)) + (2*(b*c))
    def fungsiTabung(a,b):
        print('maka hasilnya adalalah',int(2*(pi*(a**2)))*(a+b))
        return float((2*(pi*(a**2)))*(a+b))
    def fungsiKerucut(a,b):
        print('maka hasilnya adalalah',pi*a*(a+b))
        return pi*a*(a+b)
    def fungsiBola(a):
        print('maka hasilnya adalalah',4*(pi*(a**2)))
        return 4*(pi*(a**2))
    print ("KALKULATOR MENCARI LUAS\n1.Kubus\n2.Balok\n3.Tabung\n4.Kerucut\n5.bola\n6.keluar")
    pilih=int(input('mau yang mana: '))
    if pilih ==1:
        no1=int(input('masukan sisi: '))
        fungsiKubus(no1)
    elif pilih ==2:
        no1=int(input('masukan panjang: '))
        no2=int(input('masukan lebar: '))
        no3=int(input('masukan tinggi'))
        fungsiBalok(no1,no2,no3)
    elif pilih ==3:
        no1=float(input('masukan jari jari: '))
        no2=float(input('masukan tinggi: '))
        float(fungsiTabung(no1,no2))
    elif pilih ==4:
        no1=float(input('masukan jari jari: '))
        no2=float(input('masukan garis (s): '))
        fungsiKerucut(no1,no2)
    elif pilih ==5:
        no1=float(input('masukkan jari jari:'))
        fungsiBola(no1)
    elif pilih ==6:
        break
    else:
        print("kamu salah, ulangi lagi")
        pilih=int(input('mau yang mana: '))