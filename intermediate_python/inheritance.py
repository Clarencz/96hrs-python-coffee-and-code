class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "name {}, age{}".format(self.name, self.age)
class Worker(Person):
    def __init__(self,name,age,salary):
        super(Worker,self).__init__(name,age)
        self.salary = salary
    def __str__(self):
        text = super(Worker,self).__str__()
        text += "salary{}".format(self.salary)
    def calc_yearly_salary(self):
        return self.salary * 12
    
worker1 = Worker("monica",40,3000)
print(worker1)