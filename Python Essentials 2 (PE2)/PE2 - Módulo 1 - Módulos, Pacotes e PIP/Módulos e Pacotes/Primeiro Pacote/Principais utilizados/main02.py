# Módulos e pacotes

# Variante do acesso a função funI()
# a partir do pacote 'extra'
# utilizando nomes de pacotes qualificados 'iota'

from sys import path

path.append('..\\packages')
from extra.iota import funI

print(funI())
