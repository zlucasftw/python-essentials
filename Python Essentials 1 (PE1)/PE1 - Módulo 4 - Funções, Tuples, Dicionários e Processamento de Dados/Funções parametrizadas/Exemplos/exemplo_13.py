# Como as funções comunicam com o seu ambiente

# Mistura de argumentos posicionais e de keywords

# Erro - mais de um valor para um mesmo argumento

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


adding(3, a = 1, b = 2)
