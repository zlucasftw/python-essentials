# Resumo da seccção - Key takeaways: tuples (1/3)

# 3.2 Se remmover a vírgula de uma tupla de um elemento criará uma variável e não uma tuple

my_tuple_1 = 1,
print(type(my_tuple_1))     # outputs: <class 'tuple'>

my_tuple_2 = 1              # This is not a tuple.
print(type(my_tuple_2))     # outputs: <class 'int'>
