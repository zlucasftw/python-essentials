# Exercicio 1

# Qual é o output do seguinte snippet?

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)

# Resposta: 2, 6, 3, 4, 5, 1
# Resposta incorreta: O número 6 é inserido na segunda posição da lista
# e se torna o primeiro da lista quando o número 1, o primeiro elemento
# é removido.
