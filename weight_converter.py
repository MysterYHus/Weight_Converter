weight = float(input("Enter weight here: "))
unit = input("Is that in kg or lbs: ")

if unit == "kg":
    converted = round(weight * 2.2, 2)
    print("Weight in lbs: " + str(converted))
else:
    converted = round(weight / 2.2, 2)
    print("Weight in kg: " + str(converted))
