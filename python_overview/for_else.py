numbers = [21,3,41,5,-1,3]
# for i in numbers:
#     print(i)
#     if i ==5:
#         break
# else:
#     print("completed successfully")
# print("out of for/else")

for i in numbers:
    # print(i)
    if i%2 ==0:
        print(i)
        break
else:
    print("there is no number divisible by 2")
print("out of for/else")