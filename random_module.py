import random
 
a = random.randint(1,3)
print(a)

b= random.randrange(1,3)
print(b)

c = random.random()
print(c)

d= random.uniform(1,3)
print(d)

e = [2,34,4.5,2,1]
l= random.choice(e)
random.shuffle(e)
print(l)
print(e)