# Erros - o pão diário do programador | try-except

# Exceções

# Ramos dedicados de exceção. Quando não existente,
# a exceção cai no ramo geral que sempre deve ficar
# no final de todos os ramos de exceções que o bloco
# try possuir.

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")
