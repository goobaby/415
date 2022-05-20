from multiprocessing import Pool, TimeoutError
import task1
import task2
import matplotlib.pyplot as plt
import numpy as np
from math import ceil


def parseFile(filename):
    with open(filename) as f:
        result = []
        for i in f.readlines():
            result.append(int(i))
    return result

def allGraphData(min=0,max=9):
    for i in range(min,max):
        filePrefix = "KnapsackTestData/p0" + str(i) +"_"
        weights = parseFile(filePrefix + "w.txt")
        values = parseFile(filePrefix + "v.txt")
        capacity = int(open(filePrefix + "c.txt").readline())
        yield weights, values, capacity
        #DPResults = task1.DPKnapsack(weights,values,capacity)
        #MFKResults = task1.MFKnapsack(weights,values,capacity)
        #LLMFKResults = task1.LLMFKnapsack(weights,values,capacity)
def graphOne(fileMin,fileMax):
    data = [[],[],[]]
    for weights, values, capacity in allGraphData(min=fileMin,max=fileMax):
        DPResults = task1.DPKnapsack(weights,values,capacity)
        MFKResults = task1.MFKnapsack(weights,values,capacity)
        #LLMFKResults = task1.LLMFKnapsack(weights,values,capacity)
        data[0].append(DPResults[2])
        data[1].append(MFKResults[2])
        #data[2].append(LLMFKResults[2])
        print("built for another test case")
    X = np.arange(fileMin,fileMax)
    plt.title("Relative Performance of Algorithms")
    plt.xlabel("Test Case")
    plt.ylabel("Basic Operations (log scale)")
    plt.xticks(list(map(lambda x: x+0.375/2,X)),list(map(lambda x: "p0" + str(x),X)))
    #ax = fig.add_axes([0,0,1,1])
    plt.bar(X + 0.00, data[0], width = 0.375)
    plt.bar(X + 0.375, data[1], width = 0.375)
    #plt.bar(X + 0.50, data[2], width = 0.25)
    #plt.legend(labels = ["Traditional","Memory Function","Space-Efficient"])
    plt.legend(labels = ["Traditional","Memory Function"])
    plt.yscale('log')
    plt.grid(axis='y')
    return plt


def graphTwoData(weights,values,capacity, ourRange, buildWithMFK = False):
    data = [None] * ceil((ourRange.stop - ourRange.start)/ourRange.step)
    spaceData = [None] * ceil((ourRange.stop - ourRange.start)/ourRange.step)
    background = None
    backgroundSpace = None
    completed = 0
    
    if buildWithMFK:
        background = [task1.MFKnapsack(weights,values,capacity)[2]]
        backgroundSpace = [capacity * len(weights) - len(weights)]
    with Pool(processes = 4) as pool:
        argsRange = list(map(lambda i : [weights,values,capacity,i],ourRange))
        for D in pool.imap_unordered(task1.LLMFKMultiHelper, argsRange):
            completed += 1
            index = (D[4] - ourRange.start)//ourRange.step
            data[index] = D[2]
            spaceData[index] = D[3]
            if completed % ((ourRange.stop - ourRange.start)/10) < ourRange.step:
                print(round(completed/(ourRange.stop - ourRange.start)*100*ourRange.step),"% complete")
    if buildWithMFK:
        return data,spaceData,background,backgroundSpace
    else:
        return data,spaceData

def graphTwoA():
    allData = []
    names = []
    count = 0
    for weights, values, capacity in allGraphData(min=8):
        ourRange = range(capacity//10,capacity*2,capacity//10)
        rangeList = list(map(lambda x : x / capacity, ourRange))
        data,spaceData = graphTwoData(weights,values,capacity,ourRange)
        allData.append(rangeList)
        allData.append(data)
        
        #names.append("p"+str(count))
        count += 1
    #data,spaceData,background,backgroundSpace = graphTwoData(weights,values,capacity, ourRange)
    #plt.plot(spaceData,data,'ro',backgroundSpace,background,'g^')
    # actual : plt.scatter(spaceData,data,c=np.linspace(0,2 * np.pi,ceil((ourRange.stop - ourRange.start)/ourRange.step)),ec='k')
    plt.plot(*allData)
    #plt.legend(labels = names)
    #plt.plot()
    plt.suptitle("Space-Efficient Knapsack Performance for Different Values of k")
    plt.xlabel('k/Capacity')
    plt.ylabel('Basic Operations')
    plt.grid()
    return plt

def graphTwoB(weights,values,capacity,testCase,showMFK = False):
    ourRange = range(capacity//10,capacity*2,capacity//10)
    data,spaceData,background,backgroundSpace = graphTwoData(weights,values,capacity, ourRange, buildWithMFK=showMFK)
    plt.scatter(spaceData,data,c=np.linspace(0,2 * np.pi,ceil((ourRange.stop - ourRange.start)/ourRange.step)),ec='k')
    if showMFK:
        plt.scatter(backgroundSpace,background,marker='^')
        plt.suptitle("Comparitive Memory Usage and Performance of Algorithms")
        plt.legend(labels = ["Space-Efficient","Memory Function"])
    else:
        plt.suptitle("Memory Usage and Performance of Space-Efficient Algorithm")
    plt.grid()
    plt.title("Test Case Used: "+testCase,fontsize = 10)
    plt.xlabel('Space Taken')
    plt.ylabel('Basic Operations')
    
    return plt

def graphThree(fileMin,fileMax):
    data = [[],[],[]]
    for weights, values, capacity in allGraphData(min=fileMin,max=fileMax):
        basicResults = task2.basicgreedyapproach(weights,values,capacity)
        heapResults = task2.heapgreedyapproach(weights,values,capacity)
        #LLMFKResults = task1.LLMFKnapsack(weights,values,capacity)
        data[0].append(basicResults)
        data[1].append(heapResults)
        #data[2].append(LLMFKResults[2])
        print("built for another test case")
    X = np.arange(fileMin,fileMax)
    plt.title("Relative Performance of Algorithms")
    plt.xlabel("Test Case")
    plt.ylabel("Basic Operations")
    plt.xticks(list(map(lambda x: x+0.375/2,X)),list(map(lambda x: "p0" + str(x),X)))
    #ax = fig.add_axes([0,0,1,1])
    plt.bar(X + 0.00, data[0], width = 0.375)
    plt.bar(X + 0.375, data[1], width = 0.375)
    #plt.bar(X + 0.50, data[2], width = 0.25)
    #plt.legend(labels = ["Traditional","Memory Function","Space-Efficient"])
    plt.legend(labels = ["Sorting","Max Heap"])
    #plt.yscale('log')
    plt.grid(axis='y')
    return plt