# Listas em aplicações avançadas - Arrays

# Listas em listas: Arrays bidimensionais - Matriz

# Tabuleiro de xadrez

EMPTY = "-"
ROOK = "ROOK"
KNIGHT = "KNIGHT"
PAWN = "PAWN"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

# Adicionando todas as torres no tabuleiro

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

# Adicionando um cavalo (knight) ao C4
board[4][2] = KNIGHT

# Adicionando um peão (pawn) para E5
board[3][4] = PAWN

print(board)
