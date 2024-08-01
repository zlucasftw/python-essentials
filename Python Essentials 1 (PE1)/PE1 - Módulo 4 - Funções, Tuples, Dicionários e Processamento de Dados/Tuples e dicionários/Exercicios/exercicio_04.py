# Resumo da seccção - Key takeaways: dicionários (3/3)

# Exercício - 4

# Escreva um programa que irá "colar" os dois dicionários (d1 e d2) e criar um novo (d3).

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)     # Write your code here.

print(d3)
