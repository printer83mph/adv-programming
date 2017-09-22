d1 = {0:10, 1:20}
d1[2] = 30
print d1

d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
for i in d2:
    d1[i] = d2[i]
print d1

d1 = {2:20, 1:10, 3:30}
print(3 in d1)
print(4 in d1)

for i in d1:
    print d1[i]

l1 = []
for i in d1:
    l1.append(d1[i])
l1.sort()
print l1

d1 = {}
for i in range(1,16):
    d1[i] = i**2
print d1
