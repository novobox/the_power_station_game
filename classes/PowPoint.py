class PowPoint(object):
    """PowPoint = Point de la grille electrisable, définie par:
    posX: Position X sur la grille
    posY: Position Y sur la grille
    state: Etat (0: Vide / 1: Electrisé / 2: Surchargée
    player: Id du joueur en possession du point
    activated: BoOl, False: Desactivé, True activé
    """
    
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.clearPoint()
    
    def clearPoint(self):
        self.state = 0
        self.player = None
        self.playable = False
        self.activated = False

    def activate(self):
        self.activated = True
    def deactivate(self):
        self.activated = False

    def pow(self, Player):
        if(self.state < 2):
            self.state += 1
            self.player = Player
            return True
        return False
    
    def __str__(self):
        return "O"
