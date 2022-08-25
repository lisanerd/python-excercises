
weight = float(input("Your weight in kilograms: "))
height = float(input("Your height in meters: "))
BMI = round(weight/height**2)

print(f"Your BMI is {BMI}.")


if 0 < BMI < 18.5:
    print("You are underweight.")
elif 18.5 < BMI < 24.9:
    print("You are normal weight.")
elif 25 < BMI < 29.9:
    print("You are overweight.")
elif 30 < BMI < 34.9:
    print("You are obese.")
elif 35 < BMI < 100:
    print("You are extremely obese.")