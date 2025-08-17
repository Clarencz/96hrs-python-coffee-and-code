even_numbers=[]
sum =0
for number in range(101):
    if number %2 ==0:
        even_numbers.append(number)
        sum += number
print(even_numbers)
print(sum)
        