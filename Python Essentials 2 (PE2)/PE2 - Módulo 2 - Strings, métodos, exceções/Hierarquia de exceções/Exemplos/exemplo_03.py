# A anamotia das exceções

# Exceções

# Quando tratando-se de exceções a ordem
# dos ramos precisa ser levado em consideração.
# Exceções gerais vem depois de exceções mais concretas,
# pois caso contrário uma exceção se tornará inalcançável ou inútil,
# além de tornar o código confuso e inconsistente.

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")
