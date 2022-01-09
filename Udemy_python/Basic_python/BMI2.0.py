
height = float(input("Enter your height in M: "))
weight = float(input("Enter your weight in Kg: "))

bmiCalc = round(weight / (height * height),3)

print(f"your BMI is : {bmiCalc}")

if bmiCalc >= 25:
    print("Too Fat...Wanted!")
elif 24.9 >= bmiCalc >= 23.0: 
    print("over weight")
elif 18.5 <= bmiCalc <= 22.9:
    print("normal weight")
else:
    print("underweight")