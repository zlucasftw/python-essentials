# Criar funções - recursividade

# Funções simples: recursividade

# Fatorial


def factoial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factoial_function(n - 1)

