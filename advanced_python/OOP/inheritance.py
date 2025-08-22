# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return "name {}, age{}".format(self.name, self.age)
# class Worker(Person):
#     def __init__(self,name,age,salary):
#         super(Worker,self).__init__(name,age)
#         self.salary = salary
#     def __str__(self):
#         text = super(Worker,self).__str__()
#         text += "salary{}".format(self.salary)
#     def calc_yearly_salary(self):
#         return self.salary * 12
    
# worker1 = Worker("monica",40,3000)
# print(worker1)

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x +other.x, self.y + other.y)
    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)
    def __str__(self):
        return "x {}, y{}".format(self.x,self.y)
    
v1 = Vector(3,2)
v2 = Vector(8,3)
v3 = v1 + v2
print(v1)
print(v2)
print(v3)