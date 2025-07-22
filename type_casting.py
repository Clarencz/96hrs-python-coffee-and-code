# print(len("12345"))
# print(len("jenny lectures"))

#print(len(12334)) -typeError

length = len("jennny lectures")
# print("your nama has" + length) -typeError
print("your name has" + str(length))
new_length = str(length)
print(type(new_length))

name = "jenny"
# print(10 +int(name)) ValueError

first_number =int(input("guess a number?"))
second_number = int(input("guess another number?"))

# total = int(first_number) + int(second_number)
total = first_number + second_number
print(total)