from Piece import Piece

class Pion(Piece):
    def __init__(self, couleur, ligne, col):
        super().__init__(couleur, ligne, col)
        self.nom = "pion"

    def deplacements_valides(self, plateau):
        moves = []
        direction = -1 if self.couleur == "blanc" else 1
        start_row = 6 if self.couleur == "blanc" else 1

        # Avancer d'une case
        if plateau[self.ligne + direction][self.col] is None:
            moves.append((self.ligne + direction, self.col))
            # Avancer de deuc si au départ
            if self.ligne == start_row and plateau[self.ligne + 2 * direction][self.col] is None:
                moves.append((self.ligne + 2 * direction, self.col))

        # Prises en diagonale
        for dy in [-1, 1]:
            x = self.ligne + direction
            y = self.col + dy
            if 0 <= x < 8 and 0 <= y < 8:
                piece = plateau[x][y]
                if piece is not None and piece.couleur != self.couleur:
                    moves.append((x, y))

        return moves