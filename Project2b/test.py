from numpy import exp
from math import log
import timeit


def karatsuba(num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return '0'
        
        ans = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                ans[i1+i2] += digit
                ans[i1+i2+1] += ans[i1+i2]//10
                ans[i1+i2] = ans[i1+i2]%10
                
        ans, beg = ans[::-1],0
        
        while beg < len(ans) and ans[beg]==0:
            beg += 1
            
        ans = map(str, ans[beg:])
        return "".join(ans)
    
def exponent(a, n, x):
    if n == 0:
        return (1, 1)
    if n % 2 == 0:
        tuple = exponent(a, n/2, x+1)
        return (karatsuba(tuple[0], tuple[0]), tuple[1] + 1)
    if n % 2 == 1:
        tuple = exponent(a, (n-1)/2, x+1)
        return (karatsuba(a, karatsuba(tuple[0], tuple[0])), tuple[1] + 2)
    
def multiply(num1, num2):
    m,n=len(num1)-1,len(num2)-1
    c1,c2,s=1,1,0
    for i in range(0,len(num1)):
        c2=1
        for j in range(0,len(num2)):
            s+=int(num1[m-i])*int(num2[n-j])*c1*c2
            c2*=10
        c1*=10
    return str(s)

def main(vers):
    while(vers != "Quit"):
        if(vers == "Task 1"):
            print("Karatsuba Multiplication Selected!")
            print("What is Input One?")
            x = input()
            print("What is Input Two?")
            y = input()
            print("Karatsuba:", karatsuba(x,y))
        elif(vers == "Task 2"):
            print("Exponentation Selected!")
            print("What is Input One?")
            a = input()
            print("What is Input Two?")
            n = input()
            print("Exponent:", str(exponent(int(a),int(n),0)[0]))
        elif(vers == "Extra Credit"):
            print("Extra Credit Selected!")
            print("What is Input One?")
            c = input()
            print("What is Input Two?")
            d = input()
            print("Extra Credit:", multiply(c, d))
        print("Please select what Task: Task 1; Task 2; Extra Credit; Quit")
        vers =  input()
    exit()

print("Please select what Task: Task 1; Task 2; Extra Credit; Quit")
vers =  input()
main(vers)