#Sieve of Eratosthenes
# Time complexity in worst case Big O(n * sqrt(n))
'''
def isPrime(n):

    if n==1:
        return False
    
    if n==2 or n==3:
        return True
    
    if n%2==0 or n%3==0:
        return False
    
    i=5

    while(i*i <= n):
        if n%i==0 or n%(i+2)==0:
            return False
        
        i +=6
    return True

def printprime(n):

    for i in range(2, n + 1):
        if isPrime(i):
            print(i, end =" ")

if __name__ == '__main__':
    
    userInput_1 = int(input("Enter first number: "))
    
    printprime(userInput_1)
'''
'''
def sieve(n):
   
    if n <= 1:
       return
   
    isPrime = [True] * (n + 1)

    i = 2

    while i * i <= n:
        if isPrime[i]:
            for j in range(2 * i, n + 1,i):
                isPrime[j] = False

        i += 1

    for i in range(2, n + 1):
        if isPrime[i]:
            print(i, end =" ")


if __name__ == '__main__':
    
    userInput_1 = int(input("Enter first number: "))
    
    sieve(userInput_1)
'''

#Optimized Implementation
#Time Complexity O(n loglog n)
def sieve(n):
   
    if n <= 1:
       return
   
    isPrime = [True] * (n + 1)

    i = 2

    while i <= n:
        if isPrime[i]:
            print(i, end =" ")

            for j in range(i * i, n + 1, i):
                isPrime[j] = False

        i += 1


if __name__ == '__main__':
    
    userInput_1 = int(input("Enter first number: "))
    
    sieve(userInput_1)