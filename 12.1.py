# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 22:23:11 2021

@author: USER
"""

list=[]
minta=int(input('berapa rangenya? '))
for i in range(minta):
    i+=1
    list.append(int(input(f'masukan angka ke {i}:')))
print(sorted(list))