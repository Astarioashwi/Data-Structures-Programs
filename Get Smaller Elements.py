# Program to Get Smaller Elements
def getSmallerElements(l,y):
    smallElements=[]

    for x in l:
        if y > x:
            smallElements.append(x)
    return smallElements

l=[10, 11, 20, 21, 30, 31, 40, 41]
y = int(input("Enter the number: "))

print("Smaller Elements: ", getSmallerElements(l,y))
