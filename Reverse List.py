"""
#Program 1
def reverseList(l):
    
    a = list(reversed(l))
    print(a)

l = [1,1,5,3]
reverseList(l)
"""

"""
#Program 2
l = [1,1,5,3]
l.reverse()
print(l)
"""

"""
#Program 3
l = [10, 20, 30]
new = l[::-1]
print(new)
"""

def reverse(l):
    s=0
    e= len(l) - 1

    while s < e:
        l[s], l[e] = l[e], l[s]
        s = s + 1
        e = e - 1

y = [1,1,5,3,7]
reverse(y)
print(y)
