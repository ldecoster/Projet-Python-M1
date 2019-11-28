import random
from Project.Characters.Fighter import Fighter
from Project.Items.ArmorItem import ArmorItem


class Initgame:
    # Test map
    # Nb random de map
    def __init__(self, my_hero, floor, trader):
        clear_csl()
        nb_map = random.randint(7, 15)
        # Les différents if seront modifiés (par rapport aux while), je testais un truc
        for room in range(1, nb_map + 1):
            # % de chance d'avoir un combat (75% de chance parait bien, avec pq pas un faible % de chance d'avoir un item ?)
            rnd_mob = random.randint(1, 100)
            # Marchand premiere map à chaque étage ?
            if room == 1:
                if floor > 1:
                    # Besoin d'afficher les stats de façon propre
                    # fonction level up
                    my_hero.lvl_up()
                    print("\n")
                print("First room")
                print("1 : continuer 2 : inventaire 3 : marchand")
                choice = int(input())
                # Pas optimisé du tout, y'a large mieux mais j'ai gardé pour tester des trucs vite fait
                if choice == 1:
                    print("Continuer")
                    # Pas de fonctions nécéssaire (sauf si vraiment nécéssaire)
                while choice != 1:
                    if choice == 2:
                        # afficher l'inventaire
                        print("inventaire : ")
                        my_hero.show_inventory()
                    elif choice == 3:
                        trader.text()
                        choice_buy = ""
                        """Le joueur écrit ce qu'il veut acheter"""
                        while choice_buy != "nothing":
                            choice_buy = str(input())
                            if choice_buy != "nothing":
                                # On verifie que l'objet existe
                                if choice_buy == "potion" or choice_buy == "mana potion":
                                    # Ajout de l'objet dans l'inventaire + retrait argent
                                    trader.sell_to_hero(choice_buy, my_hero)
                                    print("Something else ?")
                                # Petit truc sympas
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
                    # Test ajout item
                    elif choice == 4:
                        # En gros j'explique
                        # Pour ce bloc, il faudra que pour la création de l'item ce soit random (Loot du monstre = armor ?
                        # si c'est oui, le random pour l'item se fera là bas)
                        # Ensuite, pour la mise à jour, on a pas accès a genre max_life_points donc pour la maj c'est compliqué
                        # donc ici je recup juste les valeurs et ensuite stats += valeur de equipment
                        # Sauf que, il faudrait aussi faire l'inverse, quand on enleve un item
                        #Donc là si tu compiles tu verras que les max_life_points (et life_points pcq on equip l'objet mais pas utile)
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
                        print("new stats", my_hero.max_life_points, my_hero.max_mana_points, my_hero.dodge_rate, my_hero.protection_points)
                        print("after equip")
                        my_hero.show_stats()
                    print("1 : continuer 2 : inventaire 3 : marchand")
                    choice = int(input())
                    if choice == 1:
                        print("Continuer")
                        # Pas de fonctions nécéssaire (sauf si vraiment nécéssaire)
            elif 2 <= room <= nb_map - 1:
                print("mid room")
                if rnd_mob <= 75:
                    print("Combat")
                    # fonction combat
                else:
                    print("Pas de combat")
                print("1 : Continuer 2 : inventaire")
                choice = int(input())
                while choice != 1:
                    if choice == 1:
                        print("Continuer")
                        # Pas de fonctions nécéssaire (sauf si vraiment nécéssaire)
                    elif choice == 2:
                        # Afficher l'inventaire
                        print("inventaire")
                        my_hero.show_inventory()
                    print("1 : Continuer 2 : inventaire")
                    choice = int(input())

            elif room == nb_map:
                choice = 0
                print("last room")
                print("1 : Etage suivant 2 : inventaire")
                choice = int(input())
                # changement d'etage
                if choice == 1:
                    print("Etage suivant")
                # Affichage inventaire + choix de continuer ou de revoir l'inventaire
                while choice != 1:
                    if choice == 2:
                        # Afficher l'inventaire
                        print("inventaire")
                        my_hero.show_inventory()
                    print("1 : Etage suivant 2 : inventaire")
                    choice = int(input())

            clear_csl()

# Clear la console
def clear_csl():
    for x in range(30):
        print("\n")
