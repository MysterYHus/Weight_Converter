# Weight_Converter
Converts kg to lbs and vice-versa based on user input

Create a program that asks for:

1) Weight
2) KG or LBS
3) Converts it.

This code takes user input for weight and the unit of measurement ("kg" or "lbs"). Depending on the unit entered, it converts the weight to the other unit and prints the result. The conversion factor used is 2.2, assuming 1 kilogram is approximately equal to 2.2 pounds.

This is how it works:


1. User Input:
	- The program prompts the user to enter their weight using float(input("Weight: ")). The entered value is stored in the variable weight.

2. Unit Input:
	- The program then prompts the user to enter the unit of weight, either "kg" or "lbs", using input("kg or lbs: "). The entered value is stored in the variable unit.

3. Conditional Check ( if unit == "kg":):
	- The program checks whether the unit entered by the user is "kg".

4. Conversion and Output ( converted = weight * 2.2):
	- If the unit is "kg", the program multiplies the weight by 2.2 to convert it to pounds. The result is stored in the variable converted.
	- It then prints the converted weight in pounds.

5. Alternative Conversion and Output ( else:):
	- If the unit is not "kg" (i.e., it's assumed to be "lbs"), the program divides the weight by 2.2 to convert it to kilograms. The result is stored in the variable converted.
	- It then prints the converted weight in kilograms.
