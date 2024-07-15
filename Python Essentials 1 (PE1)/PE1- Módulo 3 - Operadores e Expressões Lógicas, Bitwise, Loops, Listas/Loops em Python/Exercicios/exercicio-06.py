# Exercício 6

# Qual é o output do seguinte código?

n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

# Resposta: -1, 0, 1, 2, 2
# Resposta correta: -1, 0, 1, 2, 3, isso pelo fator de que a variável 'num' está
# dentro da estrutura de repetição for utilizada na função print mas realizando
# a subtração por 1. Como a variável 'n' carrega os valores de 0 até 3, o else vai
# ser executado assim que o loop terminar e a variável 'num' não vai ter seu valor
# alterado, apenas mostrar seu último valor da variável que é 3.
