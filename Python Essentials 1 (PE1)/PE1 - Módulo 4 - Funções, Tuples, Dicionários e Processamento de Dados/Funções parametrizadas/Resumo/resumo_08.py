# Resumo da secção - Key takeaways

# Passagem de argumentos de keyword com pré-definição de valor para determinado argumento

def name(first_name, last_name="Smith"):
    print(first_name, last_name)


name("Andy")    # outputs: Andy Smith
name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")
