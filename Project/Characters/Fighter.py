from Project.Characters.Character import Character
import random


parry_reduced_damage = 0.7
equipment_balancing_points = 10


class Fighter(Character):
    def __init__(self, gold, level, life_points, max_life_points, equipment_points, dodge_rate, parry_rate,
                 critical_hit_rate, min_damage, max_damage):
        Character.__init__(self, gold)
        self.level = level
        self.life_points = life_points
        self.max_life_points = max_life_points
        self.equipment_points = equipment_points
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
        self.life_points += life_points
        # Limit of life_points
        if self.life_points > self.max_life_points:
            self.life_points = self.max_life_points

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

    def take_damage(self, damage):
        """Computes the damage received by an attack with all the fighter parameters"""
        rnd_dodge = random.random()*100
        rnd_parry = random.random()*100
        if rnd_dodge <= self.dodge_rate:
            print("Attack dodged")
            return
        elif rnd_parry <= self.parry_rate:
            print("Attack parry")
            self.loose_life_points(int((parry_reduced_damage*damage)
                                       - (self.equipment_points/equipment_balancing_points)))
        else:
            print("Full attack received")
            self.loose_life_points(int(damage - (self.equipment_points/equipment_balancing_points)))
