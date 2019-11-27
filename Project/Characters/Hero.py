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
        self.max_mana_points = 7
        self.total_min_damage = total_min_damage
        self.total_max_damage = total_max_damage
        self.inventory = ["potion", "potion", "mana potion"]

    def show_stats(self):
        print(vars(self))

    def gain_mana(self, mana):
        """Give back mana_points to the fighter"""
        # Limit of mana_points
        if self.mana_points == self.max_mana_points:
            self.mana_points = self.max_mana_points
            return False
        # mana_point inférieur a max_mana_points mais mana_point + mana supérieur a max_mana_points
        elif mana + self.mana_points > self.max_mana_points:
            self.mana_points = self.max_mana_points
            return True
        # regeneration de mana
        elif self.mana_points < self.max_mana_points:
            self.mana_points += mana
            return True

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
        potion = 0
        mana_potion = 0
        # Compteur pour afficher le nombre de potion et de mana potion
        for item in self.inventory:
            if item == "potion":
                potion += 1
            elif item == "mana potion":
                mana_potion += 1
        print("potion : ", potion, "mana potion", mana_potion, "gold : ", self.gold)
        print("Utiliser un item ?")
        print("1 : oui 2 : non")
        choice = int(input())
        if choice == 1:
            print("Utiliser quel objet ?")
            choice = str(input())
            # On vérifie que l'item existe
            if choice == "potion" or choice == "mana potion":
                self.use_item(choice)
            else:
                print("This item doesn't exist or I just can't use it")

    def add_inventory(self, item):
        # verifier si l'inventaire n'est pas plein (si on met une limite)
        self.inventory.append(item)

    def remove_inventory(self, item):
        # verifier que l'item existe dans l'inventaire pas trop utile en soit cette fonction je pense
        self.inventory.remove(item)

    def use_item(self, item):
        # potion de soin
        if item == "potion" or item == "item1":
            # fonction heal
            before = self.life_points
            use = self.heal_life_point(10)
            print("Life points : ", before, "->", self.life_points)
            if use is True:
                self.remove_inventory(item)
            else:
                print("You keep your potion")
        # potion de mana
        elif item == "mana potion":
            # fonction mana
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
        """Augmentation de niveau + augmentation d'une stats + full heal"""
        self.level += 1
        print("Level up ! You are now level : ", self.level, "\n Choose to stats to improve")
        print("pv mana damage")
        stats = str(input())
        if stats == "pv":
            self.max_life_points += 10
            print("Maximum life points : ", self.max_life_points - 10, "->", self.max_life_points)
        elif stats == "mana":
            self.max_mana_points += 5
            print("Maximum mana points : ", self.max_mana_points - 5, "->", self.max_mana_points)
        elif stats == "damage":
            self.total_min_damage += 3
            self.total_max_damage += 3
            print("Damage : ", self.total_min_damage - 3, "-", self.total_max_damage-3, "->", self.total_min_damage, "-", self.total_max_damage)
        # full heal
        self.life_points = self.max_life_points
        self.mana_points = self.max_mana_points
