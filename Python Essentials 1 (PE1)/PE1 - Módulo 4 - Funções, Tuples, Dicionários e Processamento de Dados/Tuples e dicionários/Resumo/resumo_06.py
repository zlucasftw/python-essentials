# Resumo da seccção - Key takeaways: tuples (1/3)

# 5. Tuples são imutáveis, não pode-se alterar seus elementos
# Não se pode anexar tuples, modificar ou remover elementos de uma tuple

my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
my_tuple[2] = "guitar"      # The TypeError expection will be raised.
