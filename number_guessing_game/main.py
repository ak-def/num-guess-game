from game import NumberGuessingGame
from player import Player

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    game = NumberGuessingGame()
    game.play(player)
