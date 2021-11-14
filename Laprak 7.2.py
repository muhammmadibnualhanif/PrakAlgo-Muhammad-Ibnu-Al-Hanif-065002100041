#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 23:29:59 2021

@author: hanif
"""

print ("@  @    @    @   @   @   @@@")
print ("@  @   @ @   @@  @   @   @  ")
print ("@@@@  @@@@@  @ @ @   @   @@ ")
print ("@  @ @     @ @   @   @   @  ")

string = list(map(str, input("Masukkan sesuatu: ").lower()))

def vokal_kon(n):
  konsonan=0
  vokal=0
  for i in range(0, len(string)):
    if string[i]=='a' or string[i]=='i' or string[i]=='u' or string[i]=='e' or string[i]=='o':
      vokal+=1
    else:
      konsonan+=1
  print("Jumlah huruf vokal: ",vokal)
  print("Jumlah huruf konsonan:",konsonan)
vokal_kon(string)