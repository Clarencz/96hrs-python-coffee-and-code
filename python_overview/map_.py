numbers = [2,3,4,5,634,23,11,34,54]

def divide(x):
    return x / 2

# new_list = [divide(i) for i in numbers]
# print(new_list)

new_list = map(divide, numbers)
print(list(new_list))