# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:29:43 2021

@author: USER
"""

while True:
    print('LIST PROGRAM')
    print('1.Input Data')
    print('2.View Data')
    print('3.Average of Scores')
    
    input_1=int(input('Input Menu: '))
    if input_1==1:
        names = []
        scores = []
        for _ in range(3):
            names.append(input('Input Students Name: '))
            scores.append([])
            for _ in range(3):
                scores[-1].append(int(input('Input Students Score: ')))
            
            
    if input_1==2:
        print('NAMA | PRACTICE 1 |  PRACTICE 2 | PRACTICE 3 |')
        print(f'{names[0]}','  ', scores[0])
        print(f'{names[1]}','  ', scores[1])
        print(f'{names[2]}','  ', scores[2])
    if input_1==3:
        print((names[0]),'=',sum(scores[0])/len(scores[0]))
        print((names[1]),'=',sum(scores[1])/len(scores[1]))
        print((names[2]),'=',sum(scores[2])/len(scores[2]))