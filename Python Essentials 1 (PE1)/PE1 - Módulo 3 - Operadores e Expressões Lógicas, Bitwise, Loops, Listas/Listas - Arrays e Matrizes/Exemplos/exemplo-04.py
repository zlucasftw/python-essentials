# Listas em aplicações avançadas - Arrays

# Natureza multidimensional das listas

# Registro de temperatura para estação metereológica

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

# Dias em que a temperatura ao meio-dia era de pelo menos 20ºC

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")
