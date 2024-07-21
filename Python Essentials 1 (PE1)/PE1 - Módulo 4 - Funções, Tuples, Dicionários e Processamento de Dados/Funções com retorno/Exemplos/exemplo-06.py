# Devolver um resultado de uma função

# Efeitos e resultados: lista e funções

# Lista enviada para uma função como argumento

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([5, 4, 3]))
