# Exceções úteis

# Exceções integradas - ImportError

# Localização: BaseException <- Exception <- StandardError <- ImportError

# É uma exceção concreta levantada quando uma operação de importação falha

# One of these imports will fail - which one?

try:
    import math
    import time
    import abracadabra

except:
    print('One of your imports has failed')
