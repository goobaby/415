#import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')
#import numpy as np

#x = np.linspace(0, 10, 30)
#y = np.sin(x)

#plt.plot(x, y, 'o', color='black');
#plt.show() 

#Task Two Expontiation
# i) Decrease by one

def decreaseByOne(a,n):
    if n == 0:
        return 1
    if n > 0:
        return a * decreaseByOne(a, n-1)

# i)

def decreaseByConstantFactor(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return decreaseByConstantFactor(a, n/2) * decreaseByConstantFactor(a, n/2)
    if n % 2 == 1:
        return a * (decreaseByConstantFactor(a,(n-1)/2) * decreaseByConstantFactor(a,(n-1)/2))


print(decreaseByConstantFactor(2, 4))