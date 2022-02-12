import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import matplotlib.patches as mpatches

def setupLegend(title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    redlegend = mpatches.Patch(color='red', label='Divide And Conquer')
    bluelegend = mpatches.Patch(color='blue', label='Decrease By Constant Factor')
    greenlegend = mpatches.Patch(color='green', label='Decrease By One')
    plt.legend(handles=[redlegend, bluelegend, greenlegend])


#Task Two Expontiation
# i) Decrease by one

def decreaseByOne(a,n,x):
    if n == 0:
        return (1, 1)
    if n > 0:
        tuple = decreaseByOne(a, n-1, x+1)
        return (a * tuple[0], tuple[1] + 1)

# ii)

def decreaseByConstantFactor(a, n, x):
    if n == 0:
        return (1, 1)
    if n % 2 == 0:
        tuple = decreaseByConstantFactor(a, n/2, x+1)
        return (tuple[0]**2, tuple[1]) #idk if multiplication counts for exponents
    if n % 2 == 1:
        tuple = decreaseByConstantFactor(a, (n-1)/2, x+1)
        return (a * tuple[0]**2, tuple[1] + 1)
    
# iii)

def divideAndConquer(a, n, x):
    if n == 0:
            return (1, 1)
    if n % 2 == 0:
        tuple = decreaseByConstantFactor(a, n/2, x+1)
        return (tuple[0] * tuple[0], tuple[1]+1)
    if n % 2 == 1:
        tuple = decreaseByConstantFactor(a,(n-1)/2, x+1)
        return (a * tuple[0] * tuple[0], tuple[1]+2)

n = 100
base = 2
counter = 0

print("Type User or Scatter for mode:")
mode = input()

if mode == "user" or mode == "User":
    print("Give value of 'a' ie(base of exponent)")
    a = input()
    print("Give value of 'n' ie(the exponent)")
    n = input()
    one = decreaseByOne(int(a), int(n), 0)
    factor = decreaseByConstantFactor(int(a), int(n), 0)
    conquer = divideAndConquer(int(a), int(n), 0)
    
    print("Decrease By One:" + str(one[0]))
    print("Decrease By Constant Factor:" + str(factor[0]))
    print("Divide And Conquer:" + str(conquer[0]))



#alpha is to deal with overlaping issue
#either make seperate graphs or do this
if mode == "scatter" or mode == "Scatter":
    for arg in list(range(n)):
        plt.plot(arg, decreaseByOne(base, arg, counter)[1], 'gs', alpha=0.75)
        plt.plot(arg, decreaseByConstantFactor(base, arg, counter)[1], 'bo', alpha=0.75)
        plt.plot(arg, divideAndConquer(base, arg, counter)[1], 'r^', alpha=0.75)

    setupLegend("Exponentiation","Exponent Value","Number of Muliplications")
    
    #plt.legend(loc="lower right")
    #plt.scatter(one)
    #plt.scatter(factor)
    #plt.scatter(conquer)
    plt.show()
#print(one)
#print(factor)
#print(conquer)

# x = n