from collections import Counter
# import random 
# mylist = [random.randint(1,10) for _ in range(20)]
# print(mylist)

mylist = [1, 2, 3, 9, 8, 5, 9, 3, 2, 5, 7, 10, 7, 4, 10, 10, 2, 3, 2, 1]
# current_max = 0
# current_value = None
# for x in mylist:
#     if mylist.count(x) > current_max:
#         current_max = mylist.count(x)
#         current_value = x
        
# print(current_value)

# =======method 2 =======
# counter = Counter(mylist)
# print(counter.most_common(1)[0])


# =========method 3 ==========
most_frequent = max(set(mylist), key=mylist.count)
# print(set(mylist))
frequency = mylist.count(most_frequent)
print(most_frequent, frequency)