height = int(input("what is your height in feet: "))
if height >= 3:
    print("you can ride")
    age = int(input("what is your age? "))
    if age <= 12:
        print("pay 300")
    elif age <=18:
        print("pay 400")
    else:
        print("pay 500")    
else:
    print("can't ride")