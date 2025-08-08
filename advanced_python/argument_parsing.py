# myscript.py 

def myfunction(*args,**kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(kwargs['keyone'])
    print(kwargs['keytwo'])
    
myfunction('hey',True,19,keyone = 'animal',keytwo = 'leopard')

