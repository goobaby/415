import UserTestingMode
import ScatterplotMode

#def fib(a,b,termsToCalc):
#    termsToCalc-=1
#    if termsToCalc == 0:
#        return a+b
#    return fib(b,a+b,termsToCalc)

def fib(a,b,termsToCalc,additions):
    termsToCalc-=1
    if termsToCalc <= 0:
        return a+b, additions + 1
    return fib(b,a+b,termsToCalc,additions+1)

def fibWrapper(k):
    if k <= 2:
        if k < 2:
            return 0, 0
        return 1, 0
    return fib(0,1,k-1,0)

def euclidGCD(m,n):
    mods = 0
    if n > m:
        m,n = n,m
    while n != 0:
        m,n = n,m % n
        mods += 1
    return m, mods

def euclidGCDWrapper(k):
    m,n = fibWrapper(k+1)[0], fibWrapper(k)[0]
    print("Fib("+str(k)+") is",n)
    print("Greatest Common Denominator between",m,"and",n,"is",euclidGCD(m,n)[0])
    return ""

def euclidGCDSPWrapper(k):
    m,n = fibWrapper(k+1)[0], fibWrapper(k)[0]
    return euclidGCD(m,n)[1]

def fibSPWrapper(k):
    return fibSPWrapper(k)[1]
#UserTestingMode.Task(0,"1a","Recursive fibonacci",["kth term of sequence to compute"],[int],fibWrapper)
UserTestingMode.Task(0,"1","Euclid's Algorithm & Fibonacci's Sequence",["kth term of fibonacci sequence to use"],[int],euclidGCDWrapper)
ScatterplotMode.Task(0,"1","Basic Operations Used in Finding GCD(m,n)","ith Element of Fibonacci Sequence","Basic Operations",range(2,100),[""],[euclidGCDSPWrapper])