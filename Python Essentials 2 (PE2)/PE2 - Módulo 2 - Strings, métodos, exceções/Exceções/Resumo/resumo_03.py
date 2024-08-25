# Resumo da seccção - Key takeaways

# 3. O except não especificado ou geral só pode ser
# acrescentado uma vez e no final após de todos
# os ramos de exceções especificados.

:
# The code that always runs smoothly.
:
try:
    :
    # Risky code.
    :
except Except_1:
    # Crisis management takes place here.
except Except_2:
    # We save the world here.
except:
    # All other issues fall here.
:
# Back to normal.
:
