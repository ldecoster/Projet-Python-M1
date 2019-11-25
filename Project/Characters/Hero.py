from Project.Characters.Fighter import Fighter


class Hero(Fighter):
    def __init__(self, gold, level, life_points, equipment_points, dodge_rate,
                 critical_hit_rate, min_damage, max_damage, loots):
        super().__init__(gold, level, life_points, equipment_points, dodge_rate,
                         critical_hit_rate, min_damage, max_damage)
        self.loots = loots
