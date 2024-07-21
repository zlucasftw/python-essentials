# Resumo da seccção - Key takeaways

# 1.2. Variável fora da função tem escopo (scope) dentro do corpo da função

# Exemplo 1:

var = 2


def mult_by_var(x):
    return x * var


print(mult_by_var(7))   # outputs: 14
