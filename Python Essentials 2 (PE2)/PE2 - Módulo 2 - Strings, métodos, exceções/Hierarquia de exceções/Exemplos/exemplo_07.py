# A anatomia das exceções | raise

# Exceções

# A instrução 'raise' pode ser utilizada com a ausência do nome
# da exceção. Entretanto, essa forma só pode ser utilizada
# dentro de um bloco ou ramo except, qualquer outro contexto
# causa um erro ao tentar utilizá-la.
# A instrução irá levantar a mesma exceção que é atualmente
# tratada, o que permite distribuir o tratamento de exceções
# em diferentes partes do código.

def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise

try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")
