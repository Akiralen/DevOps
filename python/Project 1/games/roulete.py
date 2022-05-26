from games.gameABC import games


class game(games):
    dificulty = 0
    result = False
    
    def __init__(self):
        pass
    def __str__(self):
        return "Exchange Rate Roulete"
    def play(self):
        pass
    def printresult(self):
        if self.result :
            msg = "You WIN!!!"
        else :
            msg = "You LOOSE!!!"
        return msg
    
    