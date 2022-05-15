import graphs
import task1
import task2

if __name__ == '__main__':
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

    def runGraph(graphFunc,graphArgs,graphName,**kwargs):
        graph = graphFunc(*graphArgs,**kwargs)
        graph.savefig(graphName)
        graph.close()
        print(graphName,"complete!")

    weights = parseFile(filePrefix + "w.txt")
    values = parseFile(filePrefix + "v.txt")
    capacity = int(open(filePrefix + "c.txt").readline())

    runGraph(graphs.graphOne,(0,8),"One Eightless")

    #runGraph(graphs.graphOne,(0,9),"One Eighted") 
    runGraph(graphs.graphTwoA,(),"TwoA")
    runGraph(graphs.graphTwoB,(weights,values,capacity,"p08"),"TwoBYes",showMFK=True)
    runGraph(graphs.graphTwoB,(weights,values,capacity,"p08"),"TwoBNo")

    #DPResults = task1.DPKnapsack(weights,values,capacity)
    #MFKResults = task1.MFKnapsack(weights,values,capacity)
    #LLMFKResults = task1.LLMFKnapsack(weights,values,capacity)

    #printResults("(1a) Traditional Dynamic Programming",*DPResults)
    #printResults("(1b) Memory-function Dynamic Programming",*MFKResults)
    #printResults("(1c) Space-efficient Dynamic Programming",*LLMFKResults)

task2.greedyapproach(weights, values, capacity)