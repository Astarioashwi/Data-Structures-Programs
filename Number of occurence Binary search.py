# Number of occurence

def totalOccurence(l, x, low, high):
    first = firstOccurence(l, x, low, high)
    if first == -1:
        return 0
    else:
        return lastOccurence(l, x, low, high) - first + 1

def firstOccurence(l, x, low, high):
    
    while(low <= high):

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

def lastOccurence(l, x, low, high):
    
    while(low <= high):

        mid = (low + high) // 2
    
        if x > l[mid]:
            low = mid + 1
    
        elif x < l[mid]:
            high = mid -1
    
        else:
            if mid == len(l)-1 or l[mid] != l[mid + 1]:
                return mid
        
            else:
                low = mid + 1

l = [10, 20, 30, 40, 50, 60, 60, 70]
x = 60

print(totalOccurence(l, x, 0, len(l) - 1))