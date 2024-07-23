# Exercício 1

# O que acontecerá quando se tentar executar o seguinte snippet e porquê?


def factorial(n):
    return n * factorial(n - 1)


print(factorial(4))

# Resposta: Erro. É tentado realizar uma função recursiva entretanto sem nenhuma condição de terminação.
