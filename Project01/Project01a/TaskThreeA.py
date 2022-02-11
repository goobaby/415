import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

print("File to Sort:")
file = input()
datafile = open(file, "r")
#idk if file has bad open exceptions

def selectionSort(data):
    
    comp = 0
    for i in range(len(data)):
        min = i
        for j in range(i+1, len(data)):
            if(data[j]<data[min]):
                min = j
                comp = comp + 1
    return comp

def insertionSort(data):
    comp = 0
    for i in range(1, len(data)):
        find = data[i]
        
        j = i - 1
        while j >= 0 and find < data[j]:
            data[j+1] = data[j]
            j -= 1
            comp = comp + 1
        data[j+1] = find
    return comp
