# Program to find the average of the List
def average(l):
    sum = 0
    num = 0

    for x in l:
        sum = sum + x
        num = num + 1
    
    return (sum/num)


l = [10,20,30,40,50]
print(average(l))


"""
#Program with inbuilt functions

def average(l):
    return (sum(l)/len(l))

l = [1570,9560,37890,1680,83450]
print(average(l))
"""
