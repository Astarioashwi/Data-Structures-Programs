# Program to Slicing (List, Tuple and String)

l=[10, 11, 20, 21, 30, 31, 40, 41]

print(l[0:5:2])
print(l[:4])
print(l[2:])
print(l[-1:-6:-1])
print(l[ : :-1])

l1 = [10, 31, 40, 41]
l2 = l1[:]

t1 = (10,20,30)
t2 = t1[:]

s1 = "greeks"
s2 = s1[:]

print(l1 in l2)
print(t1 in t2)
print(s1 in s2)
