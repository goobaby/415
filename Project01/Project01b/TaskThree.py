from math import ceil, floor,sqrt
import UserTestingMode
import ScatterplotMode
def sieve(m,n):
    if n < m:
        n,m = m,n
    adds = 1
    A = list(range(m+1))
    for p in range(2,floor(sqrt(m))+1):
        if A[p] != 0:
            j = p*p
            while j <= m:
                A[j] = 0
                adds += 1
                j = j + p
    results = []
    for p in range(m+1):
        if A[p] != 0:
            results.append(A[p])
    return results, adds

def middleSchoolStepTwo(primesToN,m,n):
    #building list of prime factors
    ops = 0
    neatlyReorgged = [m,n]
    factors = []
    for i in range(2):
        factors.append([])
        j = 0
        while j < len(primesToN) and primesToN[j] <= neatlyReorgged[i]:
            ops += 1
            if neatlyReorgged[i]%primesToN[j] == 0:
                factors[i].append(primesToN[j])
            j += 1
    return factors[0],factors[1], ops

def middleSchoolStepThree(mFactors,nFactors):
    ops = 2
    mIndex = len(mFactors)-1
    nIndex = len(nFactors)-1
    while mFactors[mIndex] != nFactors[nIndex]:
        ops += 1
        if mFactors[mIndex] > nFactors[nIndex]:
            mIndex -= 1
        else:
            nIndex -= 1
    return mFactors[mIndex], ops

def harvardMiddleSchoolGCD(n):
    opsSum = 0
    for i in range(1,n+1):
        primesToI, ops = sieve(n,i)
        opsSum += ops
        nFactors, iFactors, opsTwo = middleSchoolStepTwo(primesToI,n,i)
        opsSum += opsTwo
        opsThree = middleSchoolStepThree(nFactors,iFactors)[1]
        opsSum += opsThree
    print("Middle School Method took",opsSum / float(n),"operations on average.")
    return ""
    #return opsSum / float(n)

def SPSieveWrapper(n):
    opsSum = 0
    for i in range(1,n+1):
        primesToN, ops = sieve(n,i)
        opsSum += ops
    return opsSum / float(n)

def SPStepTwoWrapper(n):
    opsSum = 0
    
    for i in range(1,n+1):
        primesToI, ops = sieve(n,i)
        nFactors, iFactors, opsTwo = middleSchoolStepTwo(primesToI,n,i)
        opsSum += opsTwo
    return opsSum / float(n)

def SPStepThreeWrapper(n):
    opsSum = 0
    for i in range(1,n+1):
        primesToN, ops = sieve(n,i)
        nFactors, iFactors, opsTwo = middleSchoolStepTwo(primesToN,n,i)
        opsThree = middleSchoolStepThree(nFactors,iFactors)[1]
        opsSum += opsThree
    return opsSum / float(n)

UserTestingMode.Task(2,"3","MSPAvg Calculator",["tests up to n to average"],[int],harvardMiddleSchoolGCD)
ScatterplotMode.Task(2,"3","MSPAvg Basic Operations","set of integers up to and including n","Average Basic Operations",range(2,150),
["Sieve of Eratosthenes", "Building Prime Factors", "Finding Common Factors"],[SPSieveWrapper,SPStepTwoWrapper,SPStepThreeWrapper])