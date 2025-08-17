set1={1,2,3,4,5,7,5,6}
set2={1,2,3,5,6,6,7,4}
print(set1.issubset(set2)) #print(set <=set2)

set3={3,5,6,7}
set4={4,5,6}
print(set3.isdisjoint(set4))

set5={10,11,12,13,14}
set6={11,12,13,14}
print(set5.issuperset(set6))

set2.clear()
print(set2)

del set1#deletes everything including the name set1