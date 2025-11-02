num1 = 78
num2 = 4
        
        # Get user input for the desired operation
operation =input("Enter the operation(+,-,*,/):") 
        
        # Use if/elif/else to perform the calculation
if operation == '+':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
elif operation == '-':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
elif operation == '*':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
else:
            print("Invalid operation. Please enter +, -, *, or /.")
            
