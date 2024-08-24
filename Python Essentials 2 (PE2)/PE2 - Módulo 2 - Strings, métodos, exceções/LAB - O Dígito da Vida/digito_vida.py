# LAB: O Dígito da Vida

data = input('Digite o dia, mes e ano de seu nascimento: ')

while data.isdigit() is False:
    data = input('Digite o dia, mes e ano de seu nascimento: ')

data = data.replace(' ', '')
soma = 0

for numero in data:

    soma += int(numero)

soma = str(soma)

digito = 0

for numero in soma:

    digito += int(numero)

print(digito)
