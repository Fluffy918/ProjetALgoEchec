from Piece import Piece

class Tour(Piece):
    def __init__(self, couleur, ligne, col):
        super().__init__(couleur, ligne, col)
        self.nom = "tour"

    def deplacements_valides(self, plateau):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            x, y = self.ligne, self.col
            while True:
                x += dx
                y += dy
                if 0 <= x < 8 and 0 <= y < 8:
                    piece = plateau[x][y]
                    if piece is None:
                        moves.append((x, y))
                    elif piece.couleur != self.couleur:
                        moves.append((x, y))
                        break
                    else:
                        break
                else:
                    break
        return moves