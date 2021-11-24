#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 13:10:00 2021

@author: hanif
"""

def Kali(a) :
	Hasil = 1
	for i in a :
		Hasil *= i
	print("Hasil kali value list :",Hasil)
	return Hasil

list = [1, 2, 3, 4, 5]
print("List :",list)
Kali(list)