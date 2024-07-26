# Devolver um resultado de uma função

# Efeitos e resultados: lista e funções

# Retorno de uma lista através de uma função

def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_list_fun(5))
