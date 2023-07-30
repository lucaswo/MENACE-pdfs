class Board:
    def __init__(self):
        self.board = [0] * 9

    def __getitem__(self, n):
        return self.board[n]

    def __setitem__(self, n, value):
        self.board[n] = value

    def __str__(self):
        return "\n".join([
            "".join([[" ", "o", "x", "■"][j] for j in self.board[3*i:3*i+3]])
            for i in range(3)
        ])

    def in_set(self, set):
        set = [s.n() for s in set]
        for a in self.permutations():
            if a in set:
                return True
        return False

    def is_max(self):
        return self.n() == max(self.permutations())

    def permutations(self):
        out = []
        for rot in [
            (0, 1, 2, 3, 4, 5, 6, 7, 8), (2, 5, 8, 1, 4, 7, 0, 3, 6),
            (8, 7, 6, 5, 4, 3, 2, 1, 0), (6, 3, 0, 7, 4, 1, 8, 5, 2),
            (2, 1, 0, 5, 4, 3, 8, 7, 6), (8, 5, 2, 7, 4, 1, 6, 3, 0),
            (6, 7, 8, 3, 4, 5, 0, 1, 2), (0, 3, 6, 1, 4, 7, 2, 5, 8)
        ]:
            out.append(self.nrot(rot))
        return out

    def has_winner(self):
        for i, j, k in [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
            (2, 5, 8), (0, 4, 8), (2, 4, 6)
        ]:
            if self[i] != 0 and self[i] == self[j] == self[k]:
                return True
        return False

    def n(self):
        return self.nrot(list(range(9)))

    def nrot(self, rot):
        out = 0
        for i in range(9):
            out += 3 ** i * self[rot[i]]
        return out

    def as_latex(self):
        out = "\\begin{tikzpicture}\n"
        out += "\\clip (3.75mm,-1mm) rectangle (37.25mm,30mm);\n"
        out += "\\draw[gray] (5mm,9mm) -- (36mm,9mm);\n"
        out += "\\draw[gray] (5mm,20mm) -- (36mm,20mm);\n"
        out += "\\draw[gray] (5mm,0mm) -- (5mm,30mm);\n"
        out += "\\draw[gray] (36mm,0mm) -- (36mm,30mm);\n"

        out += "\\draw (16mm,13mm) -- (25mm,13mm);\n"
        out += "\\draw (16mm,16mm) -- (25mm,16mm);\n"
        out += "\\draw (19mm,10mm) -- (19mm,19mm);\n"
        out += "\\draw (22mm,10mm) -- (22mm,19mm);\n"

        for i, c in enumerate([
            (17.5, 11.5), (20.5, 11.5), (23.5, 11.5),
            (17.5, 14.5), (20.5, 14.5), (23.5, 14.5),
            (17.5, 17.5), (20.5, 17.5), (23.5, 17.5)
        ]):
            if self[i] == 1:
                # o
                out += f"\\draw ({c[0]}mm,{c[1]}mm) circle (0.9mm);\n"
            if self[i] == 2:
                # x
                out += (f"\\draw ({c[0]-1}mm,{c[1]-1}mm)"
                        f" -- ({c[0]+1}mm,{c[1]+1}mm);\n"
                        f"\\draw ({c[0]-1}mm,{c[1]+1}mm)"
                        f" -- ({c[0]+1}mm,{c[1]-1}mm);\n")
            if self[i] == 3:
                # ■
                out += f"\\node[draw,fill=black,shape=rectangle,minimum height=1.8mm,minimum width=1.8mm,inner sep=0] at ({c[0]}mm,{c[1]}mm) {{}};\n"

        out += "\\end{tikzpicture}\n"
        out += "\\hspace{-5mm}"
        return out
