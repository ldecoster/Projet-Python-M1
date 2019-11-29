from Project.Characters.Character import GoldError
from Project.Characters.Hero import Hero
from Project.Items.WeaponItem import WeaponItem
from Project.Items.ArmorItem import ArmorItem
from Project.Characters.Fighter import Fighter
from Project.Characters.Monster import Monster
from pprint import pprint
from Project.GameRuntime.Initgame import Initgame
from Project.Characters.Trader import Trader
import random


def beginning():
    print("Hello, welcome to our game.")
    # hero_name = input("Please enter your name : ")
    hero_name = "default"

    gold = 100
    level = 1
    life_points = 100
    max_life_points = 100
    equipment_points = 0
    dodge_rate = 0.0
    parry_rate = 0.0
    critical_hit_rate = 0.0
    min_damage = 1
    max_damage = 10
    exp_points = 0
    mana_points = 10
    max_mana_points = 20
    total_min_damage = 1
    total_max_damage = 10
    loots_inventory = []

    my_hero = Hero(gold, level, life_points, max_life_points, equipment_points,
                   dodge_rate, parry_rate, critical_hit_rate,
                   min_damage, max_damage, hero_name, exp_points,
                   mana_points, max_mana_points, total_min_damage, total_max_damage, loots_inventory)
    trader = Trader(5, 20, 5, 20)

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
    
    sword = WeaponItem(1, 1, 5, 12, 25)
    sword2 = WeaponItem(1, 2, 30, 5, 15)
    my_hero.equip_weapon(sword, "weapon_1")
    my_hero.equip_weapon(sword, "weapon_2")

    chestplate = ArmorItem(1, "chestplate", 74, 2.3)
    my_hero.equip_armor(chestplate)

    my_hero.update()
    # pprint(vars(my_hero))

    monster = Monster(10, 1, 100, 100, 20, 10, 20, 15, 10, 50, [sword2, chestplate])

    while not monster.has_been_killed(my_hero):
        my_hero.attack(monster)
        print("------------------------------")
    '''
    # pprint(vars(my_hero))
    # pprint(vars(monster))
    # print(monster.is_dead())

