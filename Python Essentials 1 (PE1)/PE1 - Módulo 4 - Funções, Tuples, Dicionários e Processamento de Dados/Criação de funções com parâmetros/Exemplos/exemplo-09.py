# Criar funções - funções de três parâmetros

# Funções simples: verificar três lados de comprimento de um triângulo

# Versão compacta 2


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
