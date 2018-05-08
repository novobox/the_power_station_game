from classes.Game import Game
from classes.Station import Station
from classes.Player  import Player
from classes.PowPoint import PowPoint


def display_char_per_point(PowPoint):

    colors = {}
    default_color = '\033[34;5;200m'
    reset_color = '\033[0m'
    colors['magenta'] = {
        'active': '\033[38;5;206m',
        'deactive' : '\033[38;5;206m'
        }
    colors['orange'] = {
        'active': '\033[38;5;202m',
        'deactive' : '\033[38;5;202m',
        }

    colors['rouge'] = {
        'active' : '\033[0;1;101m',
        'deactive': '\033[31;1;107m',
        }
    colors['vert'] = {
        'active' : '\033[30;1;102m',
        'deactive': '\033[32;1;100m',
        }
        

    color = default_color
    char = '+'
    
    if PowPoint.state == 1:
        char = 'X'
    elif PowPoint.state == 2:
        char = '@'

    if PowPoint.player is not None:
        color = colors[PowPoint.player.color]['deactive']
        if PowPoint.activated:
            color = colors[PowPoint.player.color]['active']
    
    return " %s%s%s " % (color, char, reset_color)


def charge_grid_status(grid, moves):
    return False
    


def display_grid(grid, **kwargs):


    width = len(grid)    # 3 rows in your example
    height  = len(grid[0]) # 2 columns in your example

    
    display_grid = ''

    for i in range(width):
        row = ''
        for j in range(height):
            row += "%s" % display_char_per_point(grid[i][j])
        display_grid += "%s\n" % row

    return display_grid

    

def scneration01(game):

    #print(grid[14][20].posX)
    
    game.player_play_pow(1, 20, 14)
    game.player_play_pow(1, 22, 16)
    game.player_play_pow(1, 21, 17)
    game.player_play_pow(1, 22, 18)
    game.player_play_pow(1, 21, 19)

    game.activate_pow(21, 19)

    game.player_play_pow(2, 21, 14)
    game.player_play_pow(2, 20, 14)
    game.player_play_pow(2, 21, 15)
    game.player_play_pow(2, 20, 16)


    return False

###################################################

from cmd import Cmd

class MyPrompt(Cmd):

    def __init__(self):
        self.n_player = 0
        self.game = Game()

        scneration01(self.game)


        self.display_game()
        super(MyPrompt, self).__init__()
        self.do_pow('')

    def display_game(self):
        print(display_grid(self.game.grid))

    def do_pow(self, args):

        player = None
        
        self.n_player = (self.n_player % 2) + 1
        #n_player = input('Player (1 or 2): ')
        player = self.game.getplayer(int(self.n_player))

        pos = input("Player %s> X Y: " % player.id)

        posXY = pos.split(' ')
        posX = posXY[0]
        posY = posXY[1]

        self.game.player_play_pow(player.id, posX, posY)
            
        self.display_game()
        self.do_pow('')

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit



if __name__ == '__main__':
    p = MyPrompt()
    p.prompt = '>'
    p.cmdloop()
    #game()
