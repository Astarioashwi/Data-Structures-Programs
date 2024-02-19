# LCM of two numbers
# Time complexity Theta(a*b - max(a,b))

def lcm(a, b):

    res = max(a,b)

    while True:

        if res % a == 0 and res % b == 0:
            return res
        
        res +=1


if __name__ == '__main__':

    userInput_1 = int(input("Enter first number: "))
    userInput_2 = int(input("Enter second number: "))

    print(lcm(userInput_1, userInput_2))