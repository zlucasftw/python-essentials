# A natureza das strings em Python

# Strings como sequências: indexação

# Strings no Python são sequências, não são listas
# mas pode tratá-las como listas em casos particulares

# Se quiser acessar a algum caracter da string pode
# através da indexação

# Índices negativos também se comportam
# da mesma maneira como nas listas.

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()
