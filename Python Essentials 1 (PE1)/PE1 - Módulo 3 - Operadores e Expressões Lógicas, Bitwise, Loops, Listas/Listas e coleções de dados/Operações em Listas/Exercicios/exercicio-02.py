# Exercício 2

# Qual é o output do seguinte snippet?

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)

# Resposta: []
# Resposta incorreta pois a instrução de deletar 'list_2' deleta a variável que aponta
# para a memória e conteúdo da lista com variável de nome 'list_1'
