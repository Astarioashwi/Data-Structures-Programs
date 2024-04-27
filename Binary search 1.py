#Binary search

def bsearch(l,x):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high)//2

        if l[mid] == x:
            return mid
        
        elif l[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
            
    return -1


l = [10, 20, 30, 40, 50, 60, 90, 90]
x = 90

print(bsearch(l, x))