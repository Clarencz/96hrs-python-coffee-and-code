import random
import string
import timeit


# symbols = int(input("how many symbols do you like in your password? "))
# numbers = int(input("how many numbers do you like in your password? "))
# letters = int(input("how many letters do you like in your password? "))


numbers_list = list(range(10))

# using ascii values to generate letters
# letters_list =[[chr(code) for code in range(ord('a'), ord('z') + 1)] + [chr(code) for code in range(ord('A'), ord('Z') + 1)]]
letters_list = list(string.ascii_letters)

# string.ascii_lowercase
# time1 = timeit.timeit("list(string.ascii_letters)", setup="import string", number=10000)

# # chr + range
# time2 = timeit.timeit("[chr(i) for i in range(97, 123)] + [chr(i)for i in range(65, 91)]", number=10000)

symbols_list = list(string.punctuation)
#using ascii values to generate symbols
# symbols_list1 = [chr(i)for i in range(33, 127)]
# print(time1)
# print(time2)
# print(letters_list)
# print(symbols_list1)