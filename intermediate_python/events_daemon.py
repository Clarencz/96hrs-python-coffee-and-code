import threading
import time
# event = threading.Event()

# def myFunction():
#     print("waiting for event to trigger")
#     event.wait()
#     print("performing action now!!")
    
# t1 = threading.Thread(target=myFunction)
# t1.start()

# q = input("do you want to triggr the event: (y/n)")
# if q == "y":
#     event.set()


path = "text.txt"
text = ""
def readFile():
    global path, text
    while True:
        with open ("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)
        
def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)
        
t1 = threading.Thread(target=readFile, daemon = True)
t2 = threading.Thread(target=printLoop)

t1.start()
t2.start()