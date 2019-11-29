from Project.Characters.Hero import Hero
from Project.GameRuntime.Floor import Floor
from Project.Characters.Trader import Trader


def launch_game():
    print("Hello, welcome to our game.")
    hero_name = input("Please enter your name : ")

    my_hero = Hero(name=hero_name, gold=1000000)
    print("Your name is now : ", my_hero.name.capitalize())

    #  Game Settings
    floor = my_hero.level
    trader_price = 20
    print("floor", floor)
    while my_hero.is_dead() is False:
        trader = Trader(5, trader_price, 5, trader_price)

        Floor(my_hero, floor, trader)

        floor += 1
        trader_price += floor + 5

    '''
    while not monster.has_been_killed(my_hero):
        my_hero.attack(monster)
        print("------------------------------")
    '''
