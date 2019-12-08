from TheGoodGameWithADungeon.Items.WeaponItem import WeaponItem
from TheGoodGameWithADungeon.Items.ArmorItem import ArmorItem
from TheGoodGameWithADungeon.Items.JewelItem import JewelItem


class HeroEquipment:
    def __init__(self, helmet=None, chestplate=None, pants=None, boots=None, weapon_1=None, weapon_2=None,
                 jewel_1=None, jewel_2=None, equipment_protection_points=0, equipment_dodge_rate=0.0,
                 equipment_parry_rate=0.0, equipment_critical_hit_rate=0.0,
                 equipment_min_damage=0, equipment_max_damage=0, equipment_life_points=0, equipment_mana_points=0):
        self.helmet = helmet
        self.chestplate = chestplate
        self.pants = pants
        self.boots = boots
        self.weapon_1 = weapon_1
        self.weapon_2 = weapon_2
        self.jewel_1 = jewel_1
        self.jewel_2 = jewel_2
        self.equipment_protection_points = equipment_protection_points
        self.equipment_dodge_rate = equipment_dodge_rate
        self.equipment_parry_rate = equipment_parry_rate
        self.equipment_critical_hit_rate = equipment_critical_hit_rate
        self.equipment_min_damage = equipment_min_damage
        self.equipment_max_damage = equipment_max_damage
        self.equipment_life_points = equipment_life_points
        self.equipment_mana_points = equipment_mana_points

    def equip_armor(self, armor):
        """Equip an armor to the hero"""
        if isinstance(armor, ArmorItem):
            if armor.armor_type == "helmet":
                self.helmet = armor
            elif armor.armor_type == "chestplate":
                self.chestplate = armor
            elif armor.armor_type == "pants":
                self.pants = armor
            elif armor.armor_type == "boots":
                self.boots = armor
            else:
                raise Exception("Unknown armor location")
        else:
            raise Exception("Unknown armor")
        return self.update_defensive_stats()

    def equip_weapon(self, weapon, weapon_location):
        """Equip a weapon to the hero"""
        if isinstance(weapon, WeaponItem):
            if weapon_location == "weapon_1":
                self.weapon_1 = weapon
            elif weapon_location == "weapon_2":
                self.weapon_2 = weapon
            else:
                raise Exception("Unknown weapon location")
        else:
            raise Exception("Unknown weapon")
        return self.update_offensive_stats()

    def equip_jewel(self, jewel, jewel_location):
        """Equip a jewel to the hero"""
        if isinstance(jewel, JewelItem):
            if jewel_location == "jewel_1":
                self.jewel_1 = jewel
            elif jewel_location == "jewel_2":
                self.jewel_2 = jewel
            else:
                raise Exception("Unknown jewel location")
        else:
            raise Exception("Unknown jewel")
        self.update_defensive_stats()
        self.update_offensive_stats()

    def update_defensive_stats(self):
        """Update both total defensive stats with the stats given by the equipment"""
        total_protection_points = 0
        total_dodge_rate = 0.0
        total_life_point = 0
        total_mana_point = 0

        armors = [self.helmet, self.chestplate, self.pants, self.boots]
        for armor in armors:
            if isinstance(armor, ArmorItem):
                total_protection_points += armor.protection_points
                total_dodge_rate += armor.dodge_rate
                total_life_point += armor.life_point
                total_mana_point += armor.mana_point

        self.equipment_protection_points = total_protection_points
        self.equipment_dodge_rate = round(total_dodge_rate, 2)
        self.equipment_life_points = total_life_point
        self.equipment_mana_points = total_mana_point

    def update_offensive_stats(self):
        """Update all total offensives stats with the stats given by the equipment"""
        total_parry_rate = 0.0
        total_critical_hit_rate = 0.0
        total_min_damage = 0
        total_max_damage = 0

        weapons = [self.weapon_1, self.weapon_2]
        for weapon in weapons:
            if isinstance(weapon, WeaponItem):
                total_parry_rate += weapon.parry_rate
                total_critical_hit_rate += weapon.critical_hit_rate
                total_min_damage += weapon.min_damage
                total_max_damage += weapon.max_damage

        self.equipment_parry_rate = round(total_parry_rate, 2)
        self.equipment_critical_hit_rate = round(total_critical_hit_rate, 2)
        self.equipment_min_damage = total_min_damage
        self.equipment_max_damage = total_max_damage
