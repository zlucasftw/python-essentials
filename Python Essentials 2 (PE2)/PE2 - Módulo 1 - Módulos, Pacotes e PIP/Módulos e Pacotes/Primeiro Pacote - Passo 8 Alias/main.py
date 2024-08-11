# Módulos e Pacotes

# Acessando a raíz da 'árvore' do pacote e ter acesso
# aos módulos sigma e tau utilizando aliasing/alias

from sys import path

path.append('..\\packages')

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.funS())
print(alp.funA())
