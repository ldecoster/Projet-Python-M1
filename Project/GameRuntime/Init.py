from Project.Characters.Character import GoldError
from Project.Characters.Hero import Hero
from Project.Items.WeaponItem import WeaponItem
from Project.Items.ArmorItem import ArmorItem
from pprint import pprint
from Project.GameRuntime.Initgame import Initgame
from Project.Characters.Trader import Trader
import random


def beginning():
    print("Hello, welcome to our game.")
    # hero_name = input("Please enter your name : ")
    hero_name = "default"
    my_hero = Hero(100, 1, 100, 0, 0.0, 0.0, 0.0, 0, 0, hero_name, 0, 10, 5, 5, 5, 5, 0)
    trader = Trader()

    pprint(vars(my_hero))
    print("Your name is now : ", my_hero.name)

    # Lancement des étages
    floor = my_hero.level
    print("floor", floor)
    while my_hero.is_dead() is False:
        Initgame(my_hero, floor, trader)
        floor += 1
        trader.potion_price += floor + 5
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
