#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 21:02:49 2021

@author: hanif
"""

from math import *
def hitung_jarak_tempuh(kecepatah_awal, waktu, percepatan) :
    jarak_tempuh =(sqrt(v0+(1/2)*a*(t**2)))
    print("kecepatan awal = ",v0,"waktu = ",t,"dan percepatan : ",a,"hasil",jarak_tempuh)
    return jarak_tempuh

v0=int(input("kecepatan awal : "))
t=int(input("waktu : "))
a=int(input("percepatan :"))
hitung_jarak_tempuh(v0, t, a)