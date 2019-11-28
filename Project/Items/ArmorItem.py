from Project.Items.Item import Item
import random


class ArmorItem(Item):
    def __init__(self, level, armor_type, protection_points, dodge_rate, life_points, mana_points):
        super().__init__(level)
        self.armor_type = armor_type
        self.protection_points = protection_points
        self.dodge_rate = dodge_rate
        self.life_point = life_points
        self.mana_point = mana_points
        # display pour verifier dans monstre
        self.display_stats()

    def display_stats(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print("The armor is :", self.armor_type)
        print("The armor has", self.protection_points, "protections points")
        print("The armor has", self.dodge_rate, "% chance to dodge an attack")
        print("The armor give", self.life_point, "Life points")
        print("The armor give", self.mana_point, "Mana points")
        print("+++++++++++++++++++++++++++++++++++++++++++++")


"""
rnd_protection = random.randint(0,10)
rnd_dodge = random.randint(0,3)
rnd_life = random.randint(5,15)
rnd_mana = random.randint(0,10)
armortype = "pants"
level = 3

# item gives different stats in function of his type
if armortype == "helmet":
    ArmorItem = ArmorItem(level, armortype, rnd_protection, rnd_dodge, rnd_life, rnd_mana)
elif armortype == "chestplate":
    ArmorItem = ArmorItem(level, armortype, rnd_protection, 0, rnd_life, rnd_mana)
elif armortype == "boots":
    ArmorItem = ArmorItem(level, armortype, 0, rnd_dodge, rnd_life, 0)
elif armortype == "pants":
    ArmorItem = ArmorItem(level, armortype, 0, 0, rnd_life, rnd_mana)
ArmorItem.display_stats()
"""
