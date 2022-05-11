import task1
import matplotlib.pyplot as plt
import numpy as np
def graphOne():
    data = [[],[],[]]
    for i in range(8):
        filePrefix = "KnapsackTestData\\p0" + str(i) +"_"
        weights = parseFile(filePrefix + "w.txt")
        values = parseFile(filePrefix + "v.txt")
        capacity = int(open(filePrefix + "c.txt").readline())

        DPResults = task1.DPKnapsack(weights,values,capacity)
        MFKResults = task1.MFKnapsack(weights,values,capacity)
        LLMFKResults = task1.LLMFKnapsack(weights,values,capacity)
        data[0].append(DPResults[2])
        data[1].append(MFKResults[2])
        data[2].append(LLMFKResults[2])
        X = np.arange(8)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(X + 0.00, data[0], width = 0.25)
    ax.bar(X + 0.25, data[1], width = 0.25)
    ax.bar(X + 0.50, data[2], width = 0.25)
    ax.legend(labels = ["Traditional","Memory Function","Space-Efficient"])
    plt.show()


def graphTwo(weights,values,capacity):
    data = []
    spaceData = []
    background = []
    backgroundSpace = []
    for i in range(1,capacity,2):
        D = task1.LLMFKnapsack(weights,values,capacity,i,retSpace=True)
        data.append(D[2])
        spaceData.append(D[3])
        background.append(task1.MFKnapsack(weights,values,capacity)[2])
        backgroundSpace.append(capacity * len(weights) - len(weights))
        if i % (capacity/10) < 2:
            print(i/capacity,"% complete")
    plt.plot(spaceData,data)
    plt.plot(backgroundSpace,background)
    plt.xlabel('space taken')
    plt.ylabel('Basic Operations')
    plt.show()