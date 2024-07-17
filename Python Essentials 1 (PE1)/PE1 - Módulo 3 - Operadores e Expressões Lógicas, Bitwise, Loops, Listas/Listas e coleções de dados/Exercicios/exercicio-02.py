# Exercicio - 2

# Qual é o output do seguinte snippet?

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

# Resposta:  1, 3, 6, 10, 15
