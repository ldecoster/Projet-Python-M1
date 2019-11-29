from Project.Items.Item import Item


class ArmorItem(Item):
    def __init__(self, level, armor_type, protection_points, dodge_rate, life_points, mana_points):
        super().__init__(level)
        self.armor_type = armor_type
        self.protection_points = protection_points
        self.dodge_rate = dodge_rate
        self.life_point = life_points
        self.mana_point = mana_points

    def display_stats(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print("The armor is :", self.armor_type)
        print("The armor has", self.protection_points, "protections points")
        print("The armor has", self.dodge_rate, "% chance to dodge an attack")
        print("The armor give", self.life_point, "Life points")
        print("The armor give", self.mana_point, "Mana points")
        print("+++++++++++++++++++++++++++++++++++++++++++++")
