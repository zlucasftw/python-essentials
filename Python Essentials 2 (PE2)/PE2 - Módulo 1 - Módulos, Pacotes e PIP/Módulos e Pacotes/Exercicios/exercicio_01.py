# Resumo da seccção - Key takeaways

# Exercício 1

# Pretende impedir o utilizador do seu módulo de executar o seu código como um script comum.
# Como conseguirá tal efeito?

# Resposta:

# if __name__ == "__main__":
#    print()


# Resposta correta: Verifica se o diretório que está sendo executado é o
# do módulo e, se sim, mostra uma mensagem na tela e utiliza
# a instrução sys.exit() para parar a execução.

import sys

if __name__ == "__main__":
    print("Don't do that!")
    sys.exit()
