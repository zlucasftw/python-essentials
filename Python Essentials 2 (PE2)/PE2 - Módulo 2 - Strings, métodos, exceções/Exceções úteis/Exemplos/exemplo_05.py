# Exceções úteis

# Exceções integradas - OverflowError

# Localização: BaseException <- Exception <- ArithmeticError <- OverflowError

# É uma exceção concreta levantada quando uma operação produz um número
# muito grande para ser armazenado com sucesso.

# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')
