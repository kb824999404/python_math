def nup():
    import numpy as np
    print(np.arange(0,1,0.1))
    print(np.linspace(1,10,20))
    x=np.arange(0,np.pi/2,0.1)
    y=np.sin(x)
    print(y)

def fp():
    import matplotlib.pyplot as plt
    import numpy as np
    x=np.arange(-np.pi,np.pi,0.1)
    y=np.sin(x)
    plt.plot(x,y,'b')
    plt.show()

def xy():
    import numpy as np
    x=np.arange(-5,5,0.1)
    y=x**2
    import matplotlib.pyplot as plt
    plt.xlim(-5,5)
    plt.ylim(0,100)
    plt.xlabel("x")
    plt.ylabel("y=x*x")
    plt.title("Plot y=x*x")
    plt.grid(True)
    plt.plot(x,y)
    plt.show()

from pylab import *

def pic():
    import numpy as np
    x=np.linspace(-np.pi,np.pi,100)
    sin,cos=np.sin(x),np.cos(x)
    plot(x,sin,color='blue',linewidth=2.0,linestyle=':')
    plot(x,cos,color='red',linewidth=2.0,linestyle='-.')
    show()

def tick():
    import numpy as np
    x=np.linspace(-np.pi,np.pi,100)
    cos=np.cos(x)
    xticks(np.linspace(-np.pi,np.pi,5))
    plot(x,cos,color='red',linewidth=2.0,linestyle='-')
    show()

def leg():
    import numpy as np
    x=np.linspace(-np.pi,np.pi,100)
    sin,cos=np.sin(x),np.cos(x)
    plot(x,sin,color='blue',linewidth=2.0,linestyle='-',label='sin')
    plot(x,cos,color='red',linewidth=2.0,linestyle='-',label='cos')
    legend(loc='upper left')
    show()

def flag():
    import numpy as np
    x=np.linspace(-np.pi,np.pi,100)
    sin,cos=np.sin(x),np.cos(x)
    plot(x,sin,color="blue",linewidth=2.0,linestyle="-.")
    plot(x,cos,color="red",linewidth=2.0,linestyle="--")
    t=2*np.pi/3
    plot([t,t],[0,np.sin(t)],color="red",linewidth=2.5,linestyle="-.")
    scatter([t,],[np.sin(t),],50,color="red")
    annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',xy=(t,np.sin(t)),xycoords="data",xytext=(+10,+30),
    textcoords="offset points",fontsize=16,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
    show()

def sca():
    import numpy as np
    n=10
    x=np.linspace(-10,10,n)
    y=np.random.normal(0,1,n)
    scatter(x,y)
    show()

def ransca():
    import numpy as np
    import matplotlib.pyplot as plot
    N=30
    x=np.random.rand(N)
    y=np.random.rand(N)
    area=np.pi*(15*np.random.rand(N))**2
    color=2*np.pi*np.random.rand(N)
    plt.scatter(x,y,s=area,c=color,alpha=0.5,cmap=plt.cm.hsv)
    plt.show()    

def cake():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    mpl.rcParams['font.family']='sans-serif'
    mpl.rcParams['font.sans-serif']=[u'SimHei']
    data=np.random.randint(1,11,5)
    plt.pie(data,explode=[0,0,0.3,0,0])
    plt.show()

def bar():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.rcParams['font.sans-serif']=['SimHei']
    rect=plt.bar(x=(0,1),height=(173,69),width=0.2,align='center')
    plt.ylabel('人数')
    plt.xlabel('课程')
    plt.xticks((0,1),("C","Python"))
    plt.show()

def test():
    names=['张仟', '石戎',  '万行']
    enu=enumerate(names)
    print(enu)
    print(list(enu))

def people():
    import numpy as np
    import matplotlib.pyplot as plt
    N=5
    menMens=(20,35,45,50,38)
    menStd=(2,3,4,1,2)
    ind=np.arange(N)
    width=0.35
    fig,ax=plt.subplots()
    rects1=ax.bar(ind,menMens,width,color='b',yerr=menStd)
    womenMeans=(25,32,34,20,25)
    womenStd=(3,5,2,3,3)
    rects2=ax.bar(ind+width,womenMeans,width,color='g',yerr=womenStd)
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(('G1','G2','G3','G4','G5'))
    ax.legend((rects1[0],rects2[0]),('Men','Women'))
    def autolabel(rects):
        for rect in rects:
            height=rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2.,1.05*height,'%d'%int(height),ha='center',va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    plt.show()


def fab(num):
    ans=[0,1]
    for i in range(num):
        ans.append(ans[-1]+ans[-2])
    print(ans)

def ext():
    x=[1,2,3,4,5]
    y=[7,8,9,10]
    x.extend(y)
    print(x)
    print(y)

def line():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    mpl.rcParams['font.family']='sans-serif'
    mpl.rcParams['font.sans-serif']=[u'SimHei']
    data=np.random.randint(1,10,10)
    x=np.arange(len(data))
    plt.plot(x,data,color='b')
    plt.bar(x,data,alpha=.5,color='g',width=0.2)
    plt.show()


def sub():
    import numpy as np
    import matplotlib.pyplot as plt
    x=np.linspace(0,5,10)
    y=x**2
    plt.subplot(2,2,1)
    plt.plot(x,y,'r--')
    plt.subplot(2,2,4)
    plt.plot(x,y,'g*-')
    plt.show()
    
def subs():
    import numpy as np
    import matplotlib.pyplot as plt
    x=np.linspace(0,5,10)
    y=x**2
    fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(8,6),dpi=100)
    for axs in axes:
        for ax in axs:
            ax.plot(x,y,'r')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title('title')
    plt.show()    


if __name__=='__main__':
    subs()
    nup()
    fp()
    xy()
    pic()
    tick()
    leg()
    flag()
    sca()
    ransca()
    cake()
    bar()
    test()
    people()
    ext()
    line()
    sub()  