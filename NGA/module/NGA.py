import numpy as np
import numpy.random as npr
class Individual:
    _n=0
    eval=0.0
    chromsome=None
    def __init__(self,n):
        self._n=n
        self.chromsome=npr.random(n)
        
class NGA:
    population=[]
    dimension=1         #个体变量数
    bestPos=worstPos=0  #最好、最差个体位置
    mutationProb=10     #变异概率
    crossoverProb=90    #交叉概率
    maxIterTime=1000    #最大迭代次数
    evalFunc=None       #评估函数
    arfa =1.0           #收敛参数，变异步长
    popu=2              #种群大小
    def __init__(self,popu, dimension,crossoverProb,mutationProb,maxIterTime,evalFunc):
        for i in range(popu):           #初始化种群
            oneInd=Individual(dimension)
            oneInd.eval=evalFunc(oneInd.chromsome)
            self.population.append(oneInd)      
            
        self.crossoverProb=crossoverProb
        self.mutationProb=mutationProb
        self.maxIterTime=maxIterTime
        self.evalFunc=evalFunc
        self.popu=popu
        self.dimension=dimension
    
    #找最好的个体位置
    def findBestWorst(self):
        worst=best= self.population[0].eval
        worstPos=bestPos = 0
        
        for i in range(1,self.popu):
            if best > self.population[i].eval:
                bestPos = i
                best = self.population[i].eval
            if worst<self.population[i].eval:
                worstPos=i
                worst=self.population[i].eval
        self.bestPos=bestPos
        self.worstPos=worstPos
       #交叉操作 
    def crossover(self):
        fatherPos=npr.randint(0,self.popu)
        motherPos=npr.randint(0,self.popu)
        while motherPos == fatherPos:
            motherPos = npr.randint(0,self.popu)
        father = self.population[fatherPos]
        mother = self.population[motherPos]
        startPos = npr.randint(self.dimension) #交叉的起始位置
        jeneLength = npr.randint(self.dimension)+1 # //交叉的长度
        #jeneLength = self.dimension - startPos #  //基因交换的有效长度
        son1 = Individual(self.dimension)
        son2 = Individual(self.dimension)

        son1.chromsome[0:startPos]=father.chromsome[0:startPos]
        son2.chromsome[0:startPos]=mother.chromsome[0:startPos]
        
        son1.chromsome[startPos:jeneLength]=mother.chromsome[startPos:jeneLength]
        son2.chromsome[startPos:jeneLength]=father.chromsome[startPos:jeneLength]
        left=startPos+jeneLength
        
        son1.chromsome[left:]=father.chromsome[left:]
        son2.chromsome[left:]=mother.chromsome[left:]
        son1.eval = self.evalFunc(son1.chromsome) #;// 评估第一个子代
        son2.eval = self.evalFunc(son2.chromsome)
        self.findBestWorst()
        
        if son1.eval < self.population[self.worstPos].eval:
            self.population[self.worstPos] = son1
        self.findBestWorst()
        if son2.eval < self.population[self.worstPos].eval:
            self.population[self.worstPos] = son2
            
    def mutation(self):
        father = self.population[npr.randint(self.popu)]
        son = Individual(self.dimension)
        son.chromsome=father.chromsome.copy()
        mutationPos =npr.randint(self.dimension)#;//变异的位置
        #产生一个0-1之间的随机小数
        temp = npr.random()
        sign = npr.randint(0,2)   # ;//产生0 或1，决定+ 还是 -
        if sign == 0:
            temp = -temp
        son.chromsome[mutationPos] += self.arfa * temp
        son.eval = self.evalFunc(son.chromsome)
        self.findBestWorst()
        if son.eval < self.population[self.worstPos].eval:
            self.population[self.worstPos] = son
            
    def solve(self):
        shrinkTimes = self.maxIterTime / 10 
        #//将总迭代代数分成10份
        oneFold = shrinkTimes #;//每份中包含的次数
        i = 0
        while i < self.maxIterTime:
            print(i,"---",self.maxIterTime)
            if i == shrinkTimes:
                self.arfa =self.arfa / 2.0
            #经过一份代数的迭代后，将收敛参数arfa缩小为原来的1/2，以控制mutation
                shrinkTimes += oneFold  #;//下一份到达的位置
            for  j in range(self.crossoverProb):
                self.crossover()
            for  j in range(self.mutationProb):
                self.mutation()
            # print("solution:",self.population[self.bestPos].chromsome)
            # print("func value:",self.population[self.bestPos].eval)
            i=i+1
            
    def getAnswer(self):
        self.findBestWorst()
        return self.population[self.bestPos].chromsome


