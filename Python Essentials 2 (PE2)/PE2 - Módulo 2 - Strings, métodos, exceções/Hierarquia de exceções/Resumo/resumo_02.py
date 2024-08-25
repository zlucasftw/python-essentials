# Resumo da secção - Key takeaways

# 2. Todas exceções no Python pré-definidas formam um hierarquia, sendo algumas mais gerais
# e outras mais ou menos concretas. Não se deve colocar exceções mais concretas antes das
# mais gerais da mesma sequência de ramificações 'except'.

try:
    # Risky Code.
except IndexError:
    # Taking care of mistreated lists
except LookupError:
    # Dealing with other erroneous lookups
