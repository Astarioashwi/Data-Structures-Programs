#Remove Duplicates
"""
def RemDuplicates(l, n):
    temp = [0] * n
    temp[0] = l[0]
    res = 1

    for i in range (1,n):
        if temp[res-1] != l[i]:
            temp[res] = l[i]
            print(temp[res])
            res += 1
    
    for i in range (0,res):
        l[i] = temp[i]
        print(l[i])

    return res

y = [1,1,2,3,3,5,5]
result_array = RemDuplicates(y, len(y))
print(y[:result_array])

"""

def RemDuplicates(l, n):
    res = 1

    for i in range (1,n):
        if l[res-1] != l[i]:
            l[res] = l[i]
            res += 1
    return res

y = [1,1,2,3,3,5,5]
result_array = RemDuplicates(y, len(y))
print(y[:result_array])

