# Finding greatest common factor
# EUCLIDEAN ALGORITHM

def gcd(a, b):

    while a != b:

        if a > b:
            a = a - b

        else:
            b = b - a

    return a
    
if __name__ == '__main__':
    userInput_1 = int(input("Enter first number: "))
    userInput_2 = int(input("Enter second number: "))

    print(gcd(userInput_1, userInput_2))

