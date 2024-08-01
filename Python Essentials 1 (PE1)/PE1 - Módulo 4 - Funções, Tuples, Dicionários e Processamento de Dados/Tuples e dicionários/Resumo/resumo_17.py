# Resumo da seccção - Key takeaways: dicionários (2/3)

# 6. Percorrendo as chaves e valores de um dicionário com o método items()

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)
