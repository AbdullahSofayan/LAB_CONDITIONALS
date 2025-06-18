

Wieght = float (input("Enter Your Weight: "))
Height = float (input("Enter Your Height (in meters): "))
BMI = Wieght / (Height ** 2)
print("Your BMI:", round(BMI,2))

if BMI > 25:
    print("You are overweight. You need to work out more and watch your diet.")
elif 18.5 <= BMI <= 25:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")




