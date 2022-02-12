import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import os
import sys
        
#fileToOpen = open(file, "r")
#dataList = fileToOpen.read()
#print(dataList)
#fileToOpen.close()
#idk if file has bad open exceptions

def selectionSort(data):
    
    comp = 0
    for i in range(len(data)):
        min = i
        for j in range(i+1, len(data)):
            if(data[j]<data[min]):
                min = j
                comp = comp + 1
        data[i], data[min] = data[min], data[i]        
    return len(data), comp, data

def insertionSort(data):
    comp = 0
    for i in range(1, len(data)):
        find = data[i]
        
        j = i - 1
        #plus more?
        while j >= 0 and find < data[j]:
            data[j+1] = data[j]
            j -= 1
            comp = comp + 1
        data[j+1] = find
    return len(data), comp, data

def read_files(file_path):
    
    with open(file_path, 'r') as file:
        SortArray_String = file.read().splitlines()
        selectionSortArray_Int =  list(map(int, SortArray_String))
        insertionSortArray_Int =  list(map(int, SortArray_String))
        #print(selectionSort(selectionSortArray_Int))
        #print(insertionSort(insertionSortArray_Int))
        return selectionSort(selectionSortArray_Int), insertionSort(insertionSortArray_Int)
 
    file.close()
        
print("Type User or Scatter for mode:")
mode = input()

if (mode == "User" or mode == "user"):
    print("Location of the directory to Sort:")
    directory = input()

    print("Size of list to sort (10 - 100 increments of 10):")
    sizeOfList = input()
    
    os.chdir(directory)
    for file in os.listdir():
        if file.endswith('.txt') and file.find(sizeOfList + ".") != -1:
            #or file.find(sizeOfList + "_") != -1):
            # Create the filepath of particular file
            filePathString = f"{directory}/{file}"
            #print(filePathString)
            
            A = read_files(filePathString)
            print("Selection Sort:")
            print(A[0][2])
            print("Insertion Sort:")
            print(A[1][2])

elif(mode == "test" or mode == "Test"):
    print("Location of the directory to Sort:")
    directory = input()
    print("Size of list to sort (10 - 100 increments of 10):")
    sizeOfList = "10"
    
    os.chdir(directory)
    for file in os.listdir():
        if file.endswith('.txt') and file.find(sizeOfList + ".") != -1:
            #or file.find(sizeOfList + "_") != -1):
            # Create the filepath of particular file
            filePathString = f"{directory}/{file}"
            print(filePathString)
            
            A = read_files(filePathString)
            print("Selection Sort:")
            print(A[0][2])
            print("Insertion Sort:")
            print(A[1][2])




#dataTest1 = [88754, 77404, 68789, 62983, 61655, 44960, 44478, 38650, 13648, 8671]
#dataTest2 = [88754, 77404, 68789, 62983, 61655, 44960, 44478, 38650, 13648, 8671]
#print(selectionSort(dataTest1))
#print(insertionSort(dataTest2))