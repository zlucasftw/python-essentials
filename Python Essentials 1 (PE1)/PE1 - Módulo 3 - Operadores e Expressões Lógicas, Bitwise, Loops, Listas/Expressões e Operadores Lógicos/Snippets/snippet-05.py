# Operações de lógica e de bit em Python - Operadores bitwise

flag_register = 0x1234

# flag_register = 0000000000000000000000000000x000

# x & 1 = x
# x & 0 = 0

# 00000000000000000000000000001000 se o bit foi definido para 1
# 00000000000000000000000000000000 se o bit foi definido para 0

the_mask = 8

# if flag_register & the_mask:
    # My bit is set.
# else:
    # My bit is reset.

# 11111111111111111111111111110111

# flag_register = flag_register & ~the_mask
flag_register &= ~the_mask

# x | 1 = 1
# x | 0 = x

# flag_register = flag_register | the_mask
flag_register != the_mask

# x ^ 1 = ~x
# x ^ 0 = x

# flag_register = flag_register ^ the_mask
flag_register ^= the_mask