from TheGoodGameWithADungeon.Items.Item import Item


class WeaponItem(Item):
    def __init__(self, level, parry_rate, critical_hit_rate, min_damage, max_damage):
        super().__init__(level)
        self.parry_rate = parry_rate
        self.critical_hit_rate = critical_hit_rate
        self.min_damage = min_damage
        self.max_damage = max_damage

    def display_stats(self):
        print("""
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        The weapon minimum damages are {}
        The weapon maximum damages are {}
        The weapon gives {} % chance to parry an attack
        The weapon gives {} % chance to inflict a critical hit
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """.format(self.min_damage, self.max_damage, self.parry_rate, self.critical_hit_rate))
