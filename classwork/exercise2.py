import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl

if __name__=='__main__':
    x=np.arange(-np.pi,np.pi,0.5)
    y=np.arange(-np.pi,np.pi,0.5)
    xs=np.sin(x)
    yc=np.cos(y)
    Z=np.outer(yc,xs)
    X,Y=np.meshgrid(x,y)

    mpl.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    #制作二维等高线图
    cs=plt.contour(X,Y,Z,10,colors='k')
    plt.clabel(cs,fontsize=10)
    plt.title('二维等高线图')
    plt.show()
    #制作三维等高线图
    fig=plt.figure()           
    ax=Axes3D(fig)
    cs=ax.contour(X,Y,Z,10,colors='k')
    plt.title('三维等高线图')
    plt.show()




