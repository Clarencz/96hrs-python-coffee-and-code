# my_square = lambda x: x*x
# print(my_square(3))

# my_sum = lambda x,y :x+y
# print(my_sum(3,2))

# my_sum2 = lambda *args : sum(args)
# print(my_sum2(3,4,5,2,1))

# ======example 1=======

# number = [2,4,2,1,56,6,3,2,12,52]

# even_numbers = list(filter(lambda x: x%2 ==0 ,number))
# print(even_numbers)

# ======example 2 ===========
# numbers = [8,343,34,656,67,76,89,34]

# squared_numbers = list(map(lambda x : x/3, numbers))
# print(squared_numbers)

# =======example 3 ============
def myfunction(num):
    return lambda x : x * num

ten_multiplier = myfunction(10)
print(ten_multiplier(54))