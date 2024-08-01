# Resumo da seccção - Key takeaways: tuples (1/3)

# 6. É possível percorrer os elementos de uma tuple através de uma estrutura de repetição ou um loop

# Example 1

tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)


# É possível verificar se um elemento específico está ou não presente em uma tuple

# Example 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)

# É possível utilizar a função len() para verificar quantos elementos existem num tuple

# Example 3
tuple_3 = (1, 2, 3, 5)
print(len(tuple_3))

# É possível juntar ou multiplicar tuples

# Example 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

print(tuple_4)
print(tuple_5)
