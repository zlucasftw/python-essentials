# Importar um módulo - aliasing

# Pode-se utilizar o alias para entidades
# e várias vezes utilizando vírgula indicando
# a entidade e o seu alias em relação ao módulo

from math import pi as PI, sin as sine

print(sine(PI/2))
