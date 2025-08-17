import math
# def prime_checker(nums):
#     is_prime = True
#     if nums == False:
#         is_prime =False
#     for i in range (2,nums-1):
#         if nums % i == 0:
#             is_prime = False
#     if is_prime == True:
#         print(f"prime number")
#     else:
#         print(f"not a prime number")
# n= int(input("enter a number: "))
# prime_checker(19)

     
def prime_checker(num):
    if num < 2:
        return False    
    for i in range(2,int(math.sqrt(num))):
        if num % i == 0:
            return False
        return True
            
n = int(input("Enter a number: "))
print("Prime" if prime_checker(n) else "Not Prime")