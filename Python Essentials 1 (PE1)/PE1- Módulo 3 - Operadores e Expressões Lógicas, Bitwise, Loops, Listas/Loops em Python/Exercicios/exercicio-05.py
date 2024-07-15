# Exercício 5

# Qual é o output do seguinte código?

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

# Resposta: 4, 3, 2, 1
# Resposta correta: 4, 3, 2, 0 - A variável n vai de 3 a 0 e
# no print interno no while esta sendo utilizada com + 1
# entretanto quando o while para sua execução que é quando
# n atinge 0, se vai para o else e ai então é printado 0
# e não 1 pois não é o valor da variável n.
