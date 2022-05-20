import numpy as np

class PyLL:
    def __init__(self,key,value : int,nextItem):
        self.key = key
        self.value = value
        self.next = nextItem

class PyHashTable:
    def __init__(self,capacity,totalItems):
        self.arr = np.full((capacity),None,dtype=PyLL)
        self.__total = totalItems
        self.capacity = capacity
    def calcHash(self,item,c):
        return ((item-1)*self.__total + c) % self.capacity
    def get(self,item,c):
        if item <= 0 or c <= 0:
            return 0,2
        LLEntry = self.arr[self.calcHash(item,c)]
        ops = 6
        key = (item,c)
        while LLEntry != None:
            if LLEntry.key == key:
                return LLEntry.value, ops
            ops += 3
            LLEntry = LLEntry.next
        return None, ops
    def insert(self,item,c,value):
        
        ourHash = self.calcHash(item,c)
        LLEntry = self.arr[ourHash]
        ops = 5 # 4 arithmetic and 1 comparison
        self.arr[ourHash] = PyLL((item,c),value,LLEntry)
        return ops
def DPKnapsack(weights,values,capacity):
    ops = 0
    #memory = [[0]*(capacity+1)]
    memory = np.full((len(weights),capacity+1),-1)
    for c in range(capacity+1):
        ops += 2
        #memory.append([-1]*(capacity+1))
        memory[0][c] = 0
    for item in range(1,len(weights)):
        ops += 2
        #memory.append([-1]*(capacity+1))
        memory[item][0] = 0
    for item in range(1,len(weights)):
        ops += 2 #1 piece of arithmetic and 1 comparison
        #memory.append([0])
        itemWeight = weights[item]
        itemValue = values[item]
        for c in range(1,itemWeight):
            ops += 4 #2 pieces of arithmetic and 2 comparisons
            memory[item][c] = memory[item-1][c]
        for c in range(itemWeight,capacity+1):
            ops += 6 #4 pieces of arithmetic and 2 comparisons
            maxVal = max(memory[item-1][c], itemValue + memory[item-1][c-itemWeight])
            memory[item][c] = maxVal
    
    item = len(weights)-1
    c = capacity
    chosen = []
    value = 0
    while item > 0 and c > 0:
        ops += 2 # 2 comparisons
        if memory[item-1][c] < memory[item][c]:
            ops += 4 # 3 arithmetic and 1 comparison
            chosen.append(item)
            value += values[item]
            c -= weights[item]
            
        item -= 1
    return value,chosen,ops


    
def MFKnapsackHelper(weights,values,memory,item,c):
    ops = 0
    if memory[item][c] == -1:
        withoutItemVal, ops = MFKnapsackHelper(weights,values,memory,item-1,c)
        ops += 2 #1 arithmetic and 1 comparison
        if c < weights[item]:
            value = withoutItemVal
        else:
            withItemVal, newOps = MFKnapsackHelper(weights,values,memory,item-1,c-weights[item])
            ops += newOps + 3
            value = max(withoutItemVal, values[item]+withItemVal)
        memory[item][c] = value
    return memory[item][c], ops + 1


def MFKnapsack(weights,values,capacity):
    ops = 1
    memory = np.full((len(weights),capacity+1),-1)
    for c in range(capacity+1):
        ops += 2
        #memory.append([-1]*(capacity+1))
        memory[0][c] = 0
    for item in range(1,len(weights)):
        ops += 2
        #memory.append([-1]*(capacity+1))
        memory[item][0] = 0
    _, newOps = MFKnapsackHelper(weights,values,memory,len(weights)-1,capacity)
    ops += newOps
    #for item in memory:
    #    print(*i)
    item = len(weights)-1
    c = capacity
    chosen = []
    value = 0
    while item > 0 and c > 0:
        ops += 4
        if memory[item-1][c] < memory[item][c]:
            ops += 2
            chosen.append(item)
            value += values[item]
            c -= weights[item]
        item -= 1
    return value, chosen, ops

def LLMFKnapsackHelper(weights,values,memory,item,c,ops):
    value, newOps = memory.get(item,c)
    ops += newOps
    if value == None:
        value, ops = LLMFKnapsackHelper(weights,values,memory,item-1,c,ops+1)
        if c >= weights[item]:
            withValue, ops = LLMFKnapsackHelper(weights,values,memory,item-1,c-weights[item],ops+2)
            value = max(value, values[item]+withValue)
            ops += 2
        ops += memory.insert(item,c,value)
    return value, ops

def LLMFKMultiHelper(args):
    return *LLMFKnapsack(*args),args[-1]

def LLMFKnapsack(weights,values,capacity,k=-1,retSpace = True):
    if k == -1:
        k = capacity
    hashTable = PyHashTable(k,len(weights)-1)
    ops = 2
    #for i in range(capacity+1):
    #    ops += 2
    #    hashTable.insert(0,i,0)
    #for i in range(len(weights)-1):
    #    ops += 2
    #    hashTable.insert(i,0,0)
    value, ops = LLMFKnapsackHelper(weights,values,hashTable,len(weights)-1,capacity,ops)
    item = len(weights)-1
    c = capacity
    chosen = []
    while item > 0 and c > 0:
        ops += 4
        lessItem,newOps = hashTable.get(item-1,c)
        ops += newOps
        curItem, newOps = hashTable.get(item,c)
        ops += newOps
        if lessItem < curItem:
            chosen.append(item)
            c -= weights[item]
            ops += 1
        item -= 1
    ops += 2
    if retSpace:
        itemsOutThere = hashTable.capacity
        for key in hashTable.arr:
            if key == None:
                continue
            key = key.next
            while key != None:
                key = key.next
                itemsOutThere += 1
        return value,chosen,ops,itemsOutThere
    else:
        return value,chosen,ops