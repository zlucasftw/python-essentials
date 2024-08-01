# Resumo da seccção - Key takeaways: dicionários (2/3)

# 8. Pode-se utilizar a keyword del para remover um item/elemento ou chave-valores específico, ou apagar um dicionário
# Para remover todos os itens/elementos ou chave-valores de um dicionário é necessário utilizar o método clear()

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil",
    }

print(len(pol_eng_dictionary))      # outputs: 3
del pol_eng_dictionary["zamek"]     # remove an item
print(len(pol_eng_dictionary))      # outputs: 2

pol_eng_dictionary.clear()          # removes all the items
print(len(pol_eng_dictionary))      # outputs: 0

del pol_eng_dictionary              # removes the dictionary
