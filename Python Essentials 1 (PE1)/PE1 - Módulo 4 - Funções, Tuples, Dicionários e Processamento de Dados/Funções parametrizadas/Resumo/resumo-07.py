# Resumo da secção - Key takeaways

# Erro - argumentos posicionais não devem seguir argumentos keyword

def subtra(a, b):
    print(a -b)


subtra(5, b=2)      # outputs: 3
subtra(a=5, 2)      # Syntax Error
