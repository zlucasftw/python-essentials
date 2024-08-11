# Módulos e Pacotes

# Acessando os módulos sigma e tau
# através da utilização de aliasing/alias

from sys import path

path.append('..\\packages')

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.funS())
print(alp.funA())
