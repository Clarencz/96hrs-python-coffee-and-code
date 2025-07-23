tuple= (10,)
print(type(tuple))

tuple2= (12,2,4,5)
print(tuple2)

tuple3 = (10,"jenny",True,34.23)
print(tuple3)
print(tuple3[2])
print(tuple2[1:3])
print(len(tuple2))

tuple4 = (tuple2,tuple3)
print(tuple4)
print(tuple4[1])
tuple5 = tuple2 + tuple3
print(tuple5)