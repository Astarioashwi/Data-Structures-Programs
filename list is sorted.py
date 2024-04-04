#Program to check if the list is sorted

"""
def getsorted(l):
    count = 0

    if len(l) <= 1:
        return True
    
    lar = l[0]
    for x in l[1:]:
        count +=1

        if x < lar:
            return False
        
        else:
            lar = x
            if count == len(l)-1:
                return True
            
        
    
    
y = [10, 5,2]
print(getsorted(y))
"""

"""
#Program 2
def getsorted(l):
    i=1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i = i+1
    return True

l = [10, 15, 22]
if getsorted(l):
    print("Yes")
else:
    print("No")

"""

def getsorted(l):
    
    sl = sorted(l)
    if sl == l:
        return True
    else: 
        return False

l = [10, 15, 22]
if getsorted(l):
    print("Yes")
else:
    print("No")