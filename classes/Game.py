from classes.Player  import Player
from classes.PowPoint import PowPoint
from classes.Station import Station

class Game(object):
    """
    Game = Une partie

    players
    moves
    grid
    stations

    """

    def __init__(self):
        
        self.player1 = Player(1, 'rouge')
        self.player2 = Player(2, 'vert')

        # Sauvegarde des points powered
        self.moves = []
        self.init_game()

        #self.display_game()

    def init_game(self):
        width = 30
        height = 50
    
        self.grid = []
        for j in range(height):
            row = []
            for i in range(width):
                point = PowPoint(i,j)
                row.append(point)
            self.grid.append(row)
    
    def player_play_pow(self, idplayer, X, Y):
        X = int(X)
        Y = int(Y)
        player = self.getplayer(idplayer)
        self.grid[Y][X].pow(player)
        self.moves.append(self.grid[Y][X])
    
    def activate_pow(self, X, Y):
        self.grid[Y][X].activate()

    def deactivate_pow(self, X, Y):
        self.grid[Y][X].deactivate()

    def getplayer(self, idplayer):
        if idplayer == 1:
            return self.player1
        elif idplayer == 2:
            return self.player2
