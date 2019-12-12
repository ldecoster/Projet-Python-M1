from TheGoodGameWithADungeon.Items.Item import Item


class ArmorItem(Item):
    def __init__(self, level, armor_type, protection_points, dodge_rate, life_points, mana_points):
        super().__init__(level)
        self.armor_type = armor_type
        self.protection_points = protection_points
        self.dodge_rate = dodge_rate
        self.life_point = life_points
        self.mana_point = mana_points

    def display_stats(self):
        print("""
        ++++++++++++++++++++++++++++++++++++++++++++++++
        The armor is {}
        The armor has {} protections points
        The armor has {} "% chance to dodge an attack
        The armor gives {} life points
        The armor gives {} mana points
        ++++++++++++++++++++++++++++++++++++++++++++++++
        """.format(self.armor_type, self.protection_points, self.dodge_rate, self.life_point, self.mana_point))
