from Project.Items.Item import Item


class WeaponItem(Item):
    def __init__(self, level, parry_rate, critical_hit_rate, min_damage, max_damage):
        super().__init__(level)
        self.parry_rate = parry_rate
        self.critical_hit_rate = critical_hit_rate
        self.min_damage = min_damage
        self.max_damage = max_damage

    def display_stats(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print("The weapon minimum damages are :", self.min_damage)
        print("The weapon maximum damages are :", self.max_damage)
        print("The weapon has", self.parry_rate, "% chance to parry an attack")
        print("The weapon has", self.critical_hit_rate, "% chance to inflict a critical hit")
        print("+++++++++++++++++++++++++++++++++++++++++++++")