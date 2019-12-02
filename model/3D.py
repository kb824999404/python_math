import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

def wing():
    n_angles=36
    n_radii=8
    radii=np.linspace(0.125,1.0,n_radii)
    angles=np.linspace(0,2*np.pi,n_angles,endpoint=False)
    angles=np.repeat(angles[...,np.newaxis],n_radii,axis=1)
    x=np.append(0,(radii*np.cos(angles)).flatten())
    y=np.append(0,(radii*np.sin(angles)).flatten())
    z=np.sin(-x * y)
    fig=plt.figure()
    ax=Axes3D(fig)
    ax.plot_trisurf(x,y,z,cmap=plt.cm.jet,linewidth=1)
    plt.show()

def test():
    fig=plt.figure()
    ax=Axes3D(fig)
    X=[0,1,2,1.5]
    Y=[0,4,4,1]
    Z=[0,2,0,2]
    ax.plot_trisurf(X,Y,Z)
    plt.show()

def surface():
    n=200
    x=np.linspace(-10.0,10.0,n)
    y=np.linspace(-10.0,10.0,n)
    s1=2*np.exp(-((x+1)/3)**2)
    s2=2*np.exp(-((y+2)/3)**2)   
    Z1=np.outer(s1,s2)
    w1=2*np.exp(-((x-2)/4)**2)
    w2=2*np.exp(-((y-1)/4)**2) 
    Z2=np.outer(w1,w2)
    X,Y=np.meshgrid(x,y)
    Z=100*(Z2-Z1)
    fig=plt.figure()
    ax=Axes3D(fig)
    ax.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    plt.show()   

def sca():
    fig=plt.figure()
    ax=Axes3D(fig)
    x_surf=np.arrange(0,1,0.01)
    y_surf=np.arrange(0,1,0.01)   

if __name__=='__main__':
    surface()
