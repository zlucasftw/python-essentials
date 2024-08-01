# Resumo da seccção - Key takeaways: dicionários (2/3)

# 2. Para acessar um item de dicionário pode-se fazendo referência à sua chave
# ou usando o método get()

pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil",
    }

item_1 = pol_eng_dictionary["gleba"]    # ex.1
print(item_1)   # outputs: soil

item_2 = pol_eng_dictionary.get("woda")
print(item_2)
