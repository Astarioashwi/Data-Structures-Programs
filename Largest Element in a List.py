#Largest Element in a List

"""
#Inbuild function
y = [1,2,3,4,5,5,6,7,8,9,6,7,8,9]
print(max(y))
"""

"""
#Normal Method
def getMax(l):
    for x in l:
        for y in l:
            if y > x:
                break
        else:
            return x
    return None

l = [1,2,3,4,5,7,8,9]
print(getMax(l))


"""
#Efficient Method
def getMax(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1, len(l)):
            if l[i] > res:
                res = l[i]
        return res
            

y = [1,2,3,4,5,5,6,7,8,9,6,7,8,9]
print(getMax(y))

