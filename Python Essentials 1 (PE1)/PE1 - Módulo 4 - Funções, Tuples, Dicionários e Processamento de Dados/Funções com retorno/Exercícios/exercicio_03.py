# Exercício 3

# Qual é o output do seguinte snippet?

def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst


print(even_num_lst(11))

# Resposta: [2, 4, 6, 8, 10]
# Resposta incompleta: a resposta correta é [0, 2, 4, 6, 8, 10] pois 0 / 2 é igual a 0 logo o resto também é 0
