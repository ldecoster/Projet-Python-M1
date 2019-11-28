from Project.Characters.Fighter import Fighter
from Project.Items.HeroEquipment import HeroEquipment
from Project.Items.WeaponItem import WeaponItem
from Project.Items.ArmorItem import ArmorItem
from Project.Items.JewelItem import JewelItem
from Project.Items.Consumable import Consumable
from Project.GameRuntime.UserChoice import *


class Hero(Fighter, HeroEquipment):
    def __init__(self, gold, level, life_points, max_life_points, protection_points, dodge_rate, parry_rate,
                 critical_hit_rate, min_damage, max_damage,
                 name, exp_points, mana_points, max_mana_points, total_min_damage, total_max_damage, loots_inventory):
        Fighter.__init__(self, gold, level, life_points, max_life_points, protection_points, dodge_rate, parry_rate,
                         critical_hit_rate, min_damage, max_damage, loots_inventory)
        HeroEquipment.__init__(self)
        self.name = name
        self.exp_points = exp_points
        self.mana_points = mana_points
        self.max_mana_points = max_mana_points
        self.protection_points = self.equipment_protection_points # "Override"
        self.total_min_damage = total_min_damage
        self.total_max_damage = total_max_damage
        self.inventory = ["potion", "potion", "mana potion"]

    def show_stats(self):
        print(vars(self))

    def update(self):
        """Update stats"""
        # just in case
        self.update_offensive_stats()
        self.update_defensive_stats()
        self.total_min_damage = self.min_damage + self.equipment_min_damage
        self.total_max_damage = self.max_damage + self.equipment_max_damage

    def gain_mana(self, mana_points):
        """Give back mana_points to the fighter"""
        # Limit of mana_points already reached
        if self.mana_points == self.max_mana_points:
            print("Nothing happened. You already have all your mana")
            return False
        # Restore mana
        else:
            self.mana_points += mana_points
            # Check is mana_points do not overflow
            if self.mana_points > self.max_mana_points:
                self.mana_points = self.max_mana_points
            return True

    def show_inventory(self):
        """Show content of hero's inventory"""
        heal_potion = 0
        mana_potion = 0
        # Count number potions
        for item in self.inventory:
            if item == "potion":
                heal_potion += 1
            elif item == "mana potion":
                mana_potion += 1
        print("heal potion : ", heal_potion, "mana potion", mana_potion, "gold : ", self.gold)
        if user_choice_yes_no("Would you like to use an item ? Yes {y} / No {n}"):
            # Rajouter test sur la fait qu'il y a bien une potion de disponible
            if user_choice_heal_mana_potion("Which item ? Heal potion {heal} / Mana potion {mana}"):
                self.use_item("heal potion")
            else:
                self.use_item("mana potion")

    def add_inventory(self, item):
        # verifier si l'inventaire n'est pas plein (si on met une limite)
        self.inventory.append(item)

    def remove_inventory(self, item):
        # verifier que l'item existe dans l'inventaire pas trop utile en soit cette fonction je pense
        self.inventory.remove(item)

    # Test à rajouter / Fct pas clair
    def use_item(self, item):
        # Heal potion
        if item == "potion" or item == "item1":
            # heal function
            before = self.life_points
            use = self.heal_life_point(10)
            print("Life points : ", before, "->", self.life_points)
            if use is True:
                self.remove_inventory(item)
            else:
                print("You keep your potion")
        # Mana potion
        elif item == "mana potion":
            # mana function
            before = self.mana_points
            use = self.gain_mana(5)
            print("Mana points : ", before, "->", self.mana_points)
            if use is True:
                self.remove_inventory(item)
            else:
                print("You keep your potion")
        else:
            print("Can't use this item")

    def lvl_up(self):
        """Level-up + upgrade of one stat + full heal"""
        self.level += 1
        print("Level up ! You are now level : ", self.level, "\n Choose the stat you want to improve")
        lvl_up_choice = user_choice_lvl_up("Improve : {lifepoints} / {mana} / {damage}")
        if lvl_up_choice == "lifepoints":
            self.max_life_points += 10
            print("Maximum life points : ", self.max_life_points - 10, "->", self.max_life_points)
        elif lvl_up_choice == "mana":
            self.max_mana_points += 5
            print("Maximum mana points : ", self.max_mana_points - 5, "->", self.max_mana_points)
        elif lvl_up_choice == "damage":
            self.total_min_damage += 3
            self.total_max_damage += 3
            print("Damage : ", self.total_min_damage - 3, "-", self.total_max_damage - 3, "->", self.total_min_damage,
                  "-", self.total_max_damage)
        else:
            raise Exception("Error : Unhandled case")
        self.life_points = self.max_life_points
        self.mana_points = self.max_mana_points

    def receive_loots(self, loots):
        self.loots_inventory = loots
        print("Loots received")
        self.loop_through_loots()

    def loop_through_loots(self):
        # Pop loot from inventory until it's empty
        while self.loots_inventory:
            loot = self.loots_inventory.pop()
            if isinstance(loot, ArmorItem) or isinstance(loot, WeaponItem) or isinstance(loot, JewelItem):
                self.deal_with_new_loot(loot)
            elif isinstance(loot, Consumable):
                print("Known consumable :", loot.__class__.__name__)
            else:
                print("Unknown item")
        self.loots_inventory = []

    # Fonction à raccourcir / à séparer
    def deal_with_new_loot(self, item):
        if isinstance(item, ArmorItem):
            print("You found a new", item.armor_type)
            if item.armor_type == "helmet":
                self_item = self.helmet
            elif item.armor_type == "chestplate":
                self_item = self.chestplate
            elif item.armor_type == "pants":
                self_item = self.pants
            elif item.armor_type == "boots":
                self_item = self.boots
            else:
                raise Exception("Bad armor type")

            # If no item is already equipped in its location
            if self_item is None:
                print("You currently have no", item.armor_type)
                print("The new one has the following stats :")
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_armor(item)
                    print(item.armor_type, "equipped")
                else:
                    print(item.armor_type, "not equipped")
            # Else we have to ask the user if he wants to replace it
            else:
                print("You already have an equipped", item.armor_type)
                print("Its current stats are :")
                self_item.display_stats()
                print("The new", item.armor_type, "has the following stats :")
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_armor(item)
                    print(item.armor_type, "equipped")
                else:
                    print(item.armor_type, "not equipped")

        elif isinstance(item, WeaponItem):
            print("You found a new weapon")
            if self.weapon_1 is None:
                print("Your weapon 1 location is empty")
                print("The new weapon has the following stats :")
                item.display_stats()
                print("Would to equip it ? Yes {y} / No {n}")
                if user_choice_yes_no():
                    self.equip_weapon(item, "weapon_1")
                    print("Weapon equipped")
                else:
                    print("Weapon not equipped")
            elif self.weapon_2 is None:
                print("Your weapon 2 location is empty")
                print("The new weapon has the following stats :")
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_weapon(item, "weapon_2")
                    print("Weapon equipped")
                else:
                    print("Weapon not equipped")
            else:
                print("Both weapon 1 and 2 location are not empty")
                print("Weapon 1 current stats are :")
                self.weapon_1.display_stats()
                print("Weapon 2 current stats are :")
                self.weapon_2.display_stats()
                print("The new weapon has the following stats :")
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    if user_choice_1_2("Now, where would like to equip it ? Weapon 1 {1} / Weapon 2 {2}"):
                        self.equip_weapon(item, "weapon_1")
                    else:
                        self.equip_weapon(item, "weapon_2")
                    print("Weapon equipped")
                else:
                    print("Weapon not equipped")

        elif isinstance(item, JewelItem):
            print("You found a new jewel")
            if self.jewel_1 is None:
                print("Your jewel 1 location is empty")
                print("The new jewel has the following stats :")
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_jewel(item, "jewel_2")
                    print("Jewel equipped")
                else:
                    print("Jewel not equipped")
            elif self.jewel_2 is None:
                print("Your jewel 2 location is empty")
                print("The new jewel has the following stats :")
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_jewel(item, "jewel_2")
                    print("Jewel equipped")
                else:
                    print("Jewel not equipped")
            else:
                print("Both jewel 1 and 2 location are not empty")
                print("Jewel 1 current stats are :")
                self.jewel_1.display_stats()
                print("Jewel 2 current stats are :")
                self.jewel_2.display_stats()
                print("The new weapon has the following stats :")
                item.display_stats()
                if user_choice_yes_no("Would to equip the new one ? Yes {y} / No {n}"):
                    if user_choice_1_2("Where would you like to equipt it ? Weapon 1 {1} / Weapon 2 {2}"):
                        self.equip_jewel(item, "weapon_1")
                    else:
                        self.equip_jewel(item, "weapon_2")
                    print("Jewel equipped")
                else:
                    print("Jewel not equipped")
