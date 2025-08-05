import queue

numbers = [10,20,30,40,50,60,70,80,90]
# q = queue.Queue()

# for number in numbers:
#     q.put(number)
# print(q.get())
# print(q.get())

# q = queue.LifoQueue()
# for number in numbers:
#     q.put(number)
# print(q.get())
# print(q.get())


q = queue.PriorityQueue()
q.put((2,"hello"))
q.put((11,99))
q.put((5,7.4))
q.put((1,True))

while not q.empty():
    print(q.get())