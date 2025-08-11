# numbers = [23,23,12,34,78,123]
# new_list = []

# for number in numbers:
#     if number % 2 == 0:
#         new_list.append(number)
# print(new_list)

# ===list comprehension====

# new_list = [number for number in numbers if number % 2 ==0]
# print(new_list)


# ========example 2 ===========

# numbers = [1,2,3,4,5,6,7,8,9]

# powers_of_inputs = [2**x for x in numbers]
# print(powers_of_inputs)

# ========example 3 ==============

words = ['auto','amber','uncle','fox','car','anger']

words = [word.upper() if word.startswith('a') else word for word in words]
print(words)