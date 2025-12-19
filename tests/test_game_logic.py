import pytest
from game_logic import Game

def test_game_progression_and_attempts():
    g = Game(levels=[10, 20], level_names=["L1", "L2"])
    g.start_new_game()
    # make first level deterministic
    g._set_number_for_test(5)
    r = g.check_guess(3)
    assert r["result"] == "low"
    assert g.attempts == 1

    r = g.check_guess(5)
    assert r["result"] == "correct"
    assert r["level_up"] is True
    assert g.level_index == 1
    assert g.attempts == 2

    # second level
    g._set_number_for_test(7)
    r = g.check_guess(7)
    assert r["result"] == "correct"
    assert r["completed"] is True
    assert g.attempts == 3

def test_attempts_increment_on_wrong_guess():
    g = Game(levels=[10])
    g.start_new_game()
    g._set_number_for_test(1)
    r = g.check_guess(2)
    assert r["result"] == "high"
    assert g.attempts == 1