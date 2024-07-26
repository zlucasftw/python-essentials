# Resumo da seccção - Key takeaways

# 2.2. Keyword global seguida do nome de uma variável para tornar o escopo (scope)
# da variável global e acessível dentro ou fora da função

# Exemplo 5:

var = 2
print(var)  # outputs: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())     # outputs: 5
print(var)      # outputs: 5
