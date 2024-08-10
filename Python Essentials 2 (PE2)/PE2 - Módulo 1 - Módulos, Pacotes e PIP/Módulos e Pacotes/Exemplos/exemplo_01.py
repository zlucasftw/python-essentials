# Módulos e pacotes

# Variável path - lista que armazena pastas e diretórios
# com propósito de encontrar um módulo solicitado pela
# instrução de importação. Se o módulo não poder ser
# encontrado na lista a importação falha.

import sys

for p in sys.path:
    print(p)
