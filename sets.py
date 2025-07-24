set1 = {10,'jenny','True',1,0,'False',True,False}
print(set1)
print(type(set1))
set2 = set()
print(type(set2))

set1.add(99)
print(set1)
print(len(set1))
set1.remove(10)
#keyError - value to be removed is not in the set

set1.discard(20)
print(set1)

set1.pop()
#set1.clear()
print(set1)

set1.add((23,23,12,21))
print(set1)