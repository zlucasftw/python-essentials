# Resumo da seccção - Key takeaways

# 1.4. Variável com mesmo nome dentro e fora da função (sombreamento/shadows da variável fora do escopo da função)

# Exemplo 3:

def mult(x):
    var = 7
    return x * var


var = 3
print(mult(7))  # outputs: 49
