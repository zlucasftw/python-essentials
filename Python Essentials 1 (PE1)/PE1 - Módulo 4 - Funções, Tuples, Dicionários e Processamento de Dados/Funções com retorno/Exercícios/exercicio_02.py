# Exercício 2

# Qual é o output do seguinte snippet?

def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False


print(is_int(5))
print(is_int(5.0))
print(is_int("5"))

# Resulstado: True, False, None
