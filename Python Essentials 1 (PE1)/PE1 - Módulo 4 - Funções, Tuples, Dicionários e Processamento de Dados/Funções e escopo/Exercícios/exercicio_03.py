# Exercício 3

# Qual é o output do seguinte snippet?

a = 1


def fun():
    global a
    a = 2
    print(a)


fun()
a = 3
print(a)

# Resposta: 2, 3
