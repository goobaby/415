import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

#x = np.linspace(0, 10, 6)
#y = np.sin(x)

#plt.plot(x, y, 'o', color='black');
#plt.show() 

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

n = 10
base = 2
counter = 0

#one = decreaseByOne(2, 4, 0)
#factor = decreaseByConstantFactor(2, 4, 0)
#conquer = divideAndConquer(2, 4, 0)

#alpha is to deal with overlaping issue
#either make seperate graphs or do this
for arg in list(range(n)):
    plt.plot(arg, decreaseByOne(base, arg, counter)[1], 'gs', alpha=0.75)
    plt.plot(arg, decreaseByConstantFactor(base, arg, counter)[1], 'bo', alpha=0.75)
    plt.plot(arg, divideAndConquer(base, arg, counter)[1], 'r^', alpha=0.75)

plt.title("Exponentiation")
plt.xlabel("Exponent Value")
plt.ylabel("Number of Muliplications")
#plt.legend(loc="lower right")
#plt.scatter(one)
#plt.scatter(factor)
#plt.scatter(conquer)
plt.show()
#print(one)
#print(factor)
#print(conquer)

# x = n