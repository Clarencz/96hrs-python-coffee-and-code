from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass = ABCMeta):
    @abstractclassmethod
    def person_method():
        '''Interface method'''

class  Student(IPerson):
    
    def __init__(self):
        self.name = "basic sudent name"
        
    def person_method(self):
        print("i am a student")
        
class Teacher(IPerson):
    
    def __init__(self):
        self.name = "Basic Teacher Name"
        
    def person_method(self):
        print("i am a teacher")
        
# s1 = Student()
# s1.person_method()
# t1 = Teacher()
# t1.person_method()

class  PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("invalid type")
        return -1
if __name__ == "__main__":
    choice = input("what type of person do you want to create?\n")
    Person = PersonFactory.build_person(choice)
    Person.person_method()