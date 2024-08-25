# Erros - o pão diário do programador

# Exceções

# Realizar verificações para todas as circunstâncias
# no código não torna a programação mais fácil e
# pode torná-lo inchado e ilegível.
# Uma abordagem diferente é preferida.

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if second_number != 0:
    print(first_number / second_number)
else:
    print("This operation cannot be done.")

print("THE END.")
