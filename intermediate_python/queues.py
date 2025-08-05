import queue

numbers = [10,20,30,40,50,60,70,80,90]
q = queue.Queue()

for number in numbers:
    q.put(number)
print(q.get())
print(q.get())