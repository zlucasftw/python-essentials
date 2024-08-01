# Resumo da seccção - Key takeaways: dicionários (2/3)

# 4. Para Adicionar ou remover uma chave (e o valor associado)

phonebook = {}      # an empty dictionary

phonebook["Adam"] = 3456783958      # create/add a key-value pair
print(phonebook)    # outputs: {'Adam': 3456783958}

del phonebook["Adam"]
print(phonebook)    # outputs: {}
