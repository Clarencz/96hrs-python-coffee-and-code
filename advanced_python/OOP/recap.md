# class AtmMachine:
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram
#     def config(self):
#         print(f"config is, {self.ram}, {self.cpu}")
        
# com = AtmMachine('34gb','34')
# com2=AtmMachine('16gb',34)
# # print(AtmMachine.config(com))

# com.config()
# com2.config()

# class Computer:
#     def __init__(self):
#         self.name = "Navin"
#         self.age = 26
        
#     def update(self):
#         self.age = 30
        
#     def Compare(self,other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
# c1 = Computer()
# c2 = Computer()

# if c1.Compare(c2):
#     print("they are same")


# class Car:
#     wheels = 4
    
#     def __init__(self):
#         self.mileage = 10
#         self.compan = "BMW"
        
# c1 = Car()
# c2 = Car()

# c1.mil = 14
# Car.wheels = 8
# print(c1.mileage,c1.compan,c1.wheels)

# class Student:
    
#     School = 'Lea'
#     def __init__(self,m1,m2,m3):
#         self.marks1 = m1
#         self.marks2 = m2
#         self.marks3 = m3
        
#     def avg(self):
#         return (self.marks1 +self.marks2+self.marks3)
    
#     # def get_m1(self):
#     #     return self.marks1
    
#     # def set_m1(self,value):
#     #     self.marks1=value
#     @classmethod
#     def getSchool(cls):
#         return cls.School
#     @staticmethod
#     def info():
#         print("this is a student class")
        
    
# Student1 = Student(58,89,57)
# Student2 = Student(23,54,78)
# # Student1.marks1 = 30
# # Student1.marks2 = 50
# # Student1.marks3 = 69
# print(Student1.avg())
# print(Student2.avg())

# print(Student.info())


# class Student:
#     def __init__(self, name, rollno, brand, cpu, ram):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop(brand, cpu, ram)  # create Laptop instance

#     def show(self):
#         print(f"Name: {self.name}, Roll No: {self.rollno}")
#         self.lap.show()  # Call the Laptop's show method

#     class Laptop:
#         def __init__(self, brand, cpu, ram):
#             self.brand = brand
#             self.cpu = cpu
#             self.ram = ram

#         def show(self):
#             print(f"Laptop Brand: {self.brand}, CPU: {self.cpu}, RAM: {self.ram}")

# # Create students with laptop details
# s1 = Student('Navin', 34, 'HP', 'i7', '32GB')
# s2 = Student('Jenny', 35, 'Dell', 'i5', '16GB')

# # Show details
# s1.show()
# s2.show()


# class A:
#     def feature1(self):
#         print("feature 1 is working")

#     def feature2(self):
#         print("feature 2 is working")
        
# class B:
#     def feature3(self):
#         print("feature 3 is working")
        
#     def feature4(self):
#         print("feature 4 is working")
        
# class c(A,B):
#     def feature5(self):
#         print("feature 3 is working")
# a1 = A()
# a1.feature1()
# a1.feature2()

# b1 = B()
# C1 = c()
# C1.feature2()


# class A:
#     def __init__(self):
#         print("in a init")
    
#     def feature1(self):
#         print("feature 3 is working")
        
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("in the init of B")
        
#     def feature2(self):
#         print("feature 4 is working")
        
# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         print("in the init of c")
        
#     def feat(self):
#         super.feature2()
        
        
# a1 = A()
# b1 = B()
# c1 = C()

# class Vscode:
#     def execute(self):
#         print("compiling")
#         print("running")
        
# class MyEditor:
#        def execute(self):
#            print("faster compilation")
#            print("fast running")     

# class Laptop:
    
#     def code(self,ide):
#         ide.execute()
        
# ide = Vscode()
# ide = MyEditor()
        
# lap1 = Laptop()
# lap1.code(ide)


# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
        
#     def __add__(self,other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         m3 = Student(m1,m2)
#         return m3
        
#     def __gt__(self,other):
#         r1 = self.m1 + self.m2
#         r2  = other.m1 + other.m2
#         if r1 > r2:
#             print("m1 is greeater than m2")
#         else:
#             print("m2 is greater than m1")

#     def __str__(self):
#         return f"{self.m1} , {self.m2}"
  
# s1 = Student(43,12)
# s2 = Student(56,76)
# # s3 = s1 + s2
# # print(s3.m1)
# if s1 > s2:
#     print("s1 wins")
# else:
#     print("s2 wins")

# print(s1.__str__())
# 
# 
# 

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
        
#     def sum (self,a=None,b=None,c=None): 
#         if a!= None and b!= None and c!= None:
#             return a+ b +c
#         elif a!=None and b!=None:
#             return a+b
#         else:
#             return a
    
# s1 = Student(43,23)
# print(s1.sum(3,4,5))



# class A:
#     def show(self):
#         print("in A-show")
        
# class B(A):
#     pass
        
# a1 = A()
# b1 = B()
# b1.show()