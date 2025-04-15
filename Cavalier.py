from Piece import Piece

class Cavalier(Piece):
    def __init__(self, couleur, ligne, col):
        super().__init__(couleur, ligne, col)
        self.nom = "cavalier"

    def deplacements_valides(self, plateau):
        moves = []
        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]
        for dx, dy in directions:
            x, y = self.ligne + dx, self.col + dy
            while True:
                x += dx
                y += dy
                if 0 <= x < 8 and 0 <= y < 8:
                    piece = plateau[x][y]
                    if piece is None or piece.couleur != self.couleur:
                        moves.append((x, y))
        return moves