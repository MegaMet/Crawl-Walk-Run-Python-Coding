height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Hunam heights should not be over 3 meters")

bmi = weight / height ** 2
print(f"BMI: {bmi}")