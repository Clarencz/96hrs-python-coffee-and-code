order = input("what is your pizza order? (small or medium or large) ")
with_pepperoni = input("would you like some extra pepperoni with it (yes or no)")
small = 100
medium = 200
large = 300
bill =0
if order == "small":
    if with_pepperoni == "yes":
        bill = small +30
        print(f"Price is {bill}")
    else:
        bill +=small
        print(f"price is {bill}")
elif order == "medium":
    if with_pepperoni == "yes":
        bill = medium +50
        print(f"Price is {bill}")
    else:
        bill +=medium
        print(f"price is {bill}")
elif order == "large":
    if with_pepperoni == "yes":
        bill = large +50
        print(f"Price is {bill}")
    else:
        bill +=large
        print(f"price is {bill}")
        
else:
    print("you have not chosen an order!")
    
extra_cheese = input("do you want extra cheese (yes or no)")
if extra_cheese == "yes":
    bill+=20
print(f"your final bill is {bill}")
