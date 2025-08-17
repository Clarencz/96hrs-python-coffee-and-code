weight = int(input("enter your weight: "))
height = float(input("enter your height: "))
bmi = round(weight / height **2)
if bmi < 18.5 :
    print(f"your bmi {bmi} and you are underweight")
elif bmi < 25:
    print(f"your bmi {bmi} you are normal weight")
elif bmi<30:
    print(f"your bmi {bmi} and you are overweight")
elif bmi <35:
    print(f"your bmi {bmi} and you are obese")
else:
    print(f"your bmi {bmi} and you are clinically obese")