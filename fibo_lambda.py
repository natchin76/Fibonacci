# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 00:38:24 2019

@author: CHINTAN
"""
x=lambda n:x(n-1)+x(n-2) if(n>2) else 1
print([x(i) for i in range(10)])