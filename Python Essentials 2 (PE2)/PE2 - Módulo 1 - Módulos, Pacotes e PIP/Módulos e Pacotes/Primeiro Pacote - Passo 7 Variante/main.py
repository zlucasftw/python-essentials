# Módulos e Pacotes

# Alternativa para acessar a função funI() do módulo
# iota a partir do pacote extra
# utilizando nomes de pacotes qualificados

from sys import path

path.append('..\\packages')

from extra.iota import funI

print(funI())
