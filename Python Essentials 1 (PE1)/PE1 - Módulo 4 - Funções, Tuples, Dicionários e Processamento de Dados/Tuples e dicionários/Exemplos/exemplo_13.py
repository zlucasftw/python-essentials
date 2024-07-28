# Tuples e dicionários - métodos

# Como usar um dicionário: Os métodos items() e values()

# Método items() - o método devolve/retorna tuples onde cada tuple é um par key-value

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)
