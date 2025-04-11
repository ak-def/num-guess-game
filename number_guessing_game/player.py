class Player:
    def __init__(self, name):
        self.name = name
    
    def guess_number(self):
        return int(input(f"{self.name}, enter your guess: "))
    @staticmethod
    def win_closeness(a,b):
        space = abs(a-b)
        return space

