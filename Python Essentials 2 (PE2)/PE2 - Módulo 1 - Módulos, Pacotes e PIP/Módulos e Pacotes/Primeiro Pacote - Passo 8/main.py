# Módulos e Pacotes

# Acessando a raíz da 'árvore' do pacote e ter acesso
# aos módulos sigma e tau

from sys import path

path.append('..\\packages')

import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())
