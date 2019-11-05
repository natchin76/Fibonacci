# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:54:31 2019
Assignment 1 Prob 3
Fibonacci sequence
@author: CHINTAN
"""
s=[1,1]
for i in range(2,10):
    s.append(s[i-1]+s[i-2])
print(s)    
    

