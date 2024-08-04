# Módulos úteis - random

# Funções selecionadas a partir do módulo random

# Função seed() e seed(int_value)
# A função seed() define a seed com a hora atual - a seed é utilizado no output de valores aleatórios
# A função seed(int_value) define a seed com algum valor inteiro (int_value)

from random import random, seed

seed(0)

for i in range(5):
    print(random())
