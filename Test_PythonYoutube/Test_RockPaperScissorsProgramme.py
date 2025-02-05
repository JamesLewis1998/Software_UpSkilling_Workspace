import pytest

from RockPaperScissorsExample_TestImport import get_choices

def get_choices():
    return RockPaperScissorsExample_TestImport.get_choices() / "player"

def Test_get_choices (monkeypatch):

    def Test_return():
        return RockPaperScissorsExample_TestImport()
    
    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr(RockPaperScissorsExample_TestImport,"get_choices", Test_return)

    # go about using input() like you normally would:
    Test_player_choice = get_choices(player)
    assert Test_player_choice == "rock"