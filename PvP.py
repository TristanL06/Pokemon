class Battle:
    def __init__(self, Player1, Player2): #Init
        self.Player1 = Player1 #Player 1 (Player)
        self.Player2 = Player2 #Player 2 (Player)
    def __str__(self):
        return f"{str(self.Player1)} \n vs \n {str(self.Player2)}"

    #All Accsessors
    def get_Player1(self):
        return self.Player1
    def get_Player2(self):
        return self.Player2
    #Methods
    def start(self):
        pass


