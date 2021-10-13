# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:50:21 2021

@author: USER
"""

import sys
a = 0
while a == 0:
    print ("==Program Pengkonversian Bilangan==")
    print ("1. Bilangan Desimal ke Bilangan Biner")
    print ("2. Bilangan Biner ke Bilangan Desimal")
    print ("3. Keluar")
    a1 = int(input("Silahkan Pilih: "))
    if a1==1:
        decimal = int(input("Masukkan decimal: "))
        if decimal ==0:
            print (0)
        else:
            print ("Hasil bagi sisa biner:")
            bitstring=" "
        while decimal > 0:
                Sisa = decimal %2
                decimal = decimal//2
                bitstring = str (Sisa) + bitstring
                print ("Binernya adalah: ", bitstring)
                
    elif a1==2:
            bit = input ("Masukkan str Biner: ")
            decimal = 0
            Jawab = len(bit)-1
            for digit in bit:
                decimal += int (digit)*2**Jawab
                Jawab -= 1
                print ("Nilai Decimal adalah: ", decimal)
    elif a1==3:
            sys.exit (0)
            