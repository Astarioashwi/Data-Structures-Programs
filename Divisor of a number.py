#Finding the all divisor of a number 
#Time complexity = Theta(n)
#Auxiliary Space = Theta(1) 

'''
#naive approach
def divisor(n):
    for i in range (1, n+1):
        if n % i == 0:
            print(i)
        
n = int(input("Enter the number: "))
divisor(n)

'''
'''
#efficient approach
def printDivisor(n):
    i = 1

    while(i * i <=n):
        if(n%i ==0):
            print(i)
            if(i!=n/i):
                print(n/i)
        i +=1

n = int(input("Enter the number: "))
printDivisor(n)
'''

#Time complexity = Theta(sqrt(n))
#Super efficient approach
def printDivisor(n):

    i = 1

    while(i * i < n):
        if(n % i == 0):
            print(i)
        i +=1

    while(i >= 1):
        if(n % i == 0):
            print(n/i)
        i -=1

n = int(input("Enter the number: "))
printDivisor(n)

