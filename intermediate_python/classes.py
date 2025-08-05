# class Person:
    # def __init__(self):
    #     # print("hello world")
    #     self.name = "clarence"
    #     self.age = 23
    
# variable = Person()
# print(variable.name)
# print(variable.age)

# class Person:
#       def __init__(self,name,age,height):
#             self.name = name
#             self.age   = age
#             self.height = height
# variable = Person("clarence",23,5.2)
# print(variable)
# print(variable.name)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def helloworld(self):
#         print("helloworld")
        
# variable = Person("charles", 18)
# variable.name = "immaculate"
# print(variable.name)
# print(f"{variable.helloworld()}")


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     # def __del__(self):
#     #     print("oblect deleted")
#     def __str__(self):
#         return "name {} , age{}" .format(self.name,self.age)
# person1 = Person("loe", 32)
# print(person1.name)
# print(person1.age)

# # del person1

# print(person1)

class Person:
    
    amount = 0 
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.amount+=1
    def __del__(self):
        Person.amount-+1
    def __str__(self):
        return "name {} , age{}" .format(self.name,self.age)
    def get_older(years):
        self.age += years
person1 = Person("loe", 32)


# del person1

print(person1)
person2 = Person("sara",40)
print(person2)