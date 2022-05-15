#Task 2
totalbasicA = 0
totalbasicB = 0
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    global totalbasicA
    leftmost, rightmost = 0, 0
    while leftmost < len(left) and rightmost < len(right):
        totalbasicA += 1
        # Sort each one and place into the result
        if left[leftmost] >= right[rightmost]:
            
            merged[leftmost+rightmost]=left[leftmost]
            leftmost += 1
        else:
            merged[leftmost + rightmost] = right[rightmost]
            rightmost += 1
            
    for leftmost in range(leftmost, len(left)):
        merged[leftmost + rightmost] = left[leftmost]
        
    for rightmost in range(rightmost, len(right)):
        merged[leftmost + rightmost] = right[rightmost]

    return merged

def combine(weights, values):
    greedyarray = []
    #if values and weights sizes are different uh oh
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        greedyarray.append((ratio, weights[i], i+1))
    return greedyarray

def grabbingOptimal(ratio, capacity):
    optimal = 0
    optimallocarray = []
    for index, tuple in enumerate(ratio):
        if tuple[1] > capacity:
            break
        elif tuple[1] <= capacity:
            capacity -= tuple[1] #weight
            optimal += tuple[0] #values
            optimallocarray.append(tuple)       
    return optimallocarray

def max_heapify(A,i):
    l = 2 * i + 1
    r = 2 * i + 2
    global totalbasicB
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        totalbasicB += 1
        max_heapify(A, largest)

def build_max_heap(A):
    n = int((len(A) // 2)-1)
    for i in range(n, -1,-1):
        max_heapify(A, i)


def deletemax(A, n):
    A[n], A[0] = A[0], A[n]
    A.pop()
    global totalbasicB
    totalbasicB += 1

def gettingvaluesfromoptimal(A):
    totvalues = 0
    for index, tuple in enumerate(A):
        totvalues += tuple[0]
        
        global totalbasicB
        totalbasicB += 1
        global totalbasicA
        totalbasicA += 1
        
    return totvalues

def gettingindexfromoptimal(A):
    totvalues = []
    for index, tuple in enumerate(A):
        totvalues.append(tuple[2])
        
        global totalbasicB
        totalbasicB += 1
        global totalbasicA
        totalbasicA += 1
        
    return totvalues

def greedyapproach(weights, values, capacity):
    ratioarray = merge_sort(combine(weights, values))
    #print(ratioarray)
    optimalarray = grabbingOptimal(ratioarray, capacity)
    #print(optimalarray)
    
    totalvalue = gettingvaluesfromoptimal(optimalarray)
    print("(2a) Greedy Approach Optimal value: ", totalvalue)
    indexset = gettingindexfromoptimal(optimalarray)
    print("(2a) Greedy Approach Optimal subset: ", indexset)
    
    print("(2a) Greedy Approach Total Basic Ops: ", totalbasicA, "\n")
    
    #----------------------------------------------------------
    
    heaparray = combine(weights, values)
    
    build_max_heap(heaparray)

    capacityheap = capacity
    optimalheaparry = []
    for i in range(len(heaparray)):
        if heaparray[0][1] <= capacityheap :
            capacityheap -= heaparray[0][1]
            optimalheaparry.append(heaparray[0])  
        n = len(heaparray) -1 
        deletemax(heaparray, n)
        build_max_heap(heaparray)
    #print (optimalheaparry)
    
    totalheapvalue = gettingvaluesfromoptimal(optimalheaparry)
    print("(2b) Heap-based Greedy Approach Optimal value: ", totalheapvalue)
    heapindexset = gettingindexfromoptimal(optimalheaparry)
    print("(2b) Heap-based Greedy Approach Optimal subset: ",heapindexset)
    
    print("(2b) Heap-based Greedy Approach Total Basic Ops: ", totalbasicB, "\n")
        

        

# values = [10, 20, 2, 4, 8, 6, 5, 7, 9, 1, 3]
# weights = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# greedyapproach(weights, values, 15)
