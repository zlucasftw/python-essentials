# Scopes em Python

# Como a função interage com os seus argumentos
# Alteração do valor do parâmetro não se propaga para fora da função

def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)
