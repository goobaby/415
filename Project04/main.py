import graphs
import task1


filePrefix = input("common file prefix (for example, KnapsackTestData\\p01_c's prefix is KnapsackTestData\\p01_):")

def parseFile(filename):
    with open(filename) as f:
        result = [0]
        for i in f.readlines():
            result.append(int(i))
    return result

def printResults(name,value,path,operations):
    print(name,"Optimal value:",value)
    print(name,"Optimal subset:",path)
    print(name,"Total Basic Ops:",operations)
    print("")

weights = parseFile(filePrefix + "w.txt")
values = parseFile(filePrefix + "v.txt")
capacity = int(open(filePrefix + "c.txt").readline())

graphs.graphTwo(weights,values,capacity)

DPResults = task1.DPKnapsack(weights,values,capacity)
MFKResults = task1.MFKnapsack(weights,values,capacity)
LLMFKResults = task1.LLMFKnapsack(weights,values,capacity)

printResults("(1a) Traditional Dynamic Programming",*DPResults)
printResults("(1b) Memory-function Dynamic Programming",*MFKResults)
printResults("(1c) Space-efficient Dynamic Programming",*LLMFKResults)

