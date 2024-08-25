# Erros - o pão diário do programador | try-except

# Exceções

# Sem um ramo nomeado para a exceção,
# e sem a exceção geral a exceção não
# será tratada e levantará a exceção.

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter a integer value.")

print("THE END.")
