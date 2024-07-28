# Tuples e dicionários

# Remover o último item em um dicionário - método popitem()

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)   # outputs: {'cat': 'chat', 'dog': 'chien'}

# Em versões anteriores a 3.6.7 do Python o método popitem() remove um item aleatório de um dicionário
