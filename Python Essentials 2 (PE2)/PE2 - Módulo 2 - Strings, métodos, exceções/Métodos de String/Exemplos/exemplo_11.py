# Métodos de String

# Método find()

# Pode-se utilizar o método find() para procurar
# todas as ocorrências de um caracter ou uma
# sequência de caracteres.

# Nesse caso será impresso os índices de todas as
# ocorrências de acordo com o argumento que foi passado.

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s
or earlier, when it was popularized by advertisements
for Letraset transfer sheets. It was introduced to
the Information Age in the mid-1980s by the Aldus Corporation,
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
