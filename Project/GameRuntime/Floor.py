import random
from Project.Characters.Fighter import Fighter
from Project.Items.ArmorItem import ArmorItem
from Project.GameRuntime.Texts import *
from Project.GameRuntime.UserChoice import *


class Floor:
    # Test map
    # Nb random de map
    def __init__(self, my_hero, floor, trader):
        clear_csl()
        room_number = random.randint(7, 15)
        monster_rate = 60
        trader_rate = 10
        item_rate = 15
        nothing_rate = 15
        if monster_rate + trader_rate + item_rate + nothing_rate != 100:
            raise Exception("Game not well balanced !!!")

        for room in range(1, room_number + 1):
            print("Room number", room)
            if room == room_number:
                print("Last room")

            if user_choice_yes_no("An action is about to happen, do you want to open your inventory ? Yes {y} / No {n}"):
                my_hero.show_inventory()
            else:
                rnd_action_number = random.randint(1, 100)
                if rnd_action_number <= monster_rate:
                    print("!!! Fight !!!")
                    print("TODO")
                elif rnd_action_number <= monster_rate + trader_rate:
                    print("!!! Trade !!!")
                    if user_choice_yes_no("You found a trader, do want to talk to him ? Yes {y} / No {n}"):
                        trader_greeting_text(my_hero.name)
                        while user_choice_yes_no("Would you want to buy some potions ? Yes {y} / No {n}"):
                            trader.show_available_potions()
                            if user_choice_heal_mana_potion("Which potion ? Heal {heal} / Mana {mana}"):
                                trader.sell_potion(my_hero, "heal")
                            else:
                                trader.sell_potion(my_hero, "mana")
                        print("You say goodbye to the trader and keep walking...")
                        continue
                    else:
                        print("You didn't talked to the trader and keep walking...")
                        continue
                elif rnd_action_number <= monster_rate + trader_rate + item_rate:
                    print("!!! Item !!!")
                    print("TODO")
                elif rnd_action_number <= monster_rate + trader_rate + item_rate + nothing_rate:
                    print("!!! Nothing !!!")
                    print("The room is empty. So you just go ahead...")
                    continue
                else:
                    print("!!! Nothing !!!")
                    print("The room is empty. So you just go ahead...")
                    continue


'''
# En gros j'explique
# Pour ce bloc, il faudra que pour la création de l'item ce soit random (Loot du monstre = armor ?
# si c'est oui, le random pour l'item se fera là bas)
# Ensuite, pour la mise à jour, on a pas accès a genre max_life_points donc pour la maj c'est compliqué
# donc ici je recup juste les valeurs et ensuite stats += valeur de equipment
# Sauf que, il faudrait aussi faire l'inverse, quand on enleve un item
# Donc là si tu compiles tu verras que les max_life_points (et life_points pcq on equip l'objet mais pas utile)
# Pour moi c'est comme ça qu'il faudrait faire, apres à voir, teins moi au courant
print("before equip")
my_hero.show_stats()
helmet = ArmorItem(my_hero.level, "helmet", 17, 7, 17, 17)
a, b, c, d = my_hero.equip_armor(helmet)
my_hero.max_life_points += a
my_hero.life_points += a
my_hero.max_mana_points += b
my_hero.life_points += b
my_hero.dodge_rate += c
my_hero.protection_points += d
print("new stats", my_hero.max_life_points, my_hero.max_mana_points, my_hero.dodge_rate,
      my_hero.protection_points)
print("after equip")
my_hero.show_stats()

clear_csl()
'''

# Clear la console
def clear_csl():
    for x in range(30):
        print("\n")


'''
RESTE LEVEL-UP
if floor > 1:
    # Besoin d'afficher les stats de façon propre
    # fonction level up
    my_hero.lvl_up()
    print("\n")


RESTE DU PRECEDENT CHOIX POUR LE TRADERS
# Petit truc sympa
elif choice_buy == "hi i'm here to take everything you have thanks":
    for i in range(5):
        my_hero.add_inventory("potion")
        my_hero.add_inventory("mana potion")
    print("You action won't have any consequences you are lucky")
    my_hero.add_gold(50000)
    # La transaction s'arrête
    break
# L'objet n'existe pas
else:
    print("I don't understand")
# Le joueur arrête la transaction
elif choice_buy == "nothing":
break
'''
