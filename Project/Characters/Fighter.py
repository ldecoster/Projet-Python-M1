from Project.Characters.Character import Character


class Fighter(Character):
    def __init__(self, gold, level, life_points, equipment_points, dodge_rate,
                 critical_hit_rate, min_damage, max_damage):
        super().__init__(gold)
        self.level = level
        self.life_points = life_points
        self.equipment_points = equipment_points
        self.dodge_rate = dodge_rate
        self.critical_hit_rate = critical_hit_rate
        self.min_damage = min_damage
        self.max_damage = max_damage
