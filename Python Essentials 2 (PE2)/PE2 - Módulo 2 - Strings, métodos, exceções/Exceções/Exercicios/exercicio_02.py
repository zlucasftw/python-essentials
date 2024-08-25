# Resumo da seccção - Key takeaways

# Exercício 2

# Qual é o output esperado do seguinte código?

try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("zero")
except IndexError:
    # IndexingError
    print("index")
except:
    print("some")

# Resposta: zero
