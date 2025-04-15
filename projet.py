from Piece import Piece
from Pion import Pion
from Tours import Tour
from Cavalier import Cavalier
from Fou import Fou
from Reine import Reine
from Roi import Roi

def generer_coups_possibles(board, couleur_joueur):
  coups_possibles = []

  for ligne in range(8):
    for col in range(8):
      piece = board[ligne][col]
      if piece is not None and piece.couleur == couleur_joueur:
        deplacements = piece.deplacements_valides(board)
        for (to_row, to_col) in deplacements:
          coups_possibles.append((ligne, col, to_row, to_col))
  return coups_possibles

# ----------------------------------------------------------- #

def create_board():
  board = [[None for _ in range(8)] for _ in range(8)]

  # Remplir les pièces noires
  board[0]= [
      Tour("noir", 0, 0), Cavalier("noir", 0, 1), Fou("noir", 0, 2), Reine("noir", 0, 3),
        Roi("noir", 0, 4), Fou("noir", 0, 5), Cavalier("noir", 0, 6), Tour("noir", 0, 7)
  ]
  board[1]= [Pion("noir", 1, i) for i in range(8)]

  # Remplire els pièces blanches
  board[6]= [Pion("blanc", 1, i) for i in range(8)]
  board[7]= [
      Tour("blanc", 7, 0), Cavalier("blanc", 7, 1), Fou("blanc", 7, 2), Reine("blanc", 7, 3),
        Roi("blanc", 7, 4), Fou("blanc", 7, 5), Cavalier("blanc", 7, 6), Tour("blanc", 7, 7)
  ]

  return board

def print_board(board):
  print("    A   B   C   D   E   F   G   H")
  print("  +" + "---+" * 8)
  for i, row in enumerate(board):
    print(8 - i, end=' |')
    for piece in row:
      if piece is None:
        print('', end='')
      else:
        lettre = piece.nom[0].upper()
        couleur = 'B' if piece.couleur == 'blanc' else 'N'
        print(f" {lettre}{couleur}", end=' ')
    print()
    print("  +" + "---+" * 8)
  

board = create_board()
print_board(board)

def play_game():
  board = create_board()
  turn = 'B' # B pour blanc, N pour noir

  while True:
    print_board(board)
    print(f"C'est au tour des {'blanc' if turn == 'B' else 'noirs'}.")

    # Ici, la logique pour choisir un coup
    # arrête la boucle
    cmd = input("Entrée pour continuer, 'q' pour quitter:")
    if cmd == 'q':
      break

    # Alterner les tours
    turn = 'N' if turn == 'B' else 'B'
  print("Fin du jeu")
play_game()

coups_blancs = generer_coups_possibles(board, 'blanc')
print("Coups possibles pour les blancs :")
for coup in coups_blancs:
    print(coup)

coups_noirs = generer_coups_possibles(board, 'noir')
print("Coups possibles pour les coups_noirs :")
for coup in coups_noirs:
    print(coup)

# ----------------------------------------------------------- #

def evaluer_plateau(board):
  valeurs = {
      'pion': 1,
      'cavalier': 3,
      'fou': 3,
      'tour': 5,
      'reine': 9,
      'roi': 1000
  }

  score = 0

  for row in board:
    for piece in row:
      if piece is not None:
        valeur = valeurs.get(piece.nom, 0)
        if piece.couleur == 'blanc':
          score += valeur
        else:
          score -= valeur
  return score

# ----------------------------------------------------------- #

def pos_to_coords(pos):
  col = ord(pos[0].upper()) - ord('A')
  row = 8 - int(pos[1])
  return row, col

def move_piece(board, from_pos, to_pos):
  from_row, from_col = pos_to_coords(from_pos)
  to_row, to_col = pos_to_coords(to_pos)

  piece = board[from_row][from_col]

  if piece == None:
    print("Aucune pièce à cette position.")
    return False

  # Obtenir les mouvements valides de la pièce
  valid_moves = piece.deplacements_valides(board)

  if (to_row, to_col) not in valid_moves:
    print("Ce mouvement n'est pas valide.")
    return False

  # Mise à jour des coordonnées internes de la pièce
  piece.ligne, piece.col = to_row, to_col

  # Déplace la pièce
  board[from_row][from_col] = None
  board[to_row][to_col] = piece

  return True

