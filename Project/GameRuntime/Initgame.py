import random
from Project.Characters.Fighter import Fighter

class Initgame:
    # Test map
    # Nb random de map
    def __init__(self, my_hero):
        nb_map = random.randint(7, 15)
        # Les différents if seront modifiés (par rapport aux while), je testais un truc
        for room in range(1, nb_map + 1):
            # % de chance d'avoir un combat (75% de chance parait bien, avec pq pas un faible % de chance d'avoir un item ?)
            rnd_mob = random.randint(1, 100)
            # Marchand premiere map à chaque étage ?
            if room == 1:
                print("First room")
                print("1 : continuer 2 : inventaire 3 : marchand")
                choice = int(input())
                # Pas optimisé du tout, y'a large mieux mais j'ai gardé pour tester des trucs vite fait
                if choice == 1:
                    print("Continuer")
                    #Pas de fonctions nécéssaire (sauf si vraiment nécéssaire)
                while choice != 1:
                    if choice == 2:
                        print("inventaire")
                        # Fonction voir l'inventaire (utiliser objets ?)
                    elif choice == 3:
                        print("Marchand")
                        # Fonction marchand
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
                        print("inventaire")
                        # Fonction voir l'inventaire (utiliser objets ?)
                    print("1 : Continuer 2 : inventaire")
                    choice = int(input())

            elif room == nb_map:
                print("last room")
                print("1 : Etage suivant 2 : inventaire")
                choice = int(input())
                if choice == 1:
                    print("Etage suivant")
                    # level up ?
                    my_hero.level = my_hero.level+1
                    print("Level up : ", my_hero.level - 1, "->", my_hero.level)
                    # Fonction level up (choix d'1 ou +sieurs stats à augmenter ? en plus des autres ?)
                # Ce while posera le plus de pb, sio n hcoisit d'abord inventaire puis etage suivant c'est relou, et pas tres propre de mettre 2 fois le même if,
                # genre 1 avant et 1 dedans (comme dans le premier if)
                while choice != 1:
                    if choice == 2:
                        print("inventaire")
                        # Fonction voir l'inventaire (utiliser objets ?)
                    print("1 : Etage suivant 2 : inventaire")
                    choice = int(input())
