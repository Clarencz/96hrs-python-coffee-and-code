import random
userChoice = int(input("enter your choice: "))
rock = 0
paper =1 
scissors = 2
if userChoice >2 or userChoice<0:
    print("you have entered a wrong number:")
else:
    computer_choice = random.randint(0,2)
    print(computer_choice)
    if computer_choice ==0 and userChoice ==1:
        print("user wins")
    if computer_choice ==1 and userChoice ==2:
        print("user wins")
    if computer_choice ==2 and userChoice ==0:
        print("user wins")
    if computer_choice ==1 and userChoice ==0:
        print("computer wins")
    if computer_choice ==2 and userChoice ==1:
        print("computer wins")
    if computer_choice ==0 and userChoice ==2:
        print("computer wins")
    if computer_choice ==0 and userChoice ==0:
        print("Draw")
    if computer_choice ==1 and userChoice ==1:
        print("Draw")
    if computer_choice ==2 and userChoice ==2:
        print("Draw")