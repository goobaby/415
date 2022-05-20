import graphs
import sys
import task1
import task2
from pathlib import Path

if __name__ == '__main__':
    data_folder = Path("KnapsackTestData")
    #filePrefix = input("common file prefix (for example, KnapsackTestData\\p01_c's prefix is KnapsackTestData\\p01_):")
    if len(sys.argv) != 2:
        print("Usage:",sys.argv[0],"<number of file to open>")
        quit()
    fileNum = sys.argv[1].rjust(2,'0')
    filePrefix = data_folder 


    def parseFile(filename):
        with open(filename) as f:
            result = []
            for i in f.readlines():
                result.append(int(i))
        return result
    weights = parseFile(filePrefix / ('p'+fileNum + "_w.txt"))
    values = parseFile(filePrefix / ('p'+fileNum + "_v.txt"))
    capacity = int(open(filePrefix / ('p'+fileNum + "_c.txt")).readline())

    def printResults(name,value,path,operations):
        path.reverse()
        print(name,"Optimal value:",value)
        print(name,"Optimal subset:",path)
        print(name,"Total Basic Ops:",operations)
        print("")
    def printResultsSpace(name,value,path,operations,space):
        path.reverse()
        print(name,"Optimal value:",value)
        print(name,"Optimal subset:",path)
        print(name,"Total Basic Ops:",operations)
        print(name,"Space Taken:",space)
        print("")

    def runGraph(graphFunc,graphArgs,graphName,**kwargs):
        graph = graphFunc(*graphArgs,**kwargs)
        graph.savefig(graphName)
        graph.close()
        print(graphName,"complete!")

    if False:
        #runGraph(graphs.graphOne,(0,8),"One-Eightless")

        #runGraph(graphs.graphOne,(0,9),"One-Eighted") 
        #runGraph(graphs.graphTwoA,(),"TwoA")
        #runGraph(graphs.graphTwoB,(weights,values,capacity,"p08"),"TwoBYes",showMFK=True)
        #runGraph(graphs.graphTwoB,(weights,values,capacity,"p08"),"TwoBNo")
        runGraph(graphs.graphThree,(0,9),"Three")
    else:
        printResults("(1a) Traditional Dynamic Programming",*task1.DPKnapsack(weights,values,capacity))
        printResults("(1b) Memory-function Dynamic Programming",*task1.MFKnapsack(weights,values,capacity))
        printResultsSpace("(1c) Space-efficient Dynamic Programming",*task1.LLMFKnapsack(weights,values,capacity))

        task2.greedyapproach(weights, values, capacity)