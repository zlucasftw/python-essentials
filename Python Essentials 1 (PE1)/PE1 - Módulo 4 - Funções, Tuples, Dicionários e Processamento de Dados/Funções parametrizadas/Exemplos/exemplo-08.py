# Como as funções comunicam com o seu ambiente

# Passagem de argumentos de keyword ou keyword argument passing
# Passagem de argumento definida pelo nome não pela posição

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction(first_name= "James", last_name="Bond")
introduction(last_name= "Skywalker", first_name="Luke")
