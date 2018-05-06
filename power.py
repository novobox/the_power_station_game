from classes.PowPoint import PowPoint
from classes.Player  import Player
from classes.PowStation import PowStation


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


#def charge_grid_status(grid):
    
    


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

    

def game():

    #player1 = Player(1, 'magenta')
    #player2 = Player(2, 'orange')
    player1 = Player(1, 'rouge')
    player2 = Player(2, 'vert')
    
    # INIT map
    
    width = 30
    height = 50
    
    grid = []
    for j in range(height):
        row = []
        for i in range(width):
            point = PowPoint(i,j)
            row.append(point)
        grid.append(row)
    

    scneration01(grid, player1, player2)

    print(display_grid(grid))





def scneration01(grid, player1, player2):

    print(grid[14][20].posX)

    grid[14][20].pow(player1)
    grid[16][22].pow(player1)
    grid[17][21].pow(player1)
    grid[18][22].pow(player1)
    grid[19][21].pow(player1)
    grid[15][21].pow(player1)



    grid[14][21].pow(player2)
    grid[14][20].pow(player2)
    grid[15][20].pow(player2)
 
    grid[15][21].pow(player2)



    return False

###################################################

from cmd import Cmd

class MyPrompt(Cmd):

    def __init__(self):
        
        self.n_player = 0
        self.player1 = Player(1, 'rouge')
        self.player2 = Player(2, 'vert')

        self.init_game()

        scneration01(self.grid, self.player1, self.player2)


        self.display_game()
        super(MyPrompt, self).__init__()



        self.do_pow('')

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

    def display_game(self):
        print(display_grid(self.grid))
        

    def do_pow(self, args):

        player = None
        
        self.n_player = (self.n_player % 2) + 1
        #n_player = input('Player (1 or 2): ')
        if int(self.n_player) == 1:
            player = self.player1
        elif int(self.n_player) == 2:
            player = self.player2

        #self.prompt = "Player %s>" % player.id


        pos = input("Player %s> X Y: " % player.id)

        posXY = pos.split(' ')
        posX = posXY[0]
        posY = posXY[1]


        #if int(n_player) == 1:
        #    player = self.player1
        #elif int(n_player) == 2:
        #    player = self.player2

        self.grid[int(posY)][int(posX)].pow(player)
            
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
