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
    currentDir = os.getcwd()
    #print(currentDir)
    pathToGo = currentDir + r'\Project01\Project01a\smallSet' #MAC AND LINUX NO SUPPORT HERE
    #print(pathToGo)
    os.chdir(pathToGo)
    directory = os.getcwd()
    #print(currentDir)
    #print("Location of the directory to Sort:")
    #directory = input()

    print("Size of list to sort (10 - 100 increments of 10):")
    sizeOfList = input()
    ErrorCheck = sizeOfList
    ErrorCheck = int(ErrorCheck) #Note I hate how everything isnt local
    if ErrorCheck % 10 != 0:
        print("Not increment of 10!")
        exit()
    
    #os.chdir(directory)
    for file in os.listdir():
        #print(file)
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

elif (mode == "scatter" or mode == "Scatter"):
    plt.title("Sorting")
    plt.xlabel("Size of n")
    plt.ylabel("Number of Comparisons")
    currentDir = os.getcwd()
    pathToGo = currentDir + r'\Project01\Project01a\testSet' #MAC AND LINUX NO SUPPORT HERE
    os.chdir(pathToGo)
    currentDir = os.getcwd()
    for file in os.listdir():
        if file.endswith('0.txt'): #all random files end ----0.txt
            # Create the filepath of particular file
            filePathString = f"{currentDir}/{file}"
            print(filePathString)
            
            A = read_files(filePathString)
            plt.plot(A[0][0], A[0][1], 'r^', alpha=0.75) #selection
            plt.plot(A[1][0], A[1][1], 'bo', alpha=0.75) #insertion
    plt.show()
    plt.clf()
    for file in os.listdir():
        if file.endswith('_rSorted.txt'):
            # Create the filepath of particular file
            filePathString = f"{currentDir}/{file}"
            print(filePathString)
            B = read_files(filePathString)
            plt.plot(B[0][0], B[0][1], 'r^', alpha=0.75) #selection
            plt.plot(B[1][0], B[1][1], 'bo', alpha=0.75) #insertion
    plt.show()
    plt.clf()            
    for file in os.listdir():
        if file.endswith('_sorted.txt'): #all random files end ----0.txt
            # Create the filepath of particular file
            filePathString = f"{currentDir}/{file}"
            print(filePathString)
            
            C = read_files(filePathString)
            plt.plot(C[0][0], C[0][1], 'r^', alpha=0.75) #selection
            plt.plot(C[1][0], C[1][1], 'bo', alpha=0.75) #insertion
    plt.show()
    



#dataTest1 = [88754, 77404, 68789, 62983, 61655, 44960, 44478, 38650, 13648, 8671]
#dataTest2 = [88754, 77404, 68789, 62983, 61655, 44960, 44478, 38650, 13648, 8671]
#print(selectionSort(dataTest1))
#print(insertionSort(dataTest2))