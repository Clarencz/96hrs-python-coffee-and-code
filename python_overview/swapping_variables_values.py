a = 24
b = 41

# =====method 1 =====
# temp = a 
# a = b
# b = temp
# print(a,b)

# ========method 2 ======
# a,b = b,a
# print(a,b)

# =========method 3 ========
'''
24 =11000
41 = 101001
'''
a = a ^ b
b = b ^ a
a = a ^ b
print(a,b)