import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plt.style.use('seaborn-whitegrid')
import numpy as np
import os
import sys
import time
        
#fileToOpen = open(file, "r")
#dataList = fileToOpen.read()
#print(dataList)
#fileToOpen.close()
#idk if file has bad open exceptions
def setupToolbar():
    # setup toolbar
    sys.stdout.write("[%s" % (" " * 4))
    sys.stdout.flush()
    sys.stdout.write("\b" * (4+1)) # return to start of line, after '['
    
def setupLegend(title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    redlegend = mpatches.Patch(color='red', label='Selection Sort')
    bluelegend = mpatches.Patch(color='blue', label='Insertion Sort')
    plt.legend(handles=[redlegend, bluelegend])

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
        file.close()
        return selectionSort(selectionSortArray_Int), insertionSort(insertionSortArray_Int)
        
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
        #print(len(os.listdir()))
        if file.endswith('.txt') and file.find(sizeOfList + "_sorted.") != -1:
            #or file.find(sizeOfList + "_") != -1):
            # Create the filepath of particular file
            filePathString = f"{directory}/{file}"
            #print(filePathString)
            
            A = read_files(filePathString)
            print("Selection Sort:")
            print(A[0][2])
            print(A[0][1])
            print("Insertion Sort:")
            print(A[1][2])
            print(A[1][1])            

elif (mode == "scatter" or mode == "Scatter"):

    #getting directory from local machine
    currentDir = os.getcwd()
    pathToGo = currentDir + r'\Project01\Project01a\testSet' #MAC AND LINUX NO SUPPORT HERE
    os.chdir(pathToGo)
    currentDir = os.getcwd()
    
    #-------------------------------------------------------------------------------
    setupToolbar()
    
    percentage = 0
    counter100 = 0
    amountOfFiles= len(os.listdir())
    
    print("Loading " + str(amountOfFiles) + " files...")
    
    for file in os.listdir():
        time.sleep(0.1)
        if file.endswith('0.txt'): #all random files end ----0.txt
            # Create the filepath of particular file
            filePathString = f"{currentDir}/{file}"
            #print(filePathString)
            
            A = read_files(filePathString)
            plt.plot(A[0][0], A[0][1], 'r^', alpha=0.75) #selection
            plt.plot(A[1][0], A[1][1], 'bo', alpha=0.75) #insertion
            
        counter100 += 1
        percentage += (1/amountOfFiles)*100
        percentage = round(percentage,2)
        if counter100 == amountOfFiles:
            sys.stdout.write("\r[" + "100.0" + "%] \nLoaded!")
        elif percentage < 1:
            continue
        elif(percentage == 1):
            sys.stdout.write(str(percentage) + "%]")
        elif(percentage<100):
            sys.stdout.write("\r[" + str(percentage) + "%]")#\b\b\b\b\b\b\b
        else:
            sys.stdout.write("\r[" + "100" + "%]")
        sys.stdout.flush()

    
    #setting up legend
    setupLegend("Sorting(Average case)","Size of n","Number of Comparisons")
    
    sys.stdout.write("]\n")
    plt.show()
    plt.clf()
    
    #------------------------------------------------------------------------------------
    
    setupToolbar()
    
    percentage = 0
    counter100 = 0
    
    print("Loading " + str(amountOfFiles) + " files...")
    
    for file in os.listdir():
        time.sleep(0.1)
        if file.endswith('_rSorted.txt'):
            # Create the filepath of particular file
            filePathString = f"{currentDir}/{file}"
            #print(filePathString)
            B = read_files(filePathString)
            plt.plot(B[0][0], B[0][1], 'r^', alpha=0.75) #selection
            plt.plot(B[1][0], B[1][1], 'bo', alpha=0.75) #insertion

        counter100 += 1
        percentage += (1/amountOfFiles)*100
        percentage = round(percentage,2)
        if counter100 == amountOfFiles:
            sys.stdout.write("\r[" + "100.0" + "%] \nLoaded!")
        elif percentage < 1:
            continue
        elif(percentage == 1):
            sys.stdout.write(str(percentage) + "%]")
        elif(percentage<100):
            sys.stdout.write("\r[" + str(percentage) + "%]")#\b\b\b\b\b\b\b
        else:
            sys.stdout.write("\r[" + "100" + "%]")
        sys.stdout.flush() 
    
    setupLegend("Sorting(Worst case)","Size of n","Number of Comparisons")
       
    sys.stdout.write("]\n")
    plt.show()
    plt.clf()
    
    #-----------------------------------------------------------------------
    setupToolbar()
    
    percentage = 0
    counter100 = 0
    
    print("Loading " + str(amountOfFiles) + " files...")
    
    for file in os.listdir():
        time.sleep(0.1)
        
        if file.endswith('_sorted.txt'): #all random files end ----0.txt
            # Create the filepath of particular file
            filePathString = f"{currentDir}/{file}"
            #print(filePathString)
            
            C = read_files(filePathString)
            plt.plot(C[0][0], C[0][1], 'r^', alpha=0.75) #selection
            plt.plot(C[1][0], C[1][1], 'bo', alpha=0.75) #insertion
            
        counter100 += 1
        percentage += (1/amountOfFiles)*100
        percentage = round(percentage,2)
        if counter100 == amountOfFiles:
            sys.stdout.write("\r[" + "100.0" + "%] \nLoaded!")
        elif percentage < 1:
            continue
        elif(percentage == 1):
            sys.stdout.write(str(percentage) + "%]")
        elif(percentage<100):
            sys.stdout.write("\r[" + str(percentage) + "%]")#\b\b\b\b\b\b\b
        else:
            sys.stdout.write("\r[" + "100" + "%]")
        sys.stdout.flush()
    
    setupLegend("Sorting(Best case)","Size of n","Number of Comparisons")
    
    sys.stdout.write("]\n")
    plt.show()
    



#dataTest1 = [88754, 77404, 68789, 62983, 61655, 44960, 44478, 38650, 13648, 8671]
#dataTest2 = [88754, 77404, 68789, 62983, 61655, 44960, 44478, 38650, 13648, 8671]
#print(selectionSort(dataTest1))
#print(insertionSort(dataTest2))