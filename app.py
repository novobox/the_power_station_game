from flask import Flask, request, render_template, redirect, send_from_directory
from classes.Game import Game


app = Flask(__name__,
            static_url_path='/js',
            static_folder='templates/js/',
            template_folder='templates/')

class Init(object):
    def __init__(self):
        self.player_id = 0

game = Game()
init = Init()

def initgame():

    if init.player_id != 0:
        return True

    init.player_id = 1
    
    # INIT
    ## INIT player 1
    y=0
    while y < 24:
        for x in range(25, 27):
            game.player_play_pow(1, x, y)
            y += 1


    ## INIT player 2            
    y=49
    while y > 23:
        for x in range(25, 27):
            game.player_play_pow(2, x, y)
            y -= 1
            
    ## Player 2 début des hostilités        
    game.player_play_pow(2, 26, 23)
    game.player_play_pow(2, 25, 22)


    ## Player 1 se défend
    game.player_play_pow(1, 26, 22)
    game.player_play_pow(1, 25, 23)
    game.player_play_pow(1, 26, 24)

    ## Desactivation manuelle des 2 trucs...
    game.grid[23][26].deactivate()
    game.grid[25][22].deactivate()        
    

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/', methods=['GET', 'POST'])
def index():
    initgame()
    data = ''
    if request.method == 'POST':
        data = request.form
        game.player_play_pow(init.player_id, data['x'], data['y'])
        
    if init.player_id == 2:
        init.player_id = 1
    else:
        init.player_id = 2
        
    return render_template('grid.html', grid=game.grid, player_id=init.player_id, data=data)

@app.route('/add_point', methods=['GET', 'POST'])
def add_point():
    game.player_play_pow(2, 29, 22)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
