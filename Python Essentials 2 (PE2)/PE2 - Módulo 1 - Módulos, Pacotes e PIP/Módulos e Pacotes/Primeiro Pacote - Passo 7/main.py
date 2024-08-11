# Módulos e Pacotes

# Acessando a função funI() do módulo iota a partir do pacote extra
# utilizando nomes de pacotes qualificados

from sys import path

path.append('..\\packages')

import extra.iota

print(extra.iota.funI())
