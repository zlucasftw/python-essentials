from sys import path

# Adicionando um módulo a variável path
# do Python que é utilizada pela instrução de importação

# \ duplicada pois apenas uma é utilizada para
# o escape ou para que se escape em relação a outros caracteres

# O novo caminho com o método append() passa a ocupar o
# último elemento da lsta de caminhos, mas como alternativa
# pode-se utilizar o insert()

# Pode-se utilizar um caminho relativo
path.append('..\\modules')

# Pode-se utilizar um caminho absoluto
# path.append('C:\\Users\\user\\py\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.sum1(zeroes))
print(module.prod1(ones))
