# Program for Dictionary Comprehension in python

y = [1,2,3,4,5,5,6,7,8,9,6,7,8,9]
d1 = {x: x**3 for x in y}
print(d1)

d2 = {x: f"ID{x}" for x in range(5)}
print(d2)

l2 = [101, 103, 102]
l3 = ["gfg", "ide", "courses"]
d3 = {l2[i]:l3[i] for i in range(len(l2))}
print(d3)

d4 = dict(zip(l2, l3))
print(d4)

#Inverting a Dictionary (key becomes value)
# and value becomes key

d5 = d3
d6 = {v:k for (k,v) in d5.items()}
print(d6)
