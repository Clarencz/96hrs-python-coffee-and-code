import sys

# def mygenerator(n):
#     # yield
#     for x in range (n):
#         yield x**3

# values = mygenerator(100)
# # print(next(values))
# # print(next(values))
# print(sys.getsizeof(values))

# # for x in values:
# #     print(x)


def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5
        
values = infinite_sequence()
# print(next(values))
# print(next(values))
# print(next(values))
for x in range(30):
    print(next(values))