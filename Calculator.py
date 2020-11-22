def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
# Four operations were slected to choose from as options 

print("Hello, I'm HAL 1000")
print("Please select desired operation. ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
# Allows the user to choose what type of mathmatical operation they would like HAL to complete
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Please enter the First Number: "))
        num2 = float(input("Please enter the Next Number: "))
# Prompts the user to decide what numbers are to be inputed
# The type is selected as a float, in which the answer will be printed as a float and not a whole number
        if choice == '1':
             print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
             print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
             print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
             print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
             print("Im Sorry, I dont Recognize that.")