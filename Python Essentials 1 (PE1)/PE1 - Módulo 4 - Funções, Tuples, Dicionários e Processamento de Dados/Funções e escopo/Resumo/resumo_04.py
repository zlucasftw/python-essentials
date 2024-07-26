# Resumo da seccção - Key takeaways

# 2. Variável existente dentro de uma função tem escopo (scope) apenas dentro do corpo da função

# Exemplo 4:


def adding(x):
    var = 7
    return x + var


print(adding(4))    # outputs: 11
print(var)  # NameError
