# Resumo da seccção - Key takeaways

# Listas nested para criar matrizes ou listas bidimensionais

# A four-column/four-row table - a two-dimensional array (4x4)

table = [[":(", ":)", ":(", ":)",],
         [":)", ":(", ":)", ":(",],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'
