class Character:
    def __init__(self, gold=0):
        self.gold = gold

    def add_gold(self, gold):
        self.gold += gold
        return True

    def withdraw_gold(self, gold):
        if self.gold - gold >= 0:
            self.gold -= gold
            return True
        else:
            raise GoldError("Not enough gold")


class GoldError(Exception):
    def __init__(self, message):
        self.message = message
