def body_mass(*a):
    if bmi <= 18.5:
        return "Underweight"

    if bmi <= 25.0:
        return "Normal"

    if bmi <= 30.0:
        return "Overweight"

    if bmi > 30:
        return "Obese"

weight=int(input("enter the weight in kg="))
height=int(input("enter the height in cm="))
bmi=weight/height
print(body_mass(bmi))
