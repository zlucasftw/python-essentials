# Módulos úteis - math

# Funções selecionadas a partir do módulo math

# Grupo de funções ligados à exponenciação

# A função pow() é uma função já integrada com o python e não precisa ser importada

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))
