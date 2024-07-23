# Resumo da secção - Key takeaways

# 1. Uma função pode chamar outra funcão ou a si mesma, onde esta é conhecida como recursividade
# e contém um a condição de terminação especificada chamada sendo a função recursiva

# 2. Funções recursivas para código limpo, menor e mais organizado. Entretanto requer cuidado
# pela facilidade de se cometer um erro e criar uma função sem condição de terminação.
# Além disso chamadas recursivas consomem muita memória e podem ser ineficientes.


# Função factorial e exemplo clássico de recursividade

# Recursive implementation of the factorial function.


def factorial(n):
    if n == 1:  # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))     # 4 * 3 * 2 * 1 = 24
