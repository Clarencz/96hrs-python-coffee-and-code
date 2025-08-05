import threading

# def helloworld():
#     print("hello world!")
    
# t1 = threading.Thread(target = helloworld)
# t1.start()

# def function1():
#     for x in range(50):
#         print("one")
# def function2():
#     for x in range(50):
#         print("two")
        
# t1 = threading.Thread(target=function1)
# t2 = threading.Thread(target=function2)
# t1.start()
# t2.start()

def hello():
    for x in range(10):
        print("hello")
        
t1 = threading.Thread(target=hello)
t1.start()
t1.join() #pause execution of script until threading is done
print("heelloo!!")