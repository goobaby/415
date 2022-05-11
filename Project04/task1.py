from zmq import has


class PyLL:
    def __init__(self,value,nextItem):
        self.value = value
        self.next = nextItem

class PyHashTable:
    def __init__(self,capacity,totalItems):
        self.arr = [None] * capacity
        self.__total = totalItems
        self.capacity = capacity
    def calcHash(self,item,c):
        return ((item-1)*self.__total + c) % self.capacity
    def get(self,item,c):
        #if item <= 0 or c <= 0:
        #    return 0,2 added as optimization but unfair to other programs
        LLEntry = self.arr[self.calcHash(item,c)]
        ops = 4
        LLValue = None
        while LLEntry != None and (LLEntry.value.item != item or LLEntry.value.c != c):
            ops += 3
            LLEntry = LLEntry.next
        ops = 1 + [0,2][LLEntry != None]
        return LLEntry.value.value if LLEntry != None and LLEntry.value.item == item and LLEntry.value.c == c else None, ops+1
    def insert(self,item,c,value):
        
        ourHash = self.calcHash(item,c)
        LLEntry = self.arr[ourHash]
        ops = 5 # 4 arithmetic and 1 comparison
        newEntry = PyLL(PyMFKItem(item,c,value),None)
        if LLEntry == None:
            self.arr[ourHash] = newEntry
        else:
            while LLEntry.next != None:
                ops += 1
                LLEntry = LLEntry.next
            ops += 1
            LLEntry.next = newEntry
        return ops
class PyMFKItem:
    def __init__(self,item,c,value) -> None:
        self.item = item
        self.c = c
        self.value = value
def DPKnapsack(weights,values,capacity):
    ops = 0
    memory = [[0]]
    for c in range(1,capacity+1):
        ops += 2 #1 piece of arithmetic and 1 comparison
        memory[0].append(0)
    for item in range(1,len(weights)):
        ops += 2 #1 piece of arithmetic and 1 comparison
        memory.append([0])
        for c in range(1,weights[item]):
            ops += 4 #2 pieces of arithmetic and 2 comparisons
            memory[item].append(memory[item-1][c])
        for c in range(weights[item],capacity+1):
            ops += 6 #4 pieces of arithmetic and 2 comparisons
            maxVal = max(memory[item-1][c], values[item] + memory[item-1][c-weights[item]])
            memory[item].append(maxVal)
    
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
    memory = [[]]
    ops = 0
    for item in range(capacity+1):
        ops += 2
        memory[0].append(0)
    for item in range(1,len(weights)):
        ops += 2
        memory.append([0])
        for c in range(1,capacity+1):
            ops += 2
            memory[item].append(-1)
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

def LLMFKnapsack(weights,values,capacity,k=-1,retSpace = False):
    if k == -1:
        k = capacity*2
    hashTable = PyHashTable(k,len(weights)-1)
    ops = k*2 + 2
    for i in range(capacity+1):
        ops += 2
        hashTable.insert(0,i,0)
    for i in range(len(weights)-1):
        ops += 2
        hashTable.insert(i,0,0)
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