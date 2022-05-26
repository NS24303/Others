
# Future improvement: validation of data
# future improvement: Unit conversion

height = float(input("\nPlease enter your height (in meters, i.e. 1.80): "))
weight = float(input("\nPlease end your weight (in kg, i.e. 70.5kg): "))

print("\n\n========")
print("Your Height is:", height, "Meters \nYour Weight is:", weight, "KG")
print("========")

# calculate BMI and round to 1 digit
# future improvement use maths module for powers?
bmi = round(weight/(height**2), 1)

print("Your Current BMI is: ", bmi, "Which puts you within the:")

# calculate values for underweight upper limit
under_high = round(18.4*(height**2), 1)
# calculate values for normal/healthy upper/lower
normal_low = round(18.5*(height**2), 1)
normal_high = round(24.9*(height**2), 1)
# calculate values for overweight upper/lower
over_low = round(25.0*(height**2), 1)
over_high = round(29.9*(height**2), 1)
# calculate values for obese lower limit
obese_low = round(30*(height**2), 1)

if bmi >= 30:
    print("**** Obese range ****")
    obese_loss = round((weight-obese_low), 1)
    print("You need to lose" , obese_loss, "KG to drop into the overweight category")
    obese_big_loss = round((weight-normal_high), 1)
    print("You need to lose" , obese_big_loss, "KG to drop into the Healthy category")
elif bmi >= 25:
    print("**** Overweight range ****")
    over_loss = round((weight-over_low), 1)
    print("You need to lose" , over_loss, "KG to get into the Healthy category")
elif bmi >= 18.5:
    print("**** Healthy Weight range ****")
else:
    print("**** Underweight Range **** ")
    under_gain = round((under_high-weight), 1)
    print("You need to gain" , under_gain, "KG to get into the Healthy category")
print("\n========\n")

# Display as a table
#21.7 is middle of healthy range

middle = round(21.7*(height**2), 1)
print("to be in the middle of the healthy range (21.7) you weight needs to be" , middle , "KG\n")


print("The table below displays upper and lower weight thresholds (in KG) for each category: \n")

print("--------------------------------")
print("|    Group    | Lower | Higher |")
print("--------------------------------")
print("| Underweight |  n/a  | ", under_high, " |")
print("--------------------------------")
print("|   Healthy   | ", normal_low, "| ", normal_high, " |")
print("--------------------------------")
print("| Overweight  | ", over_low, "| ", over_high, " |")
print("--------------------------------")
print("|    Obese    | ", obese_low, " |  n/a  |")
print("--------------------------------")


# other tasks
# use functions
