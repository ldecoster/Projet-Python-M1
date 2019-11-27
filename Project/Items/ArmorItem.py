from Project.Items.Item import Item


class ArmorItem(Item):
    def __init__(self, level, armor_type, protection_points, dodge_rate):
        super().__init__(level)
        self.armor_type = armor_type
        self.protection_points = protection_points
        self.dodge_rate = dodge_rate

    def display_stats(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print("The armor is :", self.armor_type)
        print("The armor has", self.protection_points, "protections points")
        print("The armor has", self.dodge_rate, "% chance to dodge an attack")
        print("+++++++++++++++++++++++++++++++++++++++++++++")
