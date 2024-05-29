#Squareroot efficient way with binary search
def sqrtfloor(x):
    low = 1
    high = x
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        mSq = mid * mid

        if mSq == x:
            return mid
        
        elif mSq > x:
            high = mid - 1

        else:
            low = mid + 1
            ans = mid
    return ans

x = 16
print(sqrtfloor(x))