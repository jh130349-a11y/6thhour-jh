#Name:
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

U = (18.5)
NW = (21.7)
OW = (29.9)
O = (30)

weight = float(input("Enter your weight (in kilograms) "))
print(weight)

height = float(input("Enter your height (in meters) "))
print(height)

BMI = (weight / height**2)

print(BMI)

if BMI <= NW:
    print("You are underweight, go eat some mcdonalds you skeleton!!!!!!!")
elif BMI >= NW:
    print("You are normal weight, dont go eat mcdonalds.")
elif BMI >= OW:
    print("You are overweight, hold off the mcdonalds.")
elif BMI >= O:
    print("Holy moly, hold off the doordash! You are obese")