import numpy.random as npr
class Individual:
    eval=0
    chromcome=None
    def __init__(self,n):
        self.chromcome=npr.random(n)

class NGA:
    population=[]
    dimension=1
    bestPos=worstPos=0
    mutationProb=10
    crossoverProb=90
    maxIterTime=1000
    evalFunc=None
    arfa=1.0
    popu=2
    def __init__(self,popu,dimension,crossoverProb,mutationProb,maxIterTime,evalFunc):
        for i in range(popu):
            oneId=Individual(dimension)
            oneId.eval=evalFunc(oneId.chromcome)
            self.population.append(oneId)
        
        self.crossoverProb=crossoverProb
        self.mutationProb=mutationProb
        self.maxIterTime=maxIterTime
        self.evalFunc=evalFunc
        self.popu=popu
        self.dimension=dimension

    def crossover(self):
        fatherPos=npr.randint(0,self.popu)
        motherPos=npr.randint(0,self.popu)
        while motherPos==fatherPos:
            motherPos=npr.randint(0,self.popu)
            fatherPos=npr.randint(0,self.popu)
        father=self.population[fatherPos]
        mother=self.population[motherPos]
        startPos=npr.randint(self.dimension)
        juneLength=npr.randint(self.dimension)

        son1=Individual(self.dimension)
        son2=Individual(self.dimension)

        son1.chromcome[0:startPos]=father.chromcome[0:startPos]
        son2.chromcome[0:startPos]=mother.chromcome[0:startPos]

        son1.chromcome[startPos:juneLength]=mother.chromcome[startPos:juneLength]
        son2.chromcome[startPos:juneLength]=father.chromcome[startPos:juneLength]
        left=startPos+juneLength

        son1.chromcome[left:]=father.chromcome[left:]
        son2.chromcome[left:]=mother.chromcome[left:]
        son1.eval=self.evalFunc(son1.chromcome)
        son2.eval=self.evalFunc(son2.chromcome)
        self.findBestWorst()

        if son1.eval<self.population[self.worstPos].eval:
            self.population[self.worstPos]=son1
        self.findBestWorst()
        if son2.eval<self.population[self.worstPos].eval:
            self.population[self.worstPos]=son2      
    
    def mutation(self):
        father=self.population[npr.randint(self.popu)]
        son=Individual(self.dimension)
        son.chromcome[0:]=father.chromcome[0:]
        mutationPos=npr.randint(self.dimension)
        temp=npr.random()
        sign=npr.randint(0,2)
        if sign==0:
            temp=-temp
        son.chromcome[mutationPos]=father.chromcome[mutationPos]+self.arfa*temp
        son.eval=self.evalFunc(son.chromcome)
        self.findBestWorst()
        if son.eval<self.population[self.worstPos].eval:
            self.population[self.worstPos]=son

    def findBestWorst(self):
        worst=best=self.population[0].eval
        worstPos=bestPos=0
        for i in range(self.popu):
            if best>self.population[i].eval:
                bestPos=i
                best=self.population[i].eval
            if worst<self.population[i].eval:
                worstPos=i
                worst=self.population[i].eval
        
        self.bestPos=bestPos
        self.worstPos=worstPos

    def solve(self):
        shrinkTimes=self.maxIterTime/10
        oneFold=shrinkTimes
        i=0
        while i<self.maxIterTime:
            print(i,"---",self.maxIterTime)
            if i==shrinkTimes:
                self.arfa=self.arfa/2.0
            shrinkTimes+=oneFold
            for j in range(self.crossoverProb):
                self.crossover()
            for j in range(self.mutationProb):
                self.mutation()
            print("solution:",self.population[self.bestPos].chromcome)
            print("func value:",self.population[self.bestPos].eval)
            i+=1

    def getAnswer(self):
        self.findBestWorst()
        return self.population[self.bestPos].chromcome