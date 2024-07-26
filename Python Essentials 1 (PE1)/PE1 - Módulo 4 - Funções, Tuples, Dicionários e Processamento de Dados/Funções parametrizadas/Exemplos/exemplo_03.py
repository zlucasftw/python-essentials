# Como as funções comunicam com o seu ambiente

# Sobreamento de variável - variável com mesmo nome de parâmetro

def message(number):
    print("Enter a number:", number)


number = 1234
message(1)
print(number)
