
# Future improvement: validation of data
# future improvement: Unit conversion

height = float(input("\nPlease enter your height (in meters, i.e. 1.80): "))
weight = float(input("\nPlease end your weight (in kg, i.e. 70.5kg): "))

print("\n\n========")
print("Your Height is:", height, "Meters \nYour Weight is:", weight,"KG")
print("========")

# calculate BMI and round to 1 digit
# future improvement use maths module for powers?
bmi = round(weight/(height**2),1)

print("\n========\n========\n")
print("Your Current BMI is: " ,bmi, "\n")

if (bmi >= 30):
    print("Obese range")
elif (bmi >=25):
    print("Overweight Weight range")
elif (bmi >=18.5):
    print("Normal/Healthy Weight range")
else:
    print("Underweight Range")
print("\n========\n========\n")

### Next task, for a given height, calc a users weights for given BMI values.
# other tasks
# use functions
print("--------------------------------")
print("|    Group    | Lower | Higher |")
print("--------------------------------")
print("| Underweight | value | value  |")
print("--------------------------------")
print("|   Normal    | value | value  |")
print("--------------------------------")
print("| Overweight  | value | value  |")
print("--------------------------------")
print("|    Obese    | value | value  |")
print("--------------------------------")
'''
    If your BMI is less than 18.5, it falls within the underweight range.
    If your BMI is 18.5 to 24.9, it falls within the normal or Healthy Weight range.
    If your BMI is 25.0 to 29.9, it falls within the overweight range.
    If your BMI is 30.0 or higher, it falls within the obese range.
'''