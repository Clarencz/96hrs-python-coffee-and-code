import threading
import time
lock  = threading.Lock()
x = 8192
def double():
    global x , lock
    lock.acquire()
    while x < 16384:
        x*=2
        print(x)
        time.sleep(2)
    print("max reached")
    lock.release()
    
def half():
    global x, lock
    lock.acquire()
    while x >1 :
        x/=2
        print(x)
        time.sleep(2)
    print("min reached")
    lock.release()
    
double1 = threading.Thread(target=double)
half1 = threading.Thread(target=half)
double1.start()
half1.start()