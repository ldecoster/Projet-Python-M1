from Projet.player import player
from Projet.enemy import enemy
from Projet.map import map

class game:
    def __init__(self):
        print("main")
        while player.dead() is False and enemy.dead() is False:
            self.play()
            if player.dead() is True:
                print("Player dead, end of the game")
            if enemy.dead() is True:
                print("Fin combat")


    # Tour par tour pas encore fait, pour l'instant seulement le joueur peut jouer
    # Fin de combat possible, pas encore le changement de map, on peut juste faire un combat pour l'instant
    # Manque également l'xp qui je pense, sera par etage, etage 1 = lvl 1, comme j'avais dit, beaucoup plus simple
    # Seul le choix de la stats à ameliorer ainsi que le drop aleatoire d'objet (pas encore fait mais j'ai une idée de comment faire)
    # fera que les parties sont différentes les une des autres
    def play(self):
        print("Combat ! Stats de l'enemy : ", enemy.stats)
        while player.stats[0] > 0 and enemy.stats[0] > 0:
            print("HP/mana player : ", player.stats[0], " - ", player.stats[1])
            print("HP enemy : ", enemy.stats[0])
            print("Que faire ?")
            # 4 test de la fonction defense pour tester si le joueur est mort ou vivant (fonctionnel mais à laisser pour plus tard)
            print("1 : Attaquer", "2 : magie", "3 : inventaire", "4 : defense")
            move = int(input())
            if move == 1:
                player.attack(player.stats[9])
            elif move == 2:
                print("Choix de la magie : ")
                player.magical()
            elif move == 3:
                print("Inventaire : ", player.inventory)
            elif move == 4:
                print("TEST DEFENSE")
                player.defense(99)
            if enemy.dead() is True:
                print("Combat terminé")


game = game()