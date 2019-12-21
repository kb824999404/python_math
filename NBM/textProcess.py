import numpy as np
import jieba
from collections import Counter
from sklearn.naive_bayes import GaussianNB


def formFeature(lines,featureWords):       #根据评语，获得转换矩阵，是否有特征词
    feature=[]
    for s in lines:
        oneFeature=[]
        for w in featureWords:
            if w in s:
                oneFeature.append(1)
            else:
                oneFeature.append(0)
        feature.append(oneFeature)
    return np.array(feature)

def formFeatureCount(lines,featureWords):   #根据评语，获得转换矩阵，特征词数
    feature=np.zeros((len(lines),len(featureWords)))
    for i in range(feature.shape[0]):
        for j in range(feature.shape[1]):
            feature[i,j]=lines[i].count(featureWords[j])
    return feature

def extractFeatureWords():              #提取特征词，生成词典
    file=open('../data/comment.txt','r',encoding='utf-8')
    lines=file.readlines()
    debate=[]
    for i in range(len(lines)):
        oneLine=lines[i]
        info=oneLine.split()
        debate.append(info[0])

    al=jieba.lcut(''.join(debate),cut_all=True)
    al=[elem for elem in al if elem !='']
    al=dict(Counter(al))
    res=list(reversed(sorted(al.items(),key=lambda x:x[1])))
    res=list(filter(lambda x:x[1]>2,res))
    for i in res:
        print(i)
    
if __name__=='__main__':
    featureWords=['赞','差','太差','帅','起球','不好','货真价实','上当']  
    file=open('data/comment.txt','r',encoding='utf-8')
    lines=file.readlines()
    debate=[]
    ans=np.zeros((len(lines),1))
    for i in range(len(lines)):
        oneLine=lines[i]
        info=oneLine.split()
        debate.append(info[0])
        ans[i,0]=float(info[1])
    feature=formFeatureCount(debate,featureWords)
    bayes=GaussianNB()
    model=bayes.fit(feature,ans)
    newDebate=["这么差的衣服以后再也不买了","帅呆了，赞"]
    feature1=formFeatureCount(newDebate,featureWords)
    pred=model.predict(feature1)
    print(pred)
