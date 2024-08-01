# Resumo da seccção - Key takeaways: tuples (1/3)

# Pode-se criar uma tuple utilizando a função incorporada do Python tuple()
# Particularmente útil para conversão de um tipo de dado iterável em uma tuple

my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)      # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)      # outputs: (2, 4, 6)
print(type(tup))
