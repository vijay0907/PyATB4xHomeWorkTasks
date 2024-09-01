#Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than, or equal to the second number

# Logic Building Formula

# Step 1: Figure out the inputs and output
# input --> two numbers num1 & num2 from user --> data type --> int

# Output --> bool --> True or False

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

print("Is the num1 is greater than num2 :", num1>num2)
#print(f"{num1} > {num2} :{num1>num2}")
print("Is the num1 is lesser than num2 :", num1<num2)
#print(f"{num1} < {num2} :{num1<num2}")
print("Is the num1 & num2 are equal:", num1==num2)
#print(f"{num1} == {num2} :{num1 == num2}")