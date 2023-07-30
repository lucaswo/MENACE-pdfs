import os
from itertools import permutations
from menace import Board
from latex import preamb, postamb

positions = [[], []]

for t1, t2, t3, t4 in permutations(range(9), 4):
    board = Board()
    board[t1] = 3
    board[t2] = 3
    board[t3] = 3
    board[t4] = 3
    if board.is_max() and not board.in_set(positions[0]):
        positions[0].append(board)

for t1, t2, t3, t4, t5, t6 in permutations(range(9), 6):
    board = Board()
    board[t1] = 3
    board[t2] = 3
    board[t3] = 3
    board[t4] = 3
    board[t5] = 3
    board[t6] = 3
    if board.is_max() and not board.in_set(positions[1]):
        positions[1].append(board)


assert len(positions[0]) == 23
assert len(positions[1]) == 16
assert sum([len(p) for p in positions]) == 39

latex = preamb
i = 0
for boards in positions:
    for board in boards:
        latex += board.as_latex()
        latex += "\n"
        if (i + 1) % 6 == 0:
            latex += "\\vspace{-1mm}\n\n\\noindent"
        i += 1
latex += postamb
print(latex)
with open(f"output/placeholders.tex", "w") as f:
    f.write(latex)
