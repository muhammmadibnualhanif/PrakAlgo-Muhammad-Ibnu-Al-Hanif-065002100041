#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 08:32:50 2021

@author: hanif
"""

def index_ganjil(karakter):
    isian = [karakter[i] for i in range(len(karakter)) if i%2==1]
    print('Karakter indeks ganjil: ',''.join(isian))
    return(isian)

bacavalidinput=input('Masukkan suatu kata: ')
index_ganjil(bacavalidinput)