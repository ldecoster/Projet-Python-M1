from Project.Characters.Hero import Hero
from Project.GameRuntime.Floor import Floor
from Project.Characters.Trader import Trader


def launch_game():
    print("Hello, welcome to our game.")
    hero_name = input("Please enter your name : ")

    my_hero = Hero(name=hero_name, gold=1000000)
    print("Your name is now : ", my_hero.name.capitalize())

    #  Game Settings
    floor = 1
    trader_price = 20

    while my_hero.is_dead() is False:
        print("Floor : ", floor)
        trader = Trader(5, trader_price, 5, trader_price)

        Floor(my_hero, floor, trader)

        # Once ce floor is completed, increase the trader price and "Ah shit, here we go again"
        print("New floor")
        floor += 1
        trader_price += floor + 5

    '''
    while not monster.has_been_killed(my_hero):
        my_hero.attack(monster)
        print("------------------------------")
    '''
