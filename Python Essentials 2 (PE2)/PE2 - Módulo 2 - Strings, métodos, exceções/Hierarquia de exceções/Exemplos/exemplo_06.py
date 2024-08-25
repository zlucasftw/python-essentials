# A anatomia das exceções | raise

# Exceções

# Com a instrução 'raise' pode testar a rotina
# de tratamento de exceções.

def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")
