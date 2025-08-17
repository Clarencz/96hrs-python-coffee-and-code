import math

number = 2

# digit_amount = len(str(number))
# print(digit_amount)


# =====method 1 ======
# doesn't work for 0, and negative numbers
# print(int(math.log10(number))+1)

# ===constraint 1===
# fails because computers fail to rep floats accurately
# if number > 0 :
#     print(int(math.log10(number))+1)
# elif number <0:
#     print(int(math.log10(-number))+2)
# else:
#     print(1)
    
# ====constraint 2 ===
counter = 1
while abs(number) >= (10**counter):
    counter +=1
print(counter)