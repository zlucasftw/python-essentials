# Tuples e dicionários

# Erro - tentativa de modificação de um conteúdo de uma tuple

my_tuple = (1, 10, 100, 1000)

my_tuple.append(10000)
del my_tuple[0]
my_tuple[1] = -10
