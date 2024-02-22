# Prime checking
# Time complexity in worst case Big O(n)
'''
def isPrime(n):
    if n == 1:
        return False
    
    for i in range (2, n):

        if n % i == 0:
            return False
    
    return True

if __name__ == '__main__':

    userInput_1 = int(input("Enter first number: "))
    
    if isPrime(userInput_1) == True:
        print("True") 

    elif isPrime(userInput_1) == False:
        print("False") 
'''
#Efficient method
# Time complexity in worst case Big O(sqrt(n))

'''
def isPrime(n):
    if n == 1:
        return False
    
    i=2
    
    while(i * i <= n):

        if n % i == 0:
            return False
        
        i+=1
    
    return True

if __name__ == '__main__':

    userInput_1 = int(input("Enter first number: "))
    
    if isPrime(userInput_1) == True:
        print("True") 

    else:
        print("False") 
'''
#Super Efficient method
# Time complexity in worst case Big O(sqrt(n))
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

if __name__ == '__main__':
    
    userInput_1 = int(input("Enter first number: "))
    
    if isPrime(userInput_1) == True:
        print("True") 

    else:
        print("False") 