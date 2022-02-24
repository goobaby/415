from numpy import intc
import UserTestingMode
import ScatterplotMode
from TaskOne import euclidGCD

def intGCDCheck(m,n):
    mods = 0
    if n > m:
        n,m = m,n
    for i in range(n,2,-1):
        mods += 2
        if i%n==0 and i%m==0:
            return i, mods
    return 1, mods

def taskDos(n):
    intCheckSum = 0
    euclidSum = 0
    for i in range(1,n+1):
        euclidSum += euclidGCD(n,i)[1]
        intCheckSum += intGCDCheck(n,i)[1]
    return euclidSum/float(n),intCheckSum/float(n)

def taskDosEuclid(n):
    euclidSum = 0
    for i in range(1,n+1):
        euclidSum += euclidGCD(n,i)[1]
    return euclidSum/float(n)

def taskDosInt(n):
    intCheckSum = 0
    for i in range(1,n+1):
        intCheckSum += intGCDCheck(n,i)[1]
    return intCheckSum/float(n)

UserTestingMode.Task(1,"2","MDavg and Davg for some n",["maximum number to test up to"],[int],taskDos)
ScatterplotMode.Task(1,"2","MDavg and Davg Comparison","Average up to n","Basic Operations",range(2,1000,4),["Euclid's Algorithm","Brute Force"], [taskDosEuclid,taskDosInt])