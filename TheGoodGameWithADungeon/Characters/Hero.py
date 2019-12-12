import random
from TheGoodGameWithADungeon.Characters.Fighter import Fighter
from TheGoodGameWithADungeon.Characters.Monster import Monster
from TheGoodGameWithADungeon.GameRuntime.Stats import Stats
from TheGoodGameWithADungeon.GameRuntime.Texts import *
from TheGoodGameWithADungeon.GameRuntime.UserChoice import *
from TheGoodGameWithADungeon.Items.ArmorItem import ArmorItem
from TheGoodGameWithADungeon.Items.Inventory import Inventory
from TheGoodGameWithADungeon.Items.JewelItem import JewelItem
from TheGoodGameWithADungeon.Items.HeroEquipment import HeroEquipment
from TheGoodGameWithADungeon.Items.Potion import Potion
from TheGoodGameWithADungeon.Items.WeaponItem import WeaponItem


max_level = 10
experience_level = {1: 0, 2: 50, 3: 120, 4: 210, 5: 330, 6: 480, 7: 660, 8: 1000, 9: 1490, 10: 1840}


class Hero(Fighter, HeroEquipment, Inventory, Stats):
    def __init__(self, gold=100, level=1, life_points=100, max_life_points=100, protection_points=0, dodge_rate=0.0,
                 parry_rate=0.0, critical_hit_rate=0.0, min_damage=0, max_damage=0, loots_inventory=[],
                 name="default", exp_points=0, mana_points=20, max_mana_points=20,
                 hero_min_damage=1, hero_max_damage=10):
        Fighter.__init__(self, gold, level, life_points, max_life_points, protection_points, dodge_rate,
                         parry_rate, critical_hit_rate, min_damage, max_damage, loots_inventory)
        HeroEquipment.__init__(self)
        Inventory.__init__(self)
        Stats.__init__(self)

        self.name = name
        self.exp_points = exp_points
        self.mana_points = mana_points
        self.max_mana_points = max_mana_points
        self.hero_min_damage = hero_min_damage
        self.hero_max_damage = hero_max_damage
        self.default_life_points = self.max_life_points
        self.default_mana_points = self.max_mana_points

        self.update()

    def show_stats(self):
        hero_show_stats_text(self.life_points, self.max_life_points, self.mana_points, self.max_mana_points,
                             self.protection_points, self.dodge_rate, self.parry_rate, self.critical_hit_rate,
                             self.min_damage, self.max_damage)

    def update(self):
        """Update stats"""
        # Compute the difference of stats
        old_equipment_life_points = self.equipment_life_points
        old_equipment_mana_points = self.equipment_mana_points
        self.update_offensive_stats()
        self.update_defensive_stats()
        new_equipment_life_points = self.equipment_life_points
        new_equipment_mana_points = self.equipment_mana_points
        actual_equipment_life_points = old_equipment_life_points - \
                                       (old_equipment_life_points - new_equipment_life_points)
        actual_equipment_mana_points = old_equipment_mana_points - \
                                       (old_equipment_mana_points - new_equipment_mana_points)
        self.max_life_points = self.default_life_points + actual_equipment_life_points
        self.max_mana_points = self.default_mana_points + actual_equipment_mana_points

        self.protection_points = self.equipment_protection_points
        self.dodge_rate = self.equipment_dodge_rate
        self.parry_rate = self.equipment_parry_rate
        self.critical_hit_rate = self.equipment_critical_hit_rate
        self.min_damage = self.hero_min_damage + self.equipment_min_damage
        self.max_damage = self.hero_max_damage + self.equipment_max_damage

    def manage_experience_points(self):
        """Increase the hero's level if he has enough experience points"""
        # If the max level is already reached, do nothing
        if self.level == max_level:
            hero_max_level_text()
        # Else level-up
        else:
            while self.exp_points > experience_level[self.level + 1]:
                self.level += 1
                hero_new_level_text(self.level)
                self.lvl_up()
                # Check the case where max level is reached and then break
                if self.level == max_level:
                    hero_max_level_text()
                    break

    def gain_experience(self, experience_points):
        """Give some experiences to the hero"""
        self.exp_points += experience_points
        self.manage_experience_points()

    def gain_mana(self, mana_points):
        """Give back mana_points to the fighter"""
        # Limit of mana_points already reached
        if self.mana_points == self.max_mana_points:
            hero_all_mana_points_text()
            return False
        # Restore mana
        else:
            self.mana_points += mana_points
            self.mana_gained += mana_points
            # Check is mana_points do not overflow
            if self.mana_points > self.max_mana_points:
                self.mana_points = self.max_mana_points
            return True

    def show_inventory(self):
        """Show content of hero's inventory"""
        heal_potion_number = 0
        mana_potion_number = 0
        # Count number potions
        for item in self.inventory:
            if isinstance(item, Potion):
                if item.potion_type == "heal":
                    heal_potion_number += 1
                elif item.potion_type == "mana":
                    mana_potion_number += 1
        hero_inventory_text(heal_potion_number, mana_potion_number, self.gold)

        if user_choice_yes_no("Would you like to use an item ? Yes {y} / No {n}"):
            if user_choice_heal_mana_potion("Which item ? Heal potion {heal} / Mana potion {mana}"):
                self.use_potion("heal")
            else:
                self.use_potion("mana")

        if user_choice_yes_no("Would you like to see all your stats ? Yes {y} / No {n}"):
            self.show_stats()

    def use_potion(self, potion_type):
        """Use a potion if the hera has one and if his stats are not full"""
        # Heal potion
        heal_potion_number, mana_potion_number = self.count_potions()
        if potion_type == "heal":
            if heal_potion_number > 0:
                before = self.life_points
                can_restore_life_points = self.heal_life_point(10)
                if can_restore_life_points is True:
                    hero_life_points_change_text(before, self.life_points)
                    self.remove_potion("heal")
                    self.heal_potions_used_number += 1  # stats
                else:
                    hero_no_use_heal_potion_text()
            else:
                hero_no_heal_potion_text()
        # Mana potion
        elif potion_type == "mana":
            if mana_potion_number > 0:
                before = self.mana_points
                can_restore_mana_points = self.gain_mana(10)
                if can_restore_mana_points is True:
                    hero_mana_points_change_text(before, self.mana_points)
                    self.remove_potion("mana")
                    self.mana_potions_used_number += 1  # stats
                else:
                    hero_no_use_mana_potion_text()
            else:
                hero_no_mana_potion_text()
        else:
            raise Exception("Unknown potion type")

    def magical_spell(self, target=None):
        """Performs an attack on an other fighter or heal the player"""
        if self.mana_points >= 5:
            if target is None:
                """Heal"""
                self.heal_life_point(int(self.max_life_points * 0.2))
                hero_life_regained_text(self.life_points)
            elif isinstance(target, Monster):
                """Magic attack"""
                hero_magic_attack_text()
                rnd_damage = random.randint(self.level*3, self.level*5)
                target.loose_life_points(rnd_damage)
                self.attack(target)  # An regular attack is also performed
            else:
                hero_spell_failed_text()
            self.mana_points -= 5
            self.mana_consummed += 5  # stats
            self.spells_performed_number += 1  # stats
            hero_mana_points_after_spell_text(self.mana_points)
        else:
            hero_not_enough_mana_text()

    def lvl_up(self):
        """Level-up + upgrade of one stat + full heal"""
        hero_improve_stat_text()
        lvl_up_choice = user_choice_lvl_up("Improve : {lifepoints} / {mana} / {damage}")
        if lvl_up_choice == "lifepoints":
            self.max_life_points += 10
            hero_lvl_up_life_points_text(self.max_life_points)
        elif lvl_up_choice == "mana":
            self.max_mana_points += 5
            hero_lvl_up_mana_points_text(self.max_mana_points)
        elif lvl_up_choice == "damage":
            self.hero_min_damage += 3
            self.hero_max_damage += 3
            hero_lvl_up_damage_text(self.hero_min_damage, self.hero_max_damage)
        else:
            raise Exception("Error : Unhandled case")
        self.life_points = self.max_life_points
        self.mana_points = self.max_mana_points

    def receive_loots(self, loots):
        """Get the loots obtained from a monster"""
        self.loots_inventory = loots
        hero_new_loots_text()
        self.loop_through_loots()

    def loop_through_loots(self):
        """Pop loot from loots_inventory until it's empty"""
        while self.loots_inventory:
            loot = self.loots_inventory.pop()
            if isinstance(loot, ArmorItem) or isinstance(loot, WeaponItem) or isinstance(loot, JewelItem):
                self.deal_with_new_loot(loot)
            else:
                hero_unknown_item_text()
        # Reset loots_inventory in the easiest way
        self.loots_inventory = []

    def deal_with_new_loot(self, item):
        """Handle case depending on the nature of the item"""
        if isinstance(item, ArmorItem):
            hero_new_armor_found(item.armor_type)
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
                hero_new_no_armor_text(item.armor_type)
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_armor(item)
                    hero_item_equipped_text(item.armor_type)
                else:
                    hero_item_not_equipped_text(item.armor_type)
            # Else we have to ask the user if he wants to replace it
            else:
                hero_new_exists_armor_text(item.armor_type)
                self_item.display_stats()
                hero_new_armor_text(item.armor_type)
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_armor(item)
                    hero_item_equipped_text(item.armor_type)
                else:
                    hero_item_not_equipped_text(item.armor_type)

        elif isinstance(item, WeaponItem):
            hero_new_weapon_found_text()
            if self.weapon_1 is None:
                hero_weapon_1_empty_text()
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_weapon(item, "weapon_1")
                    hero_weapon_equipped_text()
                else:
                    hero_weapon_not_equipped_text()
            elif self.weapon_2 is None:
                hero_weapon_2_empty_text()
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_weapon(item, "weapon_2")
                    hero_weapon_equipped_text()
                else:
                    hero_weapon_not_equipped_text()
            else:
                hero_weapons_not_empty_text()
                hero_weapon_1_stats_text()
                self.weapon_1.display_stats()
                hero_weapon_2_stats_text()
                self.weapon_2.display_stats()
                hero_new_weapon_stats_text()
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    if user_choice_1_2("Now, where would like to equip it ? Weapon 1 {1} / Weapon 2 {2}"):
                        self.equip_weapon(item, "weapon_1")
                    else:
                        self.equip_weapon(item, "weapon_2")
                    hero_weapon_equipped_text()
                else:
                    hero_weapon_not_equipped_text()

        elif isinstance(item, JewelItem):
            hero_new_jewel_found_text()
            if self.jewel_1 is None:
                hero_jewel_1_empty_text()
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_jewel(item, "jewel_1")
                    hero_jewel_equipped_text()
                else:
                    hero_jewel_not_equipped_text()
            elif self.jewel_2 is None:
                hero_jewel_2_empty_text()
                item.display_stats()
                if user_choice_yes_no("Would to equip it ? Yes {y} / No {n}"):
                    self.equip_jewel(item, "jewel_2")
                    hero_jewel_equipped_text()
                else:
                    hero_jewel_not_equipped_text()
            else:
                hero_jewels_not_empty_text()
                hero_jewel_1_stats_text()
                self.jewel_1.display_stats()
                hero_jewel_2_stats_text()
                self.jewel_2.display_stats()
                hero_new_jewel_stats_text()
                item.display_stats()
                if user_choice_yes_no("Would to equip the new one ? Yes {y} / No {n}"):
                    if user_choice_1_2("Where would you like to equipt it ? Weapon 1 {1} / Weapon 2 {2}"):
                        self.equip_jewel(item, "weapon_1")
                    else:
                        self.equip_jewel(item, "weapon_2")
                    hero_jewel_equipped_text()
                else:
                    hero_jewel_not_equipped_text()

        self.update()
