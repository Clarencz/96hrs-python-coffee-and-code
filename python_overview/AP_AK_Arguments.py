# def add(*numbers):
#     sum = 0
#     for i in numbers:
#         sum += i
#     print(f"sum is {sum}")
    
# add(1,2)
# add(5,5,5)
# add(12,3,4,1)

# def add(*numbers,name = "jenny"):
#     sum = 0
#     for i in numbers:
#         sum += i
#     print(f"sum is {sum} {name}")
    
# add(1,2,4)

# def info_person(*args,**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
#     print(args)  
# info_person(1,2,name = "ram", age = 30, dept="cse")
# info_person(1,2,name="sham", dept= "cse")

def multiply(*nums):
    multi = 1
    for i in nums:
        multi *=i 
    print(f"the multiplication is {multi}")
        

multiply(2,3,-6,8)
multiply(2,5,8,9,0,6)