# Last Occurence Binary Search Naive method

def lastOccurence(l, x):
    
    for i in reversed(range(len(l))):
        if l[i] == x:
            return i
    
    return -1

l = [10, 20, 30, 40, 50, 60, 60, 70]
x = 60

print(lastOccurence(l, x))