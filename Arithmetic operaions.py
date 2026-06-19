# Arithmetic Operators Assignment
# This program performs addition, subtraction,
# multiplication, and division on two user-input numbers.
# Get input from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Perform arithmetic operations
addition_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number

# Display results
print("\n----- Arithmetic Operation Results -----")
print("Addition:", addition_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)

# Handle division by zero
if second_number != 0:
    division_result = first_number / second_number
    print("Division:", division_result)
else:
    print("Division: Error! Cannot divide by zero.")