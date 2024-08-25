# A anatomia das exceções | assert

# Exceções: continuação

# A instrução 'assert', que é uma keyword, pode ser
# utilizada inserindo-a em lugares do código onde
# não quer de nenhuma maneira dados errados, ou
# em que não se tem certeza de que esses dados já foram
# tratados. Ao levantar uma exceção 'AssertionError'
# assegura que o código não produza resultados inválidos.
# Entretanto assertions não substituem exceções nem validam dados,
# apenas é um complemento dos mesmos.

# Nesse exemplo, o programa ocorre sem falhas se
# é informado um valor número válido maior ou igual
# a zero. Caso contrário, irá se levantar uma
# exceção 'AssertionError'.

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
