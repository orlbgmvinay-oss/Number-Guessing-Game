import random
from typing import Dict, List

class Game:
    def __init__(self, levels: List[int]=None, level_names: List[str]=None):
        self.levels = levels or [10, 50, 100, 1000]
        self.level_names = level_names or ["EASY", "MEDIUM", "HARD", "IMPOSSIBLE"]
        self.level_index = 0
        self.number = None
        self.attempts = 0
        self._start_level()

    def total_levels(self) -> int:
        return len(self.levels)

    def _start_level(self):
        max_num = self.current_max()
        self.number = random.randint(1, max_num)

    def start_new_game(self):
        self.level_index = 0
        self.attempts = 0
        self._start_level()

    def current_max(self) -> int:
        return self.levels[self.level_index]

    def current_name(self) -> str:
        return self.level_names[self.level_index]

    def check_guess(self, guess: int) -> Dict:
        """Return dict with keys:
           result: 'correct'|'high'|'low'
           level_up: bool
           completed: bool
           attempts: int
        """
        self.attempts += 1
        if guess == self.number:
            if self.level_index < len(self.levels) - 1:
                self.level_index += 1
                self._start_level()
                return {"result": "correct", "level_up": True, "completed": False, "attempts": self.attempts}
            else:
                return {"result": "correct", "level_up": False, "completed": True, "attempts": self.attempts}
        elif guess > self.number:
            return {"result": "high", "level_up": False, "completed": False, "attempts": self.attempts}
        else:
            return {"result": "low", "level_up": False, "completed": False, "attempts": self.attempts}

    # helper for tests to set the target number deterministically
    def _set_number_for_test(self, value: int):
        self.number = value
