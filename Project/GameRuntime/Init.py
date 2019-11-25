from Project.Characters.Character import GoldError
from Project.Characters.Hero import Hero
from Project.Items.WeaponItem import WeaponItem
from Project.Items.ArmorItem import ArmorItem
from pprint import pprint
from Project.GameRuntime.Initgame import Initgame
import random


def beginning():
    print("Hello, welcome to our game.")
    # hero_name = input("Please enter your name : ")
    hero_name = "default"
    my_hero = Hero(100, 1, 0, 0, 0.0, 0.0, 0.0, 0, 0, hero_name, 0, 10, 5, 5)

    pprint(vars(my_hero))
    print("Your name is now : " + my_hero.name)

    # Pour lancer le debut des salles
    # Si on fait une boucle, 0pb avec le level qui augmente
    Initgame(my_hero)
    # Test sur les transactions de gold
    '''
    my_hero.add_gold(50)
    print(my_hero.gold)
    try:
        my_hero.withdraw_gold(150)
    except GoldError:
        print("Fail")
    '''
    '''
    sword = WeaponItem(1, 1, 5, 12, 25)
    my_hero.equip_weapon(sword, "weapon_1")

    chestplate = ArmorItem(1, "chestplate", 74, 2.3)
    my_hero.equip_armor(chestplate)

    pprint(vars(my_hero))
    '''
