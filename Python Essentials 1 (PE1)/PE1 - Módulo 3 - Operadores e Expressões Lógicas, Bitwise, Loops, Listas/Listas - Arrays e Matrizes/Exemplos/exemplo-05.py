# Listas em aplicaçõess avançadas - Arrays

# Arrays tridimensionais

# Representação de um hotel

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Reservando um quarto no segundo edíficio, décimo andar, quarto 14
rooms[1][9][3] = True

# Desocupando o segudno quarto no quinto andar, primeiro edíficio
rooms[0][4][1] = False

# Verificar se há vagas no 15º andar, terceiro edifício

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print(vacancy)
