"""
Created on Tue Nov  5 22:27:40 2019
Fibonacci sequence function file
@author: CHINTAN
"""
def fibo(n):
    if n==1:
        return([1])
    elif n==2:
        return([1,1])
    else:
        s=[1,1]
        for i in range(2,n):
            s.append(s[i-1]+s[i-2])
        return(s)
 
