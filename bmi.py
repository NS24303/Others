
# Future improvement: validation of data
# future improvement: Unit conversion

height = float(input("Please enter your height (in meters, i.e. 1.80): "))
weight = int(input("Please end your weight (in kg, i.e. 70.5kg): "))

print("Your Height is: ", height, "\nYour Weight is", weight,"KG")

# calculate BMI and round to 1 digit
# future improvement use maths module for powers?
bmi = round(weight/(height**2),1)

print("\n\nYour Current BMI is: " ,bmi)

if (bmi >= 30):
    print("Obese range")
elif (bmi >=25):
    print("Overweight Weight range")
elif (bmi >=18.5):
    print("Normal/Healthy Weight range")
else:
    print("Underweight Range")

### Next task, for a given height, calc a users weights for given BMI values.

'''

    If your BMI is less than 18.5, it falls within the underweight range.
    If your BMI is 18.5 to 24.9, it falls within the normal or Healthy Weight range.
    If your BMI is 25.0 to 29.9, it falls within the overweight range.
    If your BMI is 30.0 or higher, it falls within the obese range.
    
'''