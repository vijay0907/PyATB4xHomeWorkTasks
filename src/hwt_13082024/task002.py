# Task #2
# Create a program to get num1 to num2 with user input
# pow num1 to num2
# Sum, Sub, Mul, Div

num1 = int(input("Enter the number1 : "))
num2 = int(input("Enter the number2 : "))

result_of_pow = pow(num1, num2)
print(f"Power of number1 is : {result_of_pow}")

result_of_sum = num1+num2
result_of_sub = num1-num2
result_of_mul = num1*num2
result_of_div = num1/num2


print(f"Sum of two numbers : {result_of_sum}")
print(f"Sub of two numbers : {result_of_sub}")
print(f"Mul of two numbers : {result_of_mul}")
print(f"Div of two numbers : {result_of_div}")