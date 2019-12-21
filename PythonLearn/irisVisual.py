from sklearn import datasets
iris=datasets.load_iris() # 从数据库获得数据
data=iris.data #获得自变量数据
target=iris.target  # 获得样本的分类信息
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']
cls1=target==0;cls2=target==1;cls3=target==2
plt.plot(data[cls1,2],data[cls1,3],'b^',label='山鸢尾')
plt.plot(data[cls2,2],data[cls2,3],'r*',label='变色鸢尾')
plt.plot(data[cls3,2],data[cls3,3],'go',label='维吉尼亚鸢尾')
plt.legend(loc='upper left')
plt.show()
