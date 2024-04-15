#Program to find the second largest number
"""
#Time complexity Theta(n)

def secondLargest(l):
    if len(l) <=1:
        return None
    
    lar = getmax(l)
    slar = None
    for x in l:
        if x!=lar:
            if slar == None:
                slar = x
            elif x > slar:
                #slar = max(slar, x)
                slar = x
    return slar
    
def getmax(l):
    res = l[0]
    for i in range(1, len(l)):
        if l[i] > res:
            res = l[i]
    return res

y = [1,2,3,4,5]
print(secondLargest(y))
"""

"""
#Reduced step
def secondLargest(l):
    res = l[0]
    slarg = l[0]
    for i in range(1, len(l)):
        if l[i] > res:
            slarg = res
            res = l[i]

    return slarg

y = [1,2,3,4,5]
print(secondLargest(y))
"""

def getsecmax(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None
    for x in l[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or slar < x:
                slar = x
    return slar
    
y = [1,1,5,3]
print(getsecmax(y))