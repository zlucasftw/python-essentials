# Listas em aplicações avançadas - Arrays

# Natureza multidimensional das listas

# Registro de temperatura para estação metereológica

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

# Temperatura mais alta durante todo mês

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)
