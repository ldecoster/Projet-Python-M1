from Project.Characters.Fighter import Fighter


class Monster(Fighter):
    def __init__(self, gold, level, life_points, max_life_points, equipment_points, dodge_rate,
                 critical_hit_rate, min_damage, max_damage, loots):
        Fighter.__init__(self, gold, level, life_points, max_life_points, equipment_points, dodge_rate,
                         critical_hit_rate, min_damage, max_damage)
        self.loots = loots
