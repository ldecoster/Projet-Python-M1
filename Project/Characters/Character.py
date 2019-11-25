class Character:
    def __init__(self, gold=None):
        if gold is None:
            self.gold = 0
        else:
            self.gold = gold
