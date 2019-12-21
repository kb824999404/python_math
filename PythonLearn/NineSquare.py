def eva(A):
    row1=sum(A[:3]);row2=sum(A[3:6]);row3=sum(A[6:])
    srow=abs(row1-row2)+abs(row1-row3)+abs(row2-row3)
    col1=sum(A[::3]);col2=sum(A[1::3]);col3=sum(A[2::3])
    scol=abs(col1-col2)+abs(col1-col3)+abs(col2-col3)
    diag1=sum(A[0::4]);diag2=sum(A[6:0:-2])
    sdiag=abs(diag1-diag2)
    a_eva=srow+scol+sdiag
    return a_eva

B=list(range(1,10));b_eva=1000;i=0

import random as R

while i<100000:
    p1=R.randint(0,8)
    p2=R.randint(0,8)
    A=B[:]
    A[p1],A[p2]=A[p2],A[p1]     #随机交换两个数
    a_eva=eva(A)                #评估
    if(a_eva<b_eva):
        b_eva=a_eva
        B=A
        print(b_eva)
    if a_eva==0:
        break
    i+=1

print('i:{}'.format(i))

if b_eva==0:
    print('Find the result.')
    print('{}\t{}\t{}'.format(B[0],B[1],B[2]))
    print('{}\t{}\t{}'.format(B[3],B[4],B[5]))
    print('{}\t{}\t{}'.format(B[6],B[7],B[8]))
else:
    print('No result.')