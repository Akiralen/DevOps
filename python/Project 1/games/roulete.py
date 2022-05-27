import logging
from gameABC import games


class game(games):
    dificulty = 0
    result = False
    
    def __init__(self):
        pass
    
    def __str__(self):
        return "Roulete Game"
    
    def print_instructions(self):
        pass
   
    def print_result(self):
        if self.result :
            msg = "You WIN!!!"
        else :
            msg = "You LOOSE!!!"
        return msg
    
    def play(self,name):
        self.result = True
        print('You played Roulet Game')
        
def main():
    g = game()
    name = 'Test'
    dificulty = 1
    g.set_dificulty(dificulty)
    g.play(name)
    print(g.print_result())
    
if __name__ == '__main__':
    #run game
    main()
else:
    logging.info('Module "roulete.py" loaded')

        
  
    