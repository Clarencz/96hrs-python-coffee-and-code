a = range(5)
print(a[1])

b = range(2,5)
print(b[2])

for i in b:
    print(i)
    
c = range(2,15,2)
for i in c:
    print(i)
    
sum = 0
d = []
for i in range (101):
    d.append(i)
    sum +=i
print(d)
print(sum)