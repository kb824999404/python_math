from scipy.optimize import fsolve
import numpy as np
from module.NGA import NGA


def f(x):
    x0, x1,x2 = x 
    return [2*x1+3, 4*x0*x0 + np.sin(x1*x2), x1*x2/2 - 3]



def solveByFsolve():            #用fsolve解线性方程组
    ans=fsolve(f,[1.0,1.0,1.0])
    print(ans)
    print(f(ans))


def f3(v):
    sum = np.fabs(2*v[1]+3) +np.fabs(4*v[0]*v[0]+np.sin(v[1]*v[2])) +np.fabs(v[1]*v[2]/2-3)
    return sum

def solveByNGA():           #用NGA解线性方程组
    nga=NGA(10,3,0,90,10000,f3)
    nga.solve()
    ans=nga.getAnswer()
    print(ans)
    print(f3(ans))

if __name__=='__main__':
    # solveByNGA()
    solveByFsolve()