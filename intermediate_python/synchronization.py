import threading
import time
# lock  = threading.Lock()
# x = 8192
# def double():
#     global x , lock
#     lock.acquire()
#     while x < 16384:
#         x*=2
#         print(x)
#         time.sleep(2)
#     print("max reached")
#     lock.release()
    
# def half():
#     global x, lock
#     lock.acquire()
#     while x >1 :
#         x/=2
#         print(x)
#         time.sleep(2)
#     print("min reached")
#     lock.release()
    
# double1 = threading.Thread(target=double)
# half1 = threading.Thread(target=half)
# double1.start()
# half1.start()


semaphore = threading.BoundedSemaphore(value=5)
def access(thread_number):
    print("{} is trying to access".format(thread_number))
    semaphore.acquire()
    print("{} was granted".format(thread_number))
    time.sleep(10)
    print(f"{thread_number} is now releasing")
for thread_number in range(1,15):
    t = threading.Thread(target=access,args=(thread_number,))
    t.start()
    time.sleep(1)