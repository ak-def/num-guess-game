import random

class NumberGuessingGame:
    def __init__(self, start=1, end=10):
        self.start = start
        self.end = end
        self.target = random.randint(self.start, self.end)
        self.attempts = 0
    
    def play(self, player):
        print("welcome to guess game:")
        print(f"guess the number {self.start} and {self.end}")
        choice = player.guess_number()

        if choice == self.target:
            print(f"Congratulations {player.name}, you won!!")
        else:
            print(f"Sorry {player.name}, you lost.") # The correct number was {self.target}.")
            print(f"Very Close , missed out by -", player.win_closeness(choice, self.target))


