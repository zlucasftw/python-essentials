# A anamotia das exceções

# Exceções

# A exceção ArithmeticError é uma classe geral que inclui,
# entre outros a exceção ZeroDivisionError.
# Isso significa que a Exceção sempre cai primeiro no
# que corresponde-a, não tendo a necessidade de especificar
# de maneira exata a exceção, apenas uma mais geral ou mais
# abstrata que a exceção que pode ser disparada.

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")
