# Factorial of a number

# With this method time complexity "T(n) = Theta(n)"
"""
def fact(num):
    result = 1

    for i in range (1, num + 1):
        result = i * result
    
    return result

if __name__ == '__main__':
    userInput = int(input("Enter a number: "))
    print(fact(userInput))

"""
# Alternate method with time complexity "T(n) = T(n-1) + Theta(1)"

def fact(num):
    result = 1

    if num == 0:
        return 1
    
    return num * fact(num-1)

if __name__ == '__main__':
    userInput = int(input("Enter a number: "))
    print(fact(userInput))
