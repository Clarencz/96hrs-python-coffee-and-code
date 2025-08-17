#POSITIONAL ARGUMENTS
# def greet(name,dept):
#     print(f"hi {name}")
#     print(f"are from {dept} department")
    
# greet("jenny","cs")

#KEYWORD ARGUMENTS
# def greet(name,dept):
#     print(f"hi {name}")
#     print(f"are from the {dept} department")
    
# greet(dept="cs",name="jenny")

#DEFAULT ARGUMENTS
# def greet(name="jenny",dept="cs"):
#     print(f"hi {name}")
#     print(f"are you from the {dept} department")
    
# greet()

#DEFAULT AND NON-DEFAULT ARGUMENTS
# def greet(name,subject,dept = "cs"):
#     print(f"hi {name}")
#     print(f"do you teach  {subject} ?")
#     print(f"are you from the {dept} department")

# greet("jenny" , "python")

#ARBITRARY POSITIONAL ARGUMENTS
# def add(*args):
#     c=0
#     for number in args:
#         c += number
#     return c
# print(add(4,3,2))