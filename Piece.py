class Piece:
    def __init__(self, couleur, ligne, col):
        self.couleur = couleur
        self.ligne = ligne
        self.col = col
        self.nom = 'piece'


    def deplacements_valides(self, plateau):
        return []

    def get_position(self):
        return self.ligne, self.col

    def set_position(self, ligne, col):
        self.ligne = ligne
        self.col = col