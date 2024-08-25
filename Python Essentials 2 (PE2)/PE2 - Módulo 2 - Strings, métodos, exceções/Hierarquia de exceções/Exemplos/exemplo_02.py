# A anamotia das exceções

# Exceções

# Quando tratando-se de exceções a ordem
# dos ramos precisa ser levado em consideração.
# Exemplo com a ordem correta.

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")
