#Input the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#Addition
print("\nAddition: ",num1+num2)
#Subtraction
print("Subtraction: ",num1-num2)
#Multiplication 
print("Multiplication: ",num1*num2)
# Division and handling the exception of zero
if num2 != 0:
    print("Division: ", num1 / num2)
else:
    print("Division: Cannot divide by zero.")
