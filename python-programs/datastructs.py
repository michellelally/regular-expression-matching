i = 1
f = 1.0
s = "string"
l = [1, 2, 3, 4, 5]

print(l[-1])
print(l)

print(l[3])

l = [i * i for i in l]
print(l)
print(l[2:])
print(l[::-1])
print(len(l))
print(range(10))

list(range(20))

l = [i**2  for i in range(10)]
print(l)

basket = {"apple", "banana", "orange", "pear"}
"apple" in basket

dobs = {"Tim": "01-01-2000", "Jack": "02-02-2002", "John": "03-03-2003"}
print(dobs)
print(dobs["Tim"])

