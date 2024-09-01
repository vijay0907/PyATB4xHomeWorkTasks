#Develop a Python script that calculates the square and cube of given number

# Logic Building Formula

# Step 1: Figure out the inputs and output
# input --> get num1 (square) from user --> data type --> int
# input --> get num2 (cube) from user --> data type --> int
# formula for square --> square of a = a2 = a × a
# formula for cube --> cube of a = a3 = a × a × a

# Output --> int

import math

# Define the number to be squared
num1 = int(input("Enter the number to find the square: "))

# Use the ** operator to square the number
squared_number = num1 ** 2
# Print the result
print(f"The square of {num1} is {squared_number}")

# Squaring a number using the pow() function
squared_pow = pow(num1, 2)
# Print the result
print(f"The square of {num1} is {squared_pow}")


#math.pow() function
squared_math = math.pow(num1, 2)
print(f"The square of {num1} is {squared_math}")

# Find the cube of given number

# Define the number to be cubed
num2 = int(input("Enter the number to find the cube: "))
# Use the ** operator to square the number
cubed_number = num2 ** 3
# Print the result
print(f"The cube of {num2} is {cubed_number}")

# Squaring a number using the pow() function
cubed_pow = pow(num2, 3)
# Print the result
print(f"The cube of {num2} is {cubed_pow}")


#math.pow() function
cubed_math = math.pow(num2, 3)
print(f"The cube of {num2} is {cubed_math}")