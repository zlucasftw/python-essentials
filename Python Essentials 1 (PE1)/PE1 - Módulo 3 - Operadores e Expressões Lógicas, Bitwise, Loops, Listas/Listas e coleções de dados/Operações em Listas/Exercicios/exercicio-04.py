# Exercício 4

# Qual é o output do seguinte snippet?

list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

# Resposta: ['A', 'B', 'C']
