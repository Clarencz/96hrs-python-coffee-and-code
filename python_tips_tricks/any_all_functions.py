# x = [True,False,False,False]
# print(any(x))
# print(all(x))

numbers = [1,2,34,62,1,34,54,65]

even =lambda x : x%2 ==0

result = [even(number) for number in numbers]
if any(result):
    print("at least one number is even")
else:
    print("no number is even")
if all(result):
    print("all numbers are even")