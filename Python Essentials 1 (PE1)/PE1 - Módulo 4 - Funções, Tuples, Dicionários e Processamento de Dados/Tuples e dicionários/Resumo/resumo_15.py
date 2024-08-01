# Resumo da seccção - Key takeaways: dicionários (2/3)

# 4.2 É possível inserir um item em um dicionário utilizando o método update()
# e remover o último elemento usando o método popitem()

pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary)   # outputs: {'kwiat', 'flower', 'gleba': 'soil'}

pol_eng_dictionary.popitem()
print(pol_eng_dictionary)       # outputs: {'kwiat', 'flower'}
