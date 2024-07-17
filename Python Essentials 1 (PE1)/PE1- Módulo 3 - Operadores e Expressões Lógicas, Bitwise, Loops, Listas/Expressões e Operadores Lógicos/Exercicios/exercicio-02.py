# Exercício 2

# Qual é o output do seguinte snippet?

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

# Resposta: 0, 5, 16, 9, 2, 16

# Respostas incorretas devido as operações ocorrerem a nível binário. 16 é -5 pois é apenas negado o seu valor
# em decimal mas a sua representação binária muda. 9 é 1 pois 4 // 3 = 1, e 2 é 1 pois 4 em binário é
# representado por 0000 0100 e a operação faz um left shift de 2 que seria 0000 0001 que seria 2 elevado a 0
# que tem o valor de 1.
