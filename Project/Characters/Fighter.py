from Project.Characters.Character import Character
from Project.Items.LootsInventory import LootsInventory
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
        print("lost", life_points, " life points")
        self.life_points -= life_points

    def attack(self, other):
        """Performs an attack on an other fighter"""
        print("before hit", other.life_points)
        rnd_damage = random.randint(self.min_damage, self.max_damage)
        rnd_critical_hit = random.random()*100

        if rnd_critical_hit <= self.critical_hit_rate:
            print("Critical hit", 2*rnd_damage)
            other.take_damage(2*rnd_damage)
        else:
            print("Regular hit", rnd_damage)
            other.take_damage(rnd_damage)
        print("After hit", other.life_points)

    def magical_spell(self, player=None, other=None):
        """Performs an attack on an other fighter or heal the player"""
        print("Mana point before the spell", player.mana_points)
        if player is None:
            """Magic attack"""
            rnd_damage = random.randint(player.level*3, player.level*5)
            player.attack(other)
            player.mana_points -= 5
        elif other is None:
            """Heal"""
            player.heal_life_point(player.max_life_points*0.2)
        player.mana_points -= 5
        print("Mana point after the spell", player.mana_points)


    def take_damage(self, damage):
        """Computes the damage received by an attack with all the fighter parameters"""
        rnd_dodge = random.random()*100
        rnd_parry = random.random()*100
        if rnd_dodge <= self.dodge_rate:
            print("Attack dodged")
            actual_damage = 0
        elif rnd_parry <= self.parry_rate:
            print("Attack parry")
            actual_damage = (parry_reduced_damage*damage) - (self.protection_points / equipment_balancing_points)
        else:
            print("Full attack received")
            actual_damage = damage - (self.protection_points / equipment_balancing_points)
        self.loose_life_points(int(actual_damage))
