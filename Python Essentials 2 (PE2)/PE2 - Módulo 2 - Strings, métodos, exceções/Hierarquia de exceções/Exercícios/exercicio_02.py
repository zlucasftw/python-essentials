# Resumo da secção - Key takeaways

# Exercício 2

# Qual é o output esperado do seguinte código?

try:
    print(1/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

# Resposta: arith
