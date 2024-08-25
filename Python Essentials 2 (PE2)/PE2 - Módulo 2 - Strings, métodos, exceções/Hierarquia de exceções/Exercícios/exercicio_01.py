# Resumo da secção - Key takeaways

# Exercício 1

# Qual é o output esperado do seguinte código?

try:
    print(1/0)
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arith")
except:
    print("some")

# Resposta: zero
