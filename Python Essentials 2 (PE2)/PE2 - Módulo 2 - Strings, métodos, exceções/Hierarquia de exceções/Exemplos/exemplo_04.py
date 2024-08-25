# A anatomia das exceções

# Exceções

# Exceção levantada dentro de uma função
# sendo tratada dentro do corpo da função.

def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")
