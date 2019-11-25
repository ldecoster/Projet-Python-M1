from Project.Items.WeaponItem import WeaponItem
from Project.Items.ArmorItem import ArmorItem


def check_item_availability(item):
    if item is None:
        return True
    else:
        return False


class HeroEquipment:
    def __init__(self, helmet=None, chestplate=None, pants=None, boots=None, weapon_1=None, weapon_2=None,
                 jewel_1=None, jewel_2=None, total_protection_points=0, total_dodge_rate=0, total_parry_rate=0,
                 total_critical_hit_rate=0, total_min_damage=0, total_max_damage=0):
        self.helmet = helmet
        self.chestplate = chestplate
        self.pants = pants
        self.boots = boots
        self.weapon_1 = weapon_1
        self.weapon_2 = weapon_2
        self.jewel_1 = jewel_1
        self.jewel_2 = jewel_2
        self.equipment_protection_points = total_protection_points
        self.equipment_dodge_rate = total_dodge_rate
        self.equipment_parry_rate = total_parry_rate
        self.equipment_critical_hit_rate = total_critical_hit_rate
        self.equipment_min_damage = total_min_damage
        self.equipment_max_damage = total_max_damage

    def equip_armor(self, armor):
        if isinstance(armor, ArmorItem):
            if armor.armor_type == "helmet":
                if check_item_availability(self.helmet):
                    self.helmet = armor
                    self.update_defensive_stats()
                else:
                    raise Exception("An armor is already equipped at this location")
            elif armor.armor_type == "chestplate":
                if check_item_availability(self.chestplate):
                    self.chestplate = armor
                    self.update_defensive_stats()
                else:
                    raise Exception("An armor is already equipped at this location")
            elif armor.armor_type == "pants":
                if check_item_availability(self.pants):
                    self.pants = armor
                    self.update_defensive_stats()
                else:
                    raise Exception("An armor is already equipped at this location")
            elif armor.armor_type == "boots":
                if check_item_availability(self.boots):
                    self.boots = armor
                    self.update_defensive_stats()
                else:
                    raise Exception("An armor is already equipped at this location")
            else:
                raise Exception("Unknown armor location")
        else:
            raise Exception("Unknown armor")

    def equip_weapon(self, weapon, weapon_location):
        if weapon_location == "weapon_1":
            if check_item_availability(self.weapon_1):
                self.weapon_1 = weapon
                self.update_offensive_stats()
            else:
                raise Exception("A weapon is already equipped at this location")
        elif weapon_location == "weapon_2":
            if check_item_availability(self.weapon_2):
                self.weapon_2 = weapon
                self.update_offensive_stats()
            else:
                raise Exception("A weapon is already equipped at this location")
        else:
            raise Exception("Unknown weapon location")

    def update_defensive_stats(self):
        total_protection_points = 0
        total_dodge_rate = 0.0

        if isinstance(self.helmet, ArmorItem):
            total_protection_points += self.helmet.protection_points
            total_dodge_rate += self.helmet.dodge_rate
        if isinstance(self.chestplate, ArmorItem):
            total_protection_points += self.chestplate.protection_points
            total_dodge_rate += self.chestplate.dodge_rate
        if isinstance(self.pants, ArmorItem):
            total_protection_points += self.pants.protection_points
            total_dodge_rate += self.pants.dodge_rate
        if isinstance(self.boots, ArmorItem):
            total_protection_points += self.boots.protection_points
            total_dodge_rate += self.boots.dodge_rate

        self.equipment_protection_points = total_protection_points
        self.equipment_dodge_rate = total_dodge_rate

    def update_offensive_stats(self):
        total_parry_rate = 0.0
        total_critical_hit_rate = 0.0
        total_min_damage = 0
        total_max_damage = 0

        if isinstance(self.weapon_1, WeaponItem):
            total_parry_rate += self.weapon_1.parry_rate
            total_critical_hit_rate += self.weapon_1.critical_hit_rate
            total_min_damage += self.weapon_1.min_damage
            total_max_damage += self.weapon_1.max_damage
        if isinstance(self.weapon_2, WeaponItem):
            total_parry_rate += self.weapon_2.parry_rate
            total_critical_hit_rate += self.weapon_2.critical_hit_rate
            total_min_damage += self.weapon_2.min_damage
            total_max_damage += self.weapon_2.max_damage

        self.equipment_parry_rate = total_parry_rate
        self.equipment_critical_hit_rate = total_critical_hit_rate
        self.equipment_min_damage = total_min_damage
        self.equipment_max_damage = total_max_damage
