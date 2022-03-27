from numpy import add


def main(task):
    #===============Task 1==================
    
    if(task == '1'):
        
        import matplotlib.pyplot as plt
        plt.style.use('seaborn-whitegrid')
        import numpy as np
        import matplotlib.patches as mpatches
        
        def fib(a,b,termsToCalc, additions):
            termsToCalc-=1
            if termsToCalc == 0:
                return a+b, additions+1
            return fib(b,a+b,termsToCalc, additions+1)

        def A(termsToCalc):
            termsToCalc-=1
            if termsToCalc == 0:
                return 1
            return 2+A(termsToCalc)

        def fibWrapper(k):
            if k == 1:
                return 0
            return fib(0,1,k-1, 0)
        
        def GCD(m, n, numMod):
            if m == 0:
                return n, numMod
            return GCD(n%m, m, numMod+1)
        
        #idk whats happening with funct a luke
    
        print("Type User or Scatter for mode:")
        mode = input()

    
        if mode == "user" or mode == "User":
            print("Enter kth fibonacci number")
            k = input()
            print("Value of Fib(k):")
            print(fibWrapper(int(k))[0])
            
            #print("Value of Fib(k+1):")
            #print(fibWrapper(int(k)+1))
            print("Value of GCD(m, n) where m = Fib(k+1) and n = Fib(k):")

            print(GCD( fibWrapper(int(k)+1)[0], fibWrapper(int(k))[0], 0 )[0])
        
        if mode == "scatter" or mode == "Scatter":
            fibNum =  []
            for toFib in range(25):
                #print (toFib)
                if (toFib >= 2):
                    x = toFib
                    y = int(fibWrapper(toFib)[1])
                    plt.plot(x, y, 'gs', alpha=0.75)
                    #print(fibWrapper(toFib))
            plt.xlabel("kth Element of Fibonacci Sequence")
            plt.ylabel("Basic Operations")
            plt.show()
            plt.clf()
            
            for toEuclid in range(25):
                if (toEuclid >= 2):
                    plt.plot(toEuclid, GCD( fibWrapper(int(toEuclid)+1)[0], fibWrapper(int(toEuclid))[0], 0)[1], 'gs', alpha=0.75)
            #print (fibNum)
            plt.xlabel("Values of N")
            plt.ylabel("Number of modulo")
            plt.show()

    #===============Task 2==================
    elif(task == '2'):
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
                return (tuple[0]**2, tuple[1] + 1) #idk if multiplication counts for exponents
            if n % 2 == 1:
                tuple = decreaseByConstantFactor(a, (n-1)/2, x+1)
                return (a * tuple[0]**2, tuple[1] + 2)
            
        # iii)

        def divideAndConquer(a, n, x):
            if n == 0:
                    return (1, 1)
            if n % 2 == 0:
                #tuple = divideAndConquer(a, n/2, x+1)
                tuple1 = divideAndConquer(a, n/2, x+1)
                tuple2 = divideAndConquer(a, n/2, x+1)
                return (tuple1[0] * tuple2[0], tuple1[1]+ tuple2[1] + 1)
            if n % 2 == 1:
                tuple1 = divideAndConquer(a, (n-1)/2, x+1)
                tuple2 = divideAndConquer(a, (n-1)/2, x+1)
                #tuple = divideAndConquer(a,(n-1)/2, x+1)
            return (a * tuple1[0] * tuple2[0], tuple1[1]+ tuple2[1] + 1)

        n = 100
        base = 2
        counter = 0

        print("Type User or Scatter for mode:")
        mode = input()

        if mode == "user" or mode == "User":
            print("Give value of 'a' ie(base of exponent)")
            a = input()
            while(a.isalpha() == True ):
                print("ERROR: a is not a number please enter a again")
                a = input()
            print("Give value of 'n' ie(the exponent)")
            n = input()
            while(n.isalpha() == True ):
                print("ERROR: n is not a number please enter n again")
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

    #===============Task 3==================
    elif(task == '3'):
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
                    comp = comp + 1
                    if(data[j]<data[min]):
                        min = j
                        #comp = comp + 1
                data[i], data[min] = data[min], data[i]        
            return len(data), comp, data

        def insertionSort(data):
            comp = 0
            for i in range(1, len(data)):
                find = data[i]
                
                j = i - 1
                #plus more?
                while j >= 0 and find < data[j]:
                    comp = comp + 1
                    data[j+1] = data[j]
                    j -= 1
                    
                    #comp = comp + 1
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
            #pathToGo = currentDir + r'\smallSet' #MAC AND LINUX NO SUPPORT HERE
            pathToGo = "smallSet"
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
            pathToGo = "testSet" #MAC AND LINUX NO SUPPORT HERE
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
    else:
        print("Not a Task Number!")
        exit()

print("Welcome to Project 01a made by Amit Deb and Luke Demeter-Willison!")
print("Please enter 1 or 2 or 3 for the corresponding task to run")    
task = input()
main(task)

#dataTest1 = [88754, 77404, 68789, 62983, 61655, 44960, 44478, 38650, 13648, 8671]
#dataTest2 = [88754, 77404, 68789, 62983, 61655, 44960, 44478, 38650, 13648, 8671]
#print(selectionSort(dataTest1))
#print(insertionSort(dataTest2))