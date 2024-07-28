# Tuples e dicionários

# Remover uma chave

# Remover uma chave sempre causa a remoção do valor associado.
# Valores não existem sem suas chaves.

# A remoção pode ser feita com a instrução del

# A remoção de uma chave não existente causa um erro.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)
