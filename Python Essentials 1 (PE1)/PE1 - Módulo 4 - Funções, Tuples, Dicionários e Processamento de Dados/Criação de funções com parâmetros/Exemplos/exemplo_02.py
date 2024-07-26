# Criação de funções - funções de dois parâmetros

# Função simples: avaliar o IMC (BMI)

# Condicional que define comportamento em caso inválido em algum dos argumentos


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))
