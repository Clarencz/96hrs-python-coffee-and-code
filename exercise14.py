student_heights=input("enter list of height in feet: ")
list_heights = student_heights.split(" ")

new_height = [float(height)for height in list_heights]
# new_height=[]
# for height in list_heights:
#     new_height.append(float(height))
# print(new_height)
sum =0
# average= 0 
for number in range(len(new_height)):
    print(new_height[number])
    sum = sum + new_height[number]
average = (sum/len(new_height))
print (f"your average height is {sum/len(new_height)}")
