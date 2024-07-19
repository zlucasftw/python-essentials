# Como as funções comunicam com o seu ambiente

# Mistura de argumentos posicionais e de keywords

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


adding(3, c = 1, b = 2)
