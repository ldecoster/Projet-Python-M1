from Project.Items.Item import Item
import random


class WeaponItem(Item):
    def __init__(self, level, parry_rate, critical_hit_rate, min_damage, max_damage):
        super().__init__(level)
        self.parry_rate = parry_rate
        self.critical_hit_rate = critical_hit_rate
        self.min_damage = min_damage
        self.max_damage = max_damage
        #display pour verifier dans monstre
        self.display_stats()

    def display_stats(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print("The weapon minimum damages are :", self.min_damage)
        print("The weapon maximum damages are :", self.max_damage)
        print("The weapon give", self.parry_rate, "% chance to parry an attack")
        print("The weapon give", self.critical_hit_rate, "% chance to inflict a critical hit")
        print("+++++++++++++++++++++++++++++++++++++++++++++")


"""
# generation au hasard des stats (test enleve pas)
rnd_parry = random.randint(0,5)
rnd_crit = random.randint(0,5)
rnd_min = random.randint(5,10)
rnd_max = random.randint(rnd_min+3,18)
armortype = "pants"
level = 3
WeaponItem = WeaponItem(level, rnd_parry, rnd_crit, rnd_min, rnd_max)
WeaponItem.display_stats()
"""