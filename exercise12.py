import random
names = input("enter list of names: ")
names_list= names.split(" ")
print(names_list)

random_choice = random.randint(0,len(names_list)-1)
print(names_list[random_choice])