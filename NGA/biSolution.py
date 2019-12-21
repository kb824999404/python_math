import numpy as np
from module.NGA import NGA


def  fun(x):  #y=x3+ 10-4.56 * x 2 - (10^-4.56 * 0.01 + 10^-14) * x – 10^-4.56 * 10^-14
    ka = 10**(-4.56)
    y = x**3+ka*x**2-(ka*0.01+1e-14)*x-ka*1e-14
    return y

def f1(x):
    ka = 10**(-4.56)
    y = x**3+ka*x**2-(ka*0.01+1e-14)*x-ka*1e-14
    y=abs(x)
    return y    

def solve(f):       #求解高次方程的根
    while True:
        a=float(input("a="))
        b=float(input("b="))
        fa = f(a)
        fb = f(b)
        if( fa* fb <0):
            break

    while abs(a-b)/b>1e-8:
        m = (a+b) /2.0
        fm = f(m)
        if fm*fa >0:
            a=m
        else:
            b=m
    print("The answer is:",a)
    print(f(a))

def NGASolve():
    nga=NGA(10,1,50,90,500,f1)
    nga.solve()
    print(nga.getAnswer())
    print(fun(nga.getAnswer()))


if __name__=='__main__':
    solve(fun)
    NGASolve()