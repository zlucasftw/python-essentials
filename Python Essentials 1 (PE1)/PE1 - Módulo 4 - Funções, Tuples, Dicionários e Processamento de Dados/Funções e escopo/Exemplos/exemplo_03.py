# Scopes em Python

# Funções e scopes - sombreamento de variável fora de escopo da função

def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
