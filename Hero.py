from Project.Characters.Fighter import Fighter
from Project.Items.HeroEquipment import HeroEquipment


class Hero(Fighter, HeroEquipment):
    def __init__(self, gold, level, life_points, max_life_points, equipment_points, dodge_rate, parry_rate,
                 critical_hit_rate, min_damage, max_damage,
                 name, exp_points, mana_points, max_mana_points, total_min_damage, total_max_damage, loots_inventory):
        Fighter.__init__(self, gold, level, life_points, max_life_points, equipment_points, dodge_rate, parry_rate,
                         critical_hit_rate, min_damage, max_damage, loots_inventory)
        HeroEquipment.__init__(self)
        self.name = name
        self.exp_points = exp_points
        self.mana_points = mana_points
        self.max_mana_points = max_mana_points
        self.total_min_damage = total_min_damage
        self.total_max_damage = total_max_damage
        self.inventory = ["item1", "item2", "item3"]

    def update(self):
        # just in case
        self.update_offensive_stats()
        self.update_defensive_stats()
        self.total_min_damage = self.min_damage + self.equipment_min_damage
        self.total_max_damage = self.max_damage + self.equipment_max_damage

    def receive_loots(self, loots):
        self.loots_inventory = loots
        print("Loots received")
        # To Do : Dequeue loots

    def show_inventory(self):
        #On peut pas faire plus simple ptdr
        for item in self.inventory:
            print(item)
        print("Utiliser un item ?")
        print("1 : oui 2 : non")
        choice = int(input())
        if choice == 1:
            #Pareil faudra rajouter dans la fonction use_item si l'item existe
            print("Utiliser quel objet ?")
            choice = str(input())
            #Si item existe alors
            self.use_item(choice)
            #Sinon
            #Message d'erreur


    def add_inventory(self, item):
        # verifier si l'inventaire n'est pas plein (si on met une limite)
        self.inventory.append(item)

    def remove_inventory(self, item):
        # verifier que l'item existe dans l'inventaire
        self.inventory.remove(item)

    def use_item(self, item):
        # Verifier si l'item est présent dans l'inventaire à rajouter sinon ça crash
        # potion de soin /////// item == "item1" pour des test
        if item == "potion" or item == "item1":
            # fonction heal
            print("before heal")
            print(self.life_points)
            self.life_points += 5
            print("After heal")
            print(self.life_points)
            self.remove_inventory(item)
        # potion de mana
        elif item == "mana":
            # fonction mana
            print("before mana")
            print(self.mana_points)
            self.mana_points += 5
            print("after mana")
            print(self.mana_points)
            self.remove_inventory(item)
        else:
            print("Can't use this item")