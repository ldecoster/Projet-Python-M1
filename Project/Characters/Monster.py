from Project.Characters.Fighter import Fighter


class Monster(Fighter):
    def __init__(self, gold, level, life_points, max_life_points, protection_points, dodge_rate, parry_rate,
                 critical_hit_rate, min_damage, max_damage, loots_inventory):
        Fighter.__init__(self, gold, level, life_points, max_life_points, protection_points, dodge_rate, parry_rate,
                         critical_hit_rate, min_damage, max_damage, loots_inventory)

    def has_been_killed(self, hero):
        """Check if the monster is dead or not. If so, loot the stuff"""
        if self.life_points <= 0:
            hero.loots_inventory = self.loots_inventory
            hero.add_gold(self.gold)
            hero.receive_loots(self.loots_inventory)
            return True
        else:
            return False
