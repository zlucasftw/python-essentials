# Erros - o pão diário do programador | try-except

# Exceções

# A abordagem da instrução try-expect tem uma desvantagem que,
# se houver a possibilidade de mais do que uma exceção
# irá se ter  uma dificuldade em descobrir o que realmente
# aconteceu ou qual tipo de exceção foi levantada.
# Para isso existe uma variante mais avançada da instrução.

try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")

print("THE END.")
