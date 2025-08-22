class Person:
    def __init__(self,name,age,gender):
        self.__name__ = name
        self.__age__ = age
        self.__sex__ = gender
    
    @property
    def Name(self):
        return self.__name__
    
    @Name.setter
    def Name(self,value):
        if value == "bob":
            self.__name__ = "Default name"
        else:
            self.__name__ = value
    
    @staticmethod
    def mymethod():
        print("hello world")  
        
Person.mymethod()
  
p1 = Person("mike", 30, 'f')
print(p1.Name)

p1.Name = "bob"
print(p1.Name)