# Efficient method LCM of two numbers
# Time complexity Big O (log (min(a,b)))

def gcd(a,b):

    if b == 0:
        return a
    
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a,b)

if __name__ == '__main__':

    userInput_1 = int(input("Enter first number: "))
    userInput_2 = int(input("Enter second number: "))

    print(lcm(userInput_1, userInput_2))