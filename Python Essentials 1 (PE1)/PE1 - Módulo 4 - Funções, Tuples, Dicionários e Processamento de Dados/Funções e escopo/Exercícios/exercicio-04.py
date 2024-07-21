# Exercício 4

# Qual é o output do seguinte snippet?

a = 1


def fun():
    global a
    a = 2
    print(a)


a = 3
fun()
print(a)

# Resposta: 2, 2
