#Program for left rotation

def LeftRotate(l, n):

    first_digit = l[0]
    for i in range (1,n):
        l[i-1] = l[i]

    l[n-1] =  first_digit       
    
    return l

y = [10,20,30,40,50]
LeftRotate(y, len(y))
print(y)


"""
#Using direst method 1 slicing
y = [10,20,30,40,50]
y = y[1:] + y[0:1]
print(y)



#Using direst method 2 poop and append
y = [10,20,30,40,50]
x = y.pop(0)
print(y)
y.append(x)
print(y)
"""