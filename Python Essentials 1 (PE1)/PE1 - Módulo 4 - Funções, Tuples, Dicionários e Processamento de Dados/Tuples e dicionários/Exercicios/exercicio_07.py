# Resumo da seccção - Key takeaways: dicionários (3/3)

# Exercício - 7

# O que acontecerá quando executar o seguinte código?

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)

# Resposta: {'A': 1, 'B': 2} - O dicionário original foi copiado para outro dicionário que vai possuir o mesmo
# conteúdo do dicionário original. Logo, ao apagar o conteúdo completo do dicionário original, imprimir sua
# cópia não dará nenhum erro assim como terá o conteúdo do dicionário original que agora foi apagado.
