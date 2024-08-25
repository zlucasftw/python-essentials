# Exceções úteis

# Exceções integradas - Assertion Error

# Localização: BaseException <- Exception <- AssertionError

# É uma exceção concretal evantada pela instrução assert
# quando a sua argumentação avalia para False, None, 0
# ou uma string vazia.

from math import tan, radians

angle = int(input('Enter integral angle in degrees: '))

# We must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))
