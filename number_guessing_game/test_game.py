import pytest
from game import NumberGuessingGame
from player import Player

def test_game_initialization():
    player = Player("Tester")
    game = NumberGuessingGame(player)

    assert 1 <= game.secret_number <= 100, "Secret number should be within range 1-100"
