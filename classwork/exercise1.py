import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

if __name__=='__main__':
    x=np.arange(-np.pi,np.pi,0.5)
    y=np.arange(-np.pi,np.pi,0.5)
    xs=np.sin(x)
    yc=np.cos(y)
    Z=np.outer(yc,xs)
    X,Y=np.meshgrid(x,y)
    fig=plt.figure()
    ax=Axes3D(fig)
    ax.plot_surface(X,Y,Z)
    ax.set_xlabel('x=sin')
    ax.set_ylabel('y=cos')
    ax.set_zlabel('z')
    plt.show()

