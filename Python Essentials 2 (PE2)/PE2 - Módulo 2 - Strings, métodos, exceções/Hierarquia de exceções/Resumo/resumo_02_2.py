# Resumo da secção - Key takeaways

# 2.2. Não se deve colocar exceções mais concretas antes das
# mais gerais da mesma sequência de ramificações 'except'.
# A não ser que se queira ter uma parte do código
# que vai ser inalcançável.

try:
    # Risky code.
except LookupError:
    # Dealing with erroneous lookups
except IndexError:
    # You'll never get here
