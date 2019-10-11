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
        self.playable_points = []
        self.init_game()


    def init_game(self):
        width = 50
        height = 50
    
        self.grid = []
        for j in range(height):
            row = []
            for i in range(width):
                point = PowPoint(i,j)
                row.append(point)
            self.grid.append(row)

    def player_get_moves(self, idplayer, **kwargs):
        player = self.getplayer(idplayer)
        mode = 'all'
        if 'active_only' in kwargs:
            mode = 'active_only'
        player_moves = []
        for move in self.moves:
            if mode == 'active_only':
                if move.player == player and move.activated:
                    player_moves.append(move)
            else:
                if move.player == player:
                    player_moves.append(move)
        return player_moves

    def player_playables_powpoints(self, idplayer):
        player = self.getplayer(idplayer)
        pms = self.player_get_moves(idplayer, active_only=True)

        # Reset & Recalculate playable points
        for ppoint in self.playable_points:
            ppoint.playable = False
        self.playable_points = []

        for p in pms:
            #Search 8 points around
            around_points = [
                {
                    'X': p.posX - 1,
                    'Y': p.posY - 1,
                },
                {
                    'X': p.posX,
                    'Y': p.posY - 1,
                },
                {
                    'X': p.posX + 1,
                    'Y': p.posY - 1,
                },
                {
                    'X': p.posX - 1,
                    'Y': p.posY,
                },
                {
                    'X': p.posX + 1,
                    'Y': p.posY,
                },
                {
                    'X': p.posX - 1,
                    'Y': p.posY + 1,
                },
                {
                    'X': p.posX,
                    'Y': p.posY + 1,
                },
                {
                    'X': p.posX + 1,
                    'Y': p.posY + 1,
                },
                ]
            for apoint in around_points:
                g_apoint = self.grid[apoint['Y']][apoint['X']]
                if g_apoint.state < 2 and g_apoint.player != player:
                    self.grid[apoint['Y']][apoint['X']].playable = True
                    self.playable_points.append(self.grid[apoint['Y']][apoint['X']])

        return self.playable_points

    
    def player_play_pow(self, idplayer, X, Y):
        X = int(X)
        Y = int(Y)
        player = self.getplayer(idplayer)
        self.player_playables_powpoints(idplayer)
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
