Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Part 2: Multiplication and Division of two numbers
>>> 
>>> # Ask the user to input two numbers
>>> num1 = float(input("Enter the first number (num1): "))
Enter the first number (num1): 10
>>> num2 = float(input("Enter the second number (num2): "))
Enter the second number (num2): 20
>>> 
>>> # Perform multiplication
>>> multiplication_result = num1 * num2
>>> 
>>> # Perform division
>>> if num2 != 0: division_result = num1 / num2
... else:
...     division_result = "undefined (division by zero)"
... 
...     
>>> # Display the results
>>> print(f"The multiplication of {num1} and {num2} is: {multiplication_result}")
The multiplication of 10.0 and 20.0 is: 200.0
>>> print(f"The division of {num1} by {num2} is: {division_result}")
The division of 10.0 by 20.0 is: 0.5
