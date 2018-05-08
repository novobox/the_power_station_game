class Station(object):
    """
    Station = La centrale
    posX: Position X haut gauche sur la grille
    posY: Position Y haut gauche sur la grille
    Width: Taille X
    Height: Taille Y
    """
    
    def __init__(self, posX, posY, Width, Height):
        self.posX = posX
        self.posY = posY
        self.Width = Width
        self.Height = Height
    
