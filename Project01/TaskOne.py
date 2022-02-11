from UserTestingMode import Task

def fib(a,b,termsToCalc):
    termsToCalc-=1
    if termsToCalc == 0:
        return a+b
    return fib(b,a+b,termsToCalc)

def A(termsToCalc):
    termsToCalc-=1
    if termsToCalc == 0:
        return 1
    return 2+A(termsToCalc)

def fibWrapper(k):
    if k == 1:
        return 0
    return fib(0,1,k-2)

Task(0,"1b","Recursive fibonacci",["kth term of sequence to compute"],[int],fibWrapper)