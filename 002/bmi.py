height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_height = float(height)

BMI = int(weight) / (new_height ** 2)
bmi_as_int = int(BMI)

print(bmi_as_int)