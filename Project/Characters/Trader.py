from Project.Characters.Character import Character


class Trader(Character):
    def __init__(self):
        Character.__init__(self, 999999999)
        self.potion = 5
        self.mana_potion = 5
        self.potion_price = 10

    def sell(self, item, my_hero):
        # L'objet est ajouté a l'inventaire et les gold retirés
        if my_hero.gold > self.potion_price:
            my_hero.add_inventory(item)
            my_hero.withdraw_gold(self.potion_price)
            print("Thanks !")
        else:
            print("Sorry not enough gold !")

    def text(self):
        print("Welcome in my shop !", "\n", "What do you want to buy ?")
        print("Everything cost ", self.potion_price)
        print("I have everything you always wanted to have", "\n", "he looks away because he only have shitty potion")
        print("Joking I only have : Potion, mana potion")
        print("Do you want to buy some ?")
        print("Potion : ", self.potion_price, "Mana potion : ", self.potion_price, "Nothing : Free of course now leave")

