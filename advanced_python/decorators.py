# def mydecorator(function):
#     def wrapper( *args, **kwargs):
#         # return function(*args,**kwargs)
#         return_value =  function(*args,**kwargs)
#         print("i am decorating your function")
#         return return_value
        
#     return wrapper

# @mydecorator
# def hello_world(person):
#     # print(f"hello world{person}")
#     return f"hello world{person}"
    
    
# print(hello_world("mike"))

# ===========Practical Example - Logging ==============

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args,**kwargs)
        with open('logfile.txt', 'a+')as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

@logged
def add(a,y):
    return a+ y

print(add(12,23))  

