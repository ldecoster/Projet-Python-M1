class Stats:
    def __init__(self):
        self.monster_killed_number = 0
        self.heal_potions_used_number = 0
        self.mana_potions_used_number = 0
        self.heal_potions_bought_number = 0
        self.mana_potions_bought_number = 0
        self.attacks_performed_number = 0
        self.spells_performed_number = 0
        self.life_points_lost = 0
        self.life_points_gained = 0
        self.mana_gained = 0
        self.mana_consummed = 0

    def show_general_stats(self):
        print("")
        print("Here are all your stats :")
        print("")
        print("Monster killed : ", self.monster_killed_number)
        print("Heal potions used : ", self.heal_potions_used_number)
        print("Mana potions used : ", self.heal_potions_used_number)
        print("Heal potions bought : ", self.heal_potions_bought_number)
        print("Mana potions bought : ", self.mana_potions_bought_number)
        print("Number of attacks : ", self.attacks_performed_number)
        print("Number of spells : ", self.spells_performed_number)
        print("Life points lost : ", self.life_points_lost)
        print("Life points regained : ", self.life_points_gained)
        print("Mana regained : ", self.mana_gained)
        print("Mana consummed : ", self.mana_consummed)
        print("")
