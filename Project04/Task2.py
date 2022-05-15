#Task 2

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
    mergecount = 0
    leftmost, rightmost = 0, 0
    while leftmost < len(left) and rightmost < len(right):
      
        # Sort each one and place into the result
        if left[leftmost] >= right[rightmost]:
            mergecount += 1
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
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    n = int((len(A) // 2)-1)
    for i in range(n, -1,-1):
        max_heapify(A, i)


def deletemax(A, n):
    A[n], A[0] = A[0], A[n]
    A.pop()
    

def greedyapproach(weights, values, capacity):
    ratioarray = merge_sort(combine(weights, values))
    #print(ratioarray)
    optimalarray = grabbingOptimal(ratioarray, capacity)
    #print(optimalarray)
    
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
    print (optimalheaparry)

        

        

values = [10, 20, 2, 4, 8, 6, 5, 7, 9, 1, 3]
weights = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

greedyapproach(weights, values, 15)
