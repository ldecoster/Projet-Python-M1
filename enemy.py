import random

#from Projet.player import player


class enemy:
    def __init__(self):
        self.value = []
        self.stats = self.readstats()
        print("enemy init")

    def readstats(self):
        f = open("enemy.txt", 'r')
        lignes = f.readlines()
        f.close()
        for ligne in lignes:
            self.value.append(int(ligne))
        self.stats = self.value
        return self.stats

    def attack(self, damage):
        # rnd to see if we crit
        print("before hit", player.stats[0])
        rnd_crit = random.randint(1, 100)
        if rnd_crit <= int(self.stats[5]):
            print("Critical hit")
            damage = damage * 2
        player.defense(damage)
        print("After hit", player.stats[0])


    def lose_life(self, damage):
        life = self.stats[0]
        life_int = int(life)
        life_int -= damage
        self.stats[0] = life_int
        return self.stats[0]

    def dead(self):
        if self.stats[0] <= 0:
            return True
        elif self.stats[0] > 0:
            return False

    #Pareil, faire une fonction heal etc, Fonction commune ?

enemy = enemy()