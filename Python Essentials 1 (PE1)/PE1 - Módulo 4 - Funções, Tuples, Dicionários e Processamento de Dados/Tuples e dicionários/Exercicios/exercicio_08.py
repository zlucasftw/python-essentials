# Resumo da seccção - Key takeaways: dicionários (3/3)

# Exercício - 8

# Qual é o output do seguinte programa?

colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)

# Resposta: white : (255, 255, 255),
#           grey : (128, 128, 128),
#           red : (255, 0, 0),
#           green : 0, 128, 0
