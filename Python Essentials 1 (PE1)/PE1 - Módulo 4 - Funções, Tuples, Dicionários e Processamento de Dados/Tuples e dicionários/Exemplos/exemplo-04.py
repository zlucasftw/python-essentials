# Tuples e dicionários

# Como usar um tuple

# Tuples aceitam a função len() retornando o número de elementos contidos no seu anterior
# O operador + pode juntar tuples
# O operador * pode multiplicar tuples, assim como listas
# Operadores in e not in trabalham da mesma maneira que nas listas

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
