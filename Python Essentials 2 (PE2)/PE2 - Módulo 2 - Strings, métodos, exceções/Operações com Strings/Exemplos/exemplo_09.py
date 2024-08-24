# Strings em ação

# Strings vs. números

# Para transformar uma string em um número só é possível quando
# a string representa um número válido. Caso não represente,
# será disparado um erro ou uma exceção.

# Para realizar a transformação pode-se utilizar a função
# int(), para obter um número inteiro, e float()
# para um valor de floating-point

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)
