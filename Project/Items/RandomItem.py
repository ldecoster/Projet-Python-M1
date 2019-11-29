from Project.Items.ArmorItem import ArmorItem
from Project.Items.WeaponItem import WeaponItem
from Project.Items.JewelItem import JewelItem
import random


class RandomItem:
    def __init__(self, hero_level):
        self.hero_level = hero_level
        armor_rate = 50
        weapon_rate = 30
        jewel_rate = 20
        rnd_item_type = random.randint(1, 100)

        if rnd_item_type <= armor_rate:
            self.item = self.random_armor()
        elif rnd_item_type <= armor_rate+weapon_rate:
            self.item = self.random_weapon()
        elif rnd_item_type <= armor_rate+weapon_rate+jewel_rate:
            self.item = self.random_jewel()
        else:
            self.item = self.random_jewel()

    def random_armor(self):
        rnd_type = random.randint(0, 3)
        if rnd_type == 0:
            armor_type = "helmet"
        elif rnd_type == 1:
            armor_type = "chestplate"
        elif rnd_type == 2:
            armor_type = "pants"
        else:
            armor_type = "boots"
        protection_points = int((self.hero_level / 2) * random.randint(5, 15)) # max = 75 for level 10
        dodge_rate = round((self.hero_level / 2) * random.random() * 3, 2) # max = 15 for level 10
        life_points = int((self.hero_level / 2) * random.randint(2, 7)) # max = 35 for level 10
        mana_points = int((self.hero_level / 2) * random.randint(1, 4)) # max = 20 for level 10

        return ArmorItem(self.hero_level, armor_type, protection_points, dodge_rate, life_points, mana_points)

    def random_weapon(self):
        parry_rate = round((self.hero_level / 2) * random.random() * 3.6, 2)  # max = 18 for level 10
        critical_hit_rate = round((self.hero_level / 2) * random.random() * 2.8, 2)  # max = 14 for level 10
        min_damage = int((self.hero_level / 2) * random.randint(1, 4))  # max = 20 for level 10
        max_damage = int((self.hero_level / 2) * random.randint(4, 8))  # max = 40 for level 10
        return WeaponItem(self.hero_level, parry_rate, critical_hit_rate, min_damage, max_damage)

    def random_jewel(self):
        return JewelItem(self.hero_level)