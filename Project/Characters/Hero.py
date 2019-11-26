from Project.Characters.Fighter import Fighter
from Project.Items.HeroEquipment import HeroEquipment


class Hero(Fighter, HeroEquipment):
    def __init__(self, gold, level, life_points, max_life_points, equipment_points, dodge_rate, parry_rate,
                 critical_hit_rate, min_damage, max_damage,
                 name, exp_points, mana_points, max_mana_points, total_min_damage, total_max_damage):
        Fighter.__init__(self, gold, level, life_points, max_life_points, equipment_points, dodge_rate, parry_rate,
                         critical_hit_rate, min_damage, max_damage)
        HeroEquipment.__init__(self)
        self.name = name
        self.exp_points = exp_points
        self.mana_points = mana_points
        self.max_mana_points = max_mana_points
        self.total_min_damage = total_min_damage
        self.total_max_damage = total_max_damage

    def update(self):
        # just in case
        self.update_offensive_stats()
        self.update_defensive_stats()
        self.total_min_damage = self.min_damage + self.equipment_min_damage
        self.total_max_damage = self.max_damage + self.equipment_max_damage
