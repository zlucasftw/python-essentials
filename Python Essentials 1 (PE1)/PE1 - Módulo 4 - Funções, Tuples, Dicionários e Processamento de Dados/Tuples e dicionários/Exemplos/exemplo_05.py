# Tuples e dicionários

# Como usar um tuple

# Tuples são capazes de aparecer no lado esquerdo do operador de atribuição

# Troca de variáveis que contém elementos de uma tuple - troca de valores

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)
