#Naive method for first index occurence in a sorted array

def firstOccur(l, n, x):
    for i in range(0, n):
        if(l[i]==x):
            return i
        
    return -1

l = [10, 20, 30, 40, 50, 60, 90, 90]
x = 90

print(firstOccur(l,8, x))