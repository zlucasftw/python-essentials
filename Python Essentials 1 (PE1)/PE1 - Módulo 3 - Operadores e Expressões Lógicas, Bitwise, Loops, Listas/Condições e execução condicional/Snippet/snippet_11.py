# Funções integradas: max() e min()

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the lowest
# and pass it to the lowest_number variable.

lowest_number = min(number1, number2, number3)

# Print the result.
print("The lowest number is:", lowest_number)
