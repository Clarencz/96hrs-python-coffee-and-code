your_name = input("enter your name").lower()
crush_name = input("enter their name").lower()
combine_string = your_name + crush_name
t = combine_string.count('t')
r = combine_string.count('r')
u = combine_string.count('u')
e= combine_string.count('e')
true = t +r+ u+e

l = combine_string.count('l')
o = combine_string.count('o')
v = combine_string.count('v')
e = combine_string.count('e')
love = l +o +v+e

score = int(str(true) +str(love))
if  score <10 or score >90:    
    print(f" famous{score}")
elif score >=40 and score <=50:
    print(f"you just good{score}")
else:
    print(f"the score is only{score}")