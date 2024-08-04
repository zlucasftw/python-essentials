# Módulos úteis - random

# Funções selecionadas a partir do módulo random

# Desvantagem do randrange ou randint - valores repetitivos

from random import randint

for i in range(10):
    print(randint(1, 10), end=', ')
