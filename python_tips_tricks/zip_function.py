# names = ['john','anna','joy']
# ages = [34,23,65]

# for i in range(len(names)):
#     print(f"{names[i]} {ages[i]}")

# for name,age in zip(names,ages):
#     print(name,age)

# ======example 2 =========
    
# sales = [200,300,400,900]
# costs = [150,340,232,543]

# for sale,cost in zip(sales,costs):
#     print(sale-cost)

# =========example 3 ===========

zipped = [('mike',23),('anna',20),('yugo',25)]
# names=[]
# age=[]

# for i in range(len(zipped)):
#     names.append(zipped[i][0])
#     age.append(zipped[i][1])
# print(names)
# print(age)

# name,age = zip(*zipped) #unzipping
# print(name)
# print(age)

# ========example 4 ==========
# letters = ['b','d','a','c']
# numbers = [3,2,4,1]

# data = sorted(zip(letters,numbers))
# print(data)

# ==========example 5===========
#turning two lists into a dictionary
letters = ['b','d','a','c']
numbers = [3,2,4,1]

mydict = dict(zip(letters,numbers))
print(mydict)
