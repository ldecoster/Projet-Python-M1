from Project.Characters.Character import Character


class Trader(Character):
    def __init__(self, heal_potion_number, mana_potion_number, potion_price):
        Character.__init__(self, 999999999)
        self.heal_potion_number = heal_potion_number
        self.mana_potion_number = mana_potion_number
        self.potion_price = potion_price

    def sell_to_hero(self, item, hero):
        # Add object to the hero's inventory and withdraw the gold amount
        if hero.gold > self.potion_price:
            hero.add_inventory(item)
            hero.withdraw_gold(self.potion_price)
            print("Thanks !")
        else:
            print("Sorry not enough gold !")

    def text(self):
        print("Welcome in my shop !", "\n", "What do you want to buy ?")
        print("Everything cost ", self.potion_price)
        print("I have everything you always wanted to have")
        print("he's looking away because he only has shitty potions")
        print("Joking I only have : heal potions, mana potions")
        print("Do you want to buy some ?")
        print("Heal potion : ", self.potion_price, "Mana potion : ", self.potion_price, "Nothing : Free of course now "
                                                                                        "leave")

