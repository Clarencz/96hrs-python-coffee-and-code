# myscript.py 
import sys
import getopt
# def myfunction(*args,**kwargs):
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(kwargs['keyone'])
#     print(kwargs['keytwo'])
    
# myfunction('hey',True,19,keyone = 'animal',keytwo = 'leopard')


# print(sys.argv[0])
# print(sys.argv[1])

# # usage a_p.py filename
# print(len(sys.argv))
# filename= sys.argv[1]
# message = sys.argv[2]

# with open (filename,'w+')as f:
#     f.write(message)
    
opts,args = getopt.getopt(sys.argv[1:],"f:n:", ["filename", 'message'])
print(opts)
print(args)

