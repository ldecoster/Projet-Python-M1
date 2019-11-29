from Project.Characters.Character import Character
from Project.Items.Inventory import Inventory
from Project.Items.Potion import Potion


class Trader(Character, Inventory, Potion):
    def __init__(self, heal_potion_number, heal_potion_price,
                 mana_potion_number, mana_potion_price):
        Character.__init__(self, 999999999)
        Inventory.__init__(self)
        self.heal_potion_number = heal_potion_number
        self.heal_potion_price = heal_potion_price
        self.mana_potion_number = mana_potion_number
        self.mana_potion_price = mana_potion_price
        # Creation of all the potions into the Trader's inventory
        for i in range(self.heal_potion_number):
            self.inventory.append(Potion("heal", self.heal_potion_price))
        for j in range(self.mana_potion_number):
            self.inventory.append(Potion("mana", self.mana_potion_price))

    def sell_potion(self, hero, hero_potion_type_choice):
        """Sell potion to the hero by doing a trade of golds"""
        if hero_potion_type_choice == "heal":
            potion_number = self.heal_potion_number
            potion_price = self.heal_potion_price
        elif hero_potion_type_choice == "mana":
            potion_number = self.heal_potion_number
            potion_price = self.heal_potion_price
        else:
            raise Exception("Error")

        if potion_number > 0:
            if hero.gold >= potion_price:
                try:
                    hero.withdraw_gold(potion_price)
                    potion = self.remove_potion(hero_potion_type_choice)
                    hero.add_item(potion)
                    self.add_gold(potion_price)
                except Exception as e:
                    print(str(e))
            else:
                print("Sorry, you don't have enough golds")
        else:
            print("Sorry, the potion you want have been already sold out")

    def show_available_potions(self):
        """Print which potions the trader has to sell"""
        print("I have those following potions : ")
        print("#", self.heal_potion_number, "heal potion(s) at a price of", self.heal_potion_price, "golds")
        print("#", self.mana_potion_number, "mana potion(s) at a price of", self.mana_potion_price, "golds")
