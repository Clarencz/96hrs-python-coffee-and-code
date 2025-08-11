dict1 = {'a':1,'b':7}
dict2 = {'b':4, 'c':8}

# =====method 1======
# dict1.update(dict2)
# print(dict1)

# =====method 2 =======
# dict3 = {**dict1,**dict2}
# print(dict3)

# =======method 3========
dict3 = dict1 | dict2
print(dict3)