import random
from Project.Items.WeaponItem import WeaponItem
from Project.Items.ArmorItem import ArmorItem
from Project.Items.JewelItem import JewelItem
from Project.Characters.Fighter import Fighter


class Monster(Fighter):
    def __init__(self, gold, level, life_points, max_life_points, protection_points, dodge_rate, parry_rate,
                 critical_hit_rate, min_damage, max_damage, loots_inventory):
        Fighter.__init__(self, gold, level, life_points, max_life_points, protection_points, dodge_rate, parry_rate,
                         critical_hit_rate, min_damage, max_damage, loots_inventory)

    def has_been_killed(self, hero):
        """Check if the monster is dead or not. If so, loot the stuff"""
        if self.is_dead():
            hero.loots_inventory = self.loots_inventory
            hero.add_gold(self.gold)
            hero.receive_loots(self.loots_inventory)
            return True
        else:
            return False

    # A changer de place il me semble pour recuperer le level du hero, comme ça
    # On pourra generer les stats de l'item en fonction du lvl du perso
    # pour l'instant je mets lvl = 1
    # prendre lvl mob jsuis con
    def random_item_generator(self):
        level = 1
        rnd_item_type = random.randint(1, 6)
        item = None
        #rnd pour les stats
        rnd_life_points = random.randint(0, 15)
        rnd_mana_points = random.randint(0, 10)
        rnd_protection_points = random.randint(0, 7)
        rnd_dodge_rate = random.randint(0, 3)
        rnd_parry_rate = random.randint(0, 5)
        rnd_critical_hit = random.randint(0, 3)
        rnd_min_damage = random.randint(5, 10)
        rnd_max_damage = random.randint(rnd_min_damage + 2, 20)

        #Generation de l'item random
        if rnd_item_type == 1:
            armor_type = "helmet"
            item = ArmorItem(level, armor_type, rnd_protection_points, rnd_dodge_rate, rnd_life_points, rnd_mana_points)
        elif rnd_item_type == 2:
            armor_type = "chestplate"
            item = ArmorItem(level, armor_type, rnd_protection_points, 0, rnd_life_points, rnd_mana_points)
        elif rnd_item_type == 3:
            armor_type = "boots"
            item = ArmorItem(level, armor_type, 0, rnd_dodge_rate, rnd_life_points, 0)
        elif rnd_item_type == 4:
            armor_type = "pants"
            item = ArmorItem(level, armor_type, 0, 0, rnd_life_points, rnd_mana_points)
        elif rnd_item_type == 5:
            item_type = "weapon_1"
            item = WeaponItem(level, rnd_parry_rate, rnd_critical_hit, rnd_min_damage, rnd_max_damage)
        elif rnd_item_type == 6:
            item_type = "weapon_2"
            item = WeaponItem(level, rnd_parry_rate, rnd_critical_hit, rnd_min_damage, rnd_max_damage)
        elif rnd_item_type == 7:
            armor_type = "jewel_1"
            print("pas encore")
        elif rnd_item_type == 8:
            armor_type = "jewel_2"
            print("pas encore")
        #L'item se met dans le loot du monstre
        monster.loots_inventory = item


monster = Monster(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
monster.random_item_generator()

