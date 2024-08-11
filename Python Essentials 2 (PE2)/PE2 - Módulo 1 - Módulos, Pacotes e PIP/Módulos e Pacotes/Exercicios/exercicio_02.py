# Resumo da seccção - Key takeaways

# Exercício 2

# Alguns pacotes adicionais e necessários são armazenados dentro da diretoria
# D:\Python\Project\Modules. Escreva um código assegurando que a diretoria
# é atravessada pelo Python, a fim de encontrar todos os módulos solicitados.

# Resposta:

# from sys import path
#
# path.append("D:\\Python\\Project\\Modules")

# Resposta correta:

import sys

# note the double backslashes!
sys.path.append("D:\\Python\\Project\\Modules")
