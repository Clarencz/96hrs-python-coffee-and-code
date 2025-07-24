numbers = input("enter a range of numbers: ")
list_numbers = numbers.split(" ")
list2_numbers= [int(number)for number in list_numbers]
print(list2_numbers)
# max_result = [for max_number in list2_number]
max_result = list2_numbers[0]
for max_number in list2_numbers:
    if max_number > max_result:
        max_result= max_number
print(max_result)