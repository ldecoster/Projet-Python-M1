import random
from Project.Items.RandomItem import RandomItem
from Project.Characters.Fighter import Fighter


class Monster(Fighter):
    def __init__(self, level):
        gold = int(level * random.randint(1, 5))  # max = 50 for level 10
        life_points = int(1 + (level / 2) * random.randint(10, 30))  # max = 150 level 10
        max_life_points = life_points
        protection_points = int(1 + (level / 2) * random.randint(5, 15))  # max = 75 for level 10
        dodge_rate = round(1 + (level / 2) * random.random() * 3, 2)  # max = 15 for level 10
        parry_rate = round(1 + (level / 2) * random.random() * 3, 2)  # max = 15 for level 10
        critical_hit_rate = round(1 + (level / 2) * random.random() * 2.5, 2)  # max = 12.5 for level 10
        min_damage = int(1 + (level / 2) * random.randint(5, 15))  # max 75 for level 10
        max_damage = int(1 + (level / 2) * random.randint(10, 30))  # max 150 for level 10
        self.loot_experiences = int((level / 2) * random.randint(5, 20))  # max 100 for level 10
        loots_inventory = []
        Fighter.__init__(self, gold, level, life_points, max_life_points, protection_points, dodge_rate, parry_rate,
                         critical_hit_rate, min_damage, max_damage, loots_inventory)
        # Generation of loots
        rnd = random.randint(1, 3)
        for i in range(rnd):
            self.loots_inventory.append(RandomItem(self.level).item)

    def has_been_killed(self, hero):
        """Check if the monster is dead or not. If so, loot the stuff"""
        if self.is_dead():
            print("Monster killed !")
            hero.loots_inventory = self.loots_inventory
            hero.add_gold(self.gold)
            hero.receive_loots(self.loots_inventory)
            return True
        else:
            return False
