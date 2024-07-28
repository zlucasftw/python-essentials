# Tuples e dicionários - métodos

# Como usar um dicionário: keys()

# Dicionários podem ser consultados utilizando o loop for com o método keys() possuído pelo dicionário

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
