import threading

event = threading.Event()

def myFunction():
    print("waiting for event to trigger")
    event.wait()
    print("performing action now!!")
    
t1 = threading.Thread(target=myFunction)
t1.start()

q = input("do you want to triggr the event: (y/n)")
if q == "y":
    event.set()