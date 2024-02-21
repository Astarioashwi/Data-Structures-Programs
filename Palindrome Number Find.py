# Palindrome Number Find

def isPal(n):
 
    rev = 0
    temp = n

    while temp != 0:
      
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10

    return rev == n


number = int(input("Enter the number: "))

if number == 0:
        print("Zero is the input and it is a Palindrome")

elif number != 0:

    if(isPal(number)) == True:
        print("The entered number is a Palindrome")

    if(isPal(number)) == False:
        print("The entered number is NOT a Palindrome")


         