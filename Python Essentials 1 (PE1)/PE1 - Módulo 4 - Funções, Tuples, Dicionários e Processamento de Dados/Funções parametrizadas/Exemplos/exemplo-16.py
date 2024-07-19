# Como as funções comunicam com o seu ambiente

# Funções parametrizadas - mais detalhes

# Argumentos com valor padrão/predefinido que são levados em consideração quando omitidos

def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction("Henry")
introduction(first_name="William")
