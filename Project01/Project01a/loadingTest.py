import time
import sys


def setupToolbar():
    # setup toolbar
    sys.stdout.write("[%s" % (" " * 4))
    sys.stdout.flush()
    sys.stdout.write("\b" * (4+1)) # return to start of line, after '['

amountOfFiles = 1000
setupToolbar()

percentage = 0
counter100 = 0
print("Loading " + str(amountOfFiles) + " files...")


for i in range(amountOfFiles):
    time.sleep(0.1) # do real work here
    # update the bar
    a = 0
    a += 1
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
sys.stdout.write("\n") # this ends the progress bar
print("end")

#sys.stdout.write("[%s]" % (" " * amountOfFiles))
#sys.stdout.flush()
#sys.stdout.write("\b" * (amountOfFiles+1))
#for i in range(amountOfFiles):
    #time.sleep(0.1) # do real work here
    # update the bar
    #sys.stdout.write("-")
    #sys.stdout.flush()

#sys.stdout.write("]\n") # this ends the progress bar