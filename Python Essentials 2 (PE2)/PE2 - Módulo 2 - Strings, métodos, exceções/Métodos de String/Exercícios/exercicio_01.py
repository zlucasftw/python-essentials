# Resumo da seccção - Key takeaways

# Exercício 1

# Qual é o output esperado do seguinte código?

for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')

# Resposta: ABC123xyx
