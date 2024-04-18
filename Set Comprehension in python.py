# Program for Set Comprehension in python

y = [1,2,3,4,5,5,6,7,8,9,6,7,8,9]

l1 = {x for x in y if x %2==0}
l2 = {x for x in y if x %2!=0}
print(l1)
print(l2)

######################################################

y = [1,2,3,4,5,5,6,7,8,9,6,7,8,9]

l3 = [x for x in y if x %2==0]
l4 = [x for x in y if x %2!=0]
print(l3)
print(l4)

######################################################

def getSmaller(l,z):
    return [x for x in l if x < z]

y = [1,2,3,4,5,6,7,8,9]
z = 5
print(getSmaller(y,z))

######################################################

def evenOdd(y):
    even = [x for x in y if x %2==0]
    odd = [x for x in y if x %2!=0]
    return even, odd

y = [1,2,3,4,5,6,7,8,9]
even, odd = evenOdd(y)
print("Odd Number: ", odd)
print("Even Number: ", even)

######################################################

s = "geekforgeeks"
l1 = [x for x in s if x in "aeious"]
print(l1)

######################################################

l2 = ["geeks", "ide", "courses", "gfg"]
l3 = [x for x in l2 if x.startswith("g")]
print(l3)

######################################################

m = int(input("Enter the number: "))
l4 = [x*2 for x in range(m)]
print(l4)

######################################################

l2 = ["geeks", "ide", "courses", "gfg"]
l3 = [x.upper() for x in l2 if x.startswith("g")]
print(l3)

