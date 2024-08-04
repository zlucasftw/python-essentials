# Módulos úteis - math

# Funções selecionadas a partir do módulo math

# Primeiro grupo das funções math estão relacionadas com trigonometria

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
