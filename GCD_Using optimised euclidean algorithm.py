# Finding greatest common factor
# OPTIMISED EUCLIDEAN ALGORITHM


def gcd(a, b):

    if b == 0:
        return a
    
    return gcd(b, a % b)

    
if __name__ == '__main__':

    userInput_1 = int(input("Enter first number: "))
    userInput_2 = int(input("Enter second number: "))

    print(gcd(userInput_1, userInput_2))