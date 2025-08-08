def mydecorator(function):
    def wrapper( *args, **kwargs):
        # return function(*args,**kwargs)
        return_value =  function(*args,**kwargs)
        print("i am decorating your function")
        return return_value
        
    return wrapper

@mydecorator
def hello_world(person):
    # print(f"hello world{person}")
    return f"hello world{person}"
    
    
print(hello_world("mike"))
