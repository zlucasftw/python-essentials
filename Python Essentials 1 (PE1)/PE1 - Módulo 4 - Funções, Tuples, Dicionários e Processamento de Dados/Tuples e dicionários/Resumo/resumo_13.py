# Resumo da seccção - Key takeaways: dicionários (2/3)

# 3. Alterando o valor associado a uma chave específica

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]
print(item)     # outputs: lock
