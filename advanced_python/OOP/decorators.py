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

# def logged(function):
#     def wrapper(*args, **kwargs):
#         value = function(*args,**kwargs)
#         with open('logfile.txt', 'a+')as f:
#             fname = function.__name__
#             print(f"{fname} returned value {value}")
#             f.write(f"{fname} returned value {value}\n")
#         return value
#     return wrapper

# @logged
# def add(a,y):
#     return a+ y

# print(add(12,23))  

# ==================Practical Example 2 - Timing==============

import time
# timed decorator to see how first a functino executes
def timed(function):
    def wrapper(*args,**kwargs):
        before = time.time()
        value = function (*args,**kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute")
        return value
    return wrapper

@timed        
def myfunction(x):
    result = 1
    for i in range(1,x):
        result*=i
    return result

myfunction(1000)