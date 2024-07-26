# Scopes em Python

# Funções e scopes: keyword global

def my_function():
    global var
    var = 2
    print("Do I know that varaible?", var)


var = 1
my_function()
print(var)
