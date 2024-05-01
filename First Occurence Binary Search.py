#Recursive Binary Search

def firstOccurence(l, x, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if x > l[mid]:
        return firstOccurence(l, x, mid + 1, high)
    
    elif x < l[mid]:
        return firstOccurence(l, x, low, mid-1)
    
    else:
        if mid == 0 or l[mid -1] != l[mid]:
            return mid
        
        else:
            firstOccurence(l, x, low, mid-1)

l = [10, 20, 30, 40, 50, 60, 70]
x = 70

print(firstOccurence(l, x, 0, len(l) - 1))