# Resumo da secção - Key takeaways

# Exercício 3

# Qual é o output esperado do seguinte código?

def foo(x):
    assert x
    return 1/x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")

# Resposta: AssertError

# Resposta correta: some
