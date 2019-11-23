import numpy as np
import random

#from Projet.enemy import enemy

class player:
    def __init__(self):
        # On peut aussi faire 1 getter pour chaque stats + enlever chaque cast en int (devenu inutile j'ai changé une ligne de code pour tout recuperer directement en int)
        self.value = []
        self.stats = self.readstats()
        self.maxpv = self.stats[0]
        self.maxmana = self.stats[1]
        #  Not necessary, just to remember which index correspond to which stat
        '''self.life = self.stats[0]
        self.mana = self.stats[1]
        self.shield = self.stats[2]
        self.dodge = self.stats[3]
        self.parry = self.stats[4]
        self.crit = self.stats[5]
        self.armor = self.stats[6]
        self.speed = self.stats[7]
        self.level = self.stats[8]
        self.power = self.stats[9]
        print(self.stats)'''
        self.defense(10)

    def initname(self):
        print("Name : ")
        self.name = str(input())
        return self.name

    def readstats(self):
        f = open("character.txt", 'r')
        lignes = f.readlines()
        f.close()
        # all the stats are in an array, self.stats[0] is character life for example
        for ligne in lignes:
            self.value.append(int(ligne))
        self.stats = self.value
        return self.stats

    def attack(self, damage, magical = 1):
        #rnd to see if we crit
        print("before hit", enemy.stats[0])
        rnd_crit = random.randint(1, 100)
        if rnd_crit <= int(self.stats[5]) and magical != 0:
            print("Critical hit")
            damage = damage * 2
        enemy.lose_life(damage)
        print("After hit", enemy.stats[0])

    def defense(self, damage):
        # random to check the defense system
        rnd_dodge = random.randint(1, 100)
        rnd_parry = random.randint(1, 100)
        # Parry if
        if rnd_parry <= int(self.stats[4]):
            print("Parry")
            damage = damage - (int(self.stats[6])/2) * 0.7
        # Dodge if
        elif rnd_parry > int(self.stats[4]) and rnd_dodge <= int(self.stats[3]):
            print("Dodge")
            damage = 0
        # Nothing if
        elif rnd_parry > int(self.stats[4]) and rnd_dodge > int(self.stats[3]):
            print("Nothing")
            damage = damage - (int(self.stats[6])/2)

        life = int(self.stats[0])
        life -= int(damage)
        self.stats[0] = life

    def magical(self):
        print("Spell =")
        spell = int(input())
        print("magical attack")
        # Choix du spell
        if int(self.stats[1]) > 0:
            #Condition pour le lancer
            if spell == 1 and int(self.stats[1]) >= 5:
                print("Life before Heal")
                print(self.stats[0])
                # On soigne
                self.healing(5)
                #On enleve le mana utilisé
                self.consumeMana(5)
                print("after heal", self.stats[0])
            elif spell == 2 and int(self.stats[1]) >= 10:
                print("Fireball")
                mdamage = 5
                self.consumeMana(10)
                self.attack(0)

    def healing(self, heal):
        #Heal if player hp < max hp and player hp < heal for example, 33hp/100hp
        if int(self.stats[0]) <= (int(self.maxpv) - heal):
            self.stats[0] = int(self.stats[0]) + heal
            print("Life after heal 1", self.stats[0])

        #Heal if player hp < max hp and player hp > heal for example, 98hp/100hp, avoid to have player hp > max hp (103hp/100)
        elif int(self.maxpv) - heal < int(self.stats[0]) < int(self.maxpv):
            self.stats[0] = self.maxpv
            print("Life after heal 2", self.stats[0])

        # Heal if player hp == max hp, avoid to have too much hp (explained in the previous elif)
        elif int(self.stats[0]) == int(self.maxpv):
            #  Ajouter une condition pour les sorts/objets
            print("Already full life, losing your mana/item")
        return self.stats[0]

    def consumeMana(self, mana):
        self.stats[1] = int(self.stats[1]) - mana
        return self.stats[1]


player = player()