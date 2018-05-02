class Player(object):
    """
    Player = Le Joueur
    id: Id player
    PowStation: Centrale du joueur
    PowPoints: Points possédés du joueur
    RoundPoints: Nombre de Points à placer restant (pour un tour)
    Round : Round actuel XXX: utile ?
    """
    
    def __init__(self, idplayer):
        self.id = idplayer
        #self.PowPoints = []

    #def spawn_station(self, SpawnStation):
    #    self.PowStation = SpawnStation        
        
    #def pow_point(self, PowPoint):
    #    self.PowPoints.append(PowPoint)
