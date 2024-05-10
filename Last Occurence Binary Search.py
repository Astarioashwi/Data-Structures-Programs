# Last Occurence Binary Search Efficient method

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

print(lastOccurence(l, x, 0, len(l) - 1))