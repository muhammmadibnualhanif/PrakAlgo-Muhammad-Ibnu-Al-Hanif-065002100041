#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:04:59 2021

@author: hanif
"""

print('Tuple 1: ')
a=('1000','1100', '1200', '1300', '1400', '1500', '1600', '1700', '1800', '1900', '2000')
b = ", ".join(a[0:3])
c = ", ".join(a[4:7])
d= ", ".join(a[8:11])
print((b,c,d))
print('Rata-rata dari Tuple adalah: ')
print ([sum(map(float, filter(None, a[0:3])))/(len(a)-1),(sum(map(float, filter(None, a[4:7])))/(len(a)-1)),(sum(map(float, filter(None, a[8:11])))/(len(a)-1))])  
print('===== Muhammad Ibnu Al Hanif =====')
print('===== 065002100041 =====')