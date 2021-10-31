# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:46:30 2021

@author: USER
"""

print ("@  @    @    @   @   @   @@@")
print ("@  @   @ @   @@  @   @   @  ")
print ("@@@@  @@@@@  @ @ @   @   @@ ")
print ("@  @ @     @ @   @   @   @  ")

print('=======HITUNGAN GAJI=======')
jam1=float(input('Jam masuk kantor: '))
gaji = 175000
if jam1 >=7.00:
    print('Selamat Pagi')
elif jam1 >=12.00:
    print('Selamat Siang')

jam2=float(input('Jam pulang kantor: '))
if jam2 >=15.00:
    print('Selamat Siang menuju Sore')

elif jam2 >=16.00:
    print('Selamat Sore')
elif jam2-jam1 == 8.00:
    gaji=gaji
elif jam2-jam1 >=8.59:
    x = int((jam2 -jam1)-8)
    gaji2=((x)*15000)
    y=int((jam2 - jam1) - 8.00)
x = int((jam2 -jam1)-8)
gaji2=((x)*15000)

    

    

print('=====Rincian Gaji Harian=====')
print(f'Total jam kerja : {int(jam2-jam1)} Jam')
print(f'Gaji harian     : Rp.{gaji}') 
print(f'Lembur          : Rp.{gaji2} ({x} Jam x Rp.15000)')
print(f'Total gaji      : Rp.{(gaji)+gaji2}')
if jam2-jam1<=8.00:
    print('Karena kamu tidak masuk, gaji kamu dipotong ya!')
print('=========TERIMA KASIH=========')