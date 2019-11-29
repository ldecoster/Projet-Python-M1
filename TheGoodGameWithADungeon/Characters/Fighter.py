from TheGoodGameWithADungeon.Characters.Character import Character
from TheGoodGameWithADungeon.Items.LootsInventory import LootsInventory
import random


parry_reduced_damage = 0.7
equipment_balancing_points = 10


class Fighter(Character, LootsInventory):
    def __init__(self, gold, level, life_points, max_life_points, protection_points, dodge_rate, parry_rate,
                 critical_hit_rate, min_damage, max_damage, loots_inventory):
        Character.__init__(self, gold)
        LootsInventory.__init__(self, loots_inventory)
        self.level = level
        self.life_points = life_points
        self.max_life_points = max_life_points
        self.protection_points = protection_points
        self.dodge_rate = dodge_rate
        self.parry_rate = parry_rate
        self.critical_hit_rate = critical_hit_rate
        self.min_damage = min_damage
        self.max_damage = max_damage

    def is_dead(self):
        """Check if the fighter is dead or not"""
        if self.life_points <= 0:
            return True
        else:
            return False

    def heal_life_point(self, life_points):
        """Give back life_points to the fighter"""
        # Limit of life_points already reached
        if self.life_points == self.max_life_points:
            print("Nothing happened. You already have all your life points")
            return False
        # Heal the fighter
        else:
            self.life_points += life_points
            # Check is life_points do not overflow
            if self.life_points > self.max_life_points:
                self.life_points = self.max_life_points
            return True

    def loose_life_points(self, life_points):
        """Decrease the life_points of the fighter"""
        self.life_points -= life_points

    def attack(self, other):
        """Performs an attack on an other fighter"""
        rnd_damage = random.randint(self.min_damage, self.max_damage + 1)
        rnd_critical_hit = random.random()*100

        if rnd_critical_hit <= self.critical_hit_rate:
            other.take_damage(2*rnd_damage)
        else:
            other.take_damage(rnd_damage)

    def take_damage(self, damage):
        """Computes the damage received by an attack with all the fighter parameters"""
        rnd_dodge = random.random()*100
        rnd_parry = random.random()*100
        if rnd_dodge <= self.dodge_rate:
            actual_damage = 0
        elif rnd_parry <= self.parry_rate:
            actual_damage = (parry_reduced_damage*damage) - (self.protection_points / equipment_balancing_points)
        else:
            actual_damage = damage - (self.protection_points / equipment_balancing_points)
        self.loose_life_points(int(actual_damage))
