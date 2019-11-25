from Project.Characters.Fighter import Fighter


class Hero(Fighter):
    def __init__(self, gold, level, life_points, equipment_points, dodge_rate,
                 critical_hit_rate, min_damage, max_damage,
                 name, exp_points, parry_rate, mana_points):
        super().__init__(gold, level, life_points, equipment_points, dodge_rate,
                         critical_hit_rate, min_damage, max_damage)
        self.name = name
        self.exp_points = exp_points
        self.parry_rate = parry_rate
        self.mana_points = mana_points

