# Criação de funções - funções de dois parâmetros

# Função simples: Conversão de unidades imperiais em unidades métricas

# Função de conversão de pés e polegadas para altura ou metros

# Caso de utilização de apenas um parâmetro (no caso pés sem polegadas)

# 1 ft = 0.3048 m
# 1 in = 2.54cm = 0.0254 m


def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(6))
