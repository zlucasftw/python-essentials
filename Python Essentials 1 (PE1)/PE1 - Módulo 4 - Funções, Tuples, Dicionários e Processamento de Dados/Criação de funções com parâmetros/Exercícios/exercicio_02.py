# Exercício 2

# Qual é o output do seguinte snippet?


def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))

# Resposta: 56
