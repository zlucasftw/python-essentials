# Resumo da seccção - Key takeaways

# 2. Caso seja necessário tratar mais de um tipo de exceção
# proveniente do mesmo ramo do try, pode-se adicionar mais
# do que um ramo except, onde é necessário rotulá-los.
# O que deve ser levado em consideração é que, apenas
# um ou no máximo um dos ramos expect é executado.
# E nenhum dos ramos é executado quando a exceção levantada
# não coincide com as exceções especificadas.

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
:
# Back to normal.
:
