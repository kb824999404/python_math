import math
import random

x1=x=0
while True:
    flag=random.randint(0,1)
    step=random.uniform(0,math.pi)
    if(flag):
        x1=x+step
    else:
        x1=x-step
    if(not 0<x1<math.pi):
        continue
    if(math.sin(x1)>math.sin(x)):
        if(abs(math.sin(x1)-math.sin(x))<1e-10):
            x=x1
            break
        x=x1

print('x:{},sin(x):{}'.format(x,math.sin(x)))
print('pi/2:{}'.format(math.pi/2))
print('diff:{}'.format(abs(x-math.pi/2)))