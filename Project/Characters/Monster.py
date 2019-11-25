from Project.Characters.Fighter import Fighter


class Monster(Fighter):
    def __init__(self, gold, level, life_points, equipment_points, dodge_rate,
                 critical_hit_rate, min_damage, max_damage, exp_points, parry_rate, mana_points):
        super().__init__(gold, level, life_points, equipment_points, dodge_rate,
                         critical_hit_rate, min_damage, max_damage)
        self.exp_points = exp_points
        self.parry_rate = parry_rate
        self.mana_points = mana_points
