# A anatomia das exceções

# Exceções

# Exceção levantada dentro de uma função,
# mas deixando que se propague para fora
# da função e tratando-se fora da função.
# Nesse caso quem está invocando a função
# precisa tratar da exceção que pode ser
# disparada com a invocação da função.

# Considerações: Exceções podem ultrapassar
# limites de funções e do módulo, e através
# da cadeia de invocação procurar por uma cláusula
# except correspondente que capaz de tratá-la.
# Caso a cláusula não exista, o a execução de código
# é terminada emitindo uma mensagem de diagnóstico.

def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")
