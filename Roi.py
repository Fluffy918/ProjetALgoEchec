from Piece import Piece

class Roi(Piece):
    def __init__(self, couleur, ligne, col):
        super().__init__(couleur, ligne, col)
        self.nom = "roi"

    def deplacements_valides(self, plateau):
        deplacements = []
        directions = [
                (-1, -1), (-1, 0),
                (-1, 1), (0, -1),
                (0, 1), (1, -1),
                (1, 0), (1, 1)]

        for dx, dy in directions:
            x, y =self.ligne + dx, self.col +dy
            if 0 <= x < 8 and 0 <= y < 8:
                piece = plateau[x][y]
                if piece is None or piece.couleur != self.couleur:
                    deplacements.append((x, y))

        return deplacements