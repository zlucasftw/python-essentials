# Devolver um resultado de uma função

# Efeitos e resultados: lista e funções

# Erro (TypeError) - Função esperando uma lista como parâmetro
# mas recebe um inteiro como argumento na invocação

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum(5))
