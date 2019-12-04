from TheGoodGameWithADungeon.Characters.Hero import Hero
from TheGoodGameWithADungeon.GameRuntime.Floor import Floor
from TheGoodGameWithADungeon.Characters.Trader import Trader
from TheGoodGameWithADungeon.GameRuntime.UserChoice import *
from TheGoodGameWithADungeon.GameRuntime.save import *


def launch_game():
    print("Hello, welcome to our game.")
    print("Do you want to load a save ?")
    if user_choice_yes_no("Yes {y} / No {n}"):
        """Load the save"""
        my_hero = load_save()
    else:
        """Start a new Hero"""
        hero_name = input("Please enter your name : ")
        my_hero = Hero(name=hero_name)
        print("Your name is now : ", my_hero.name.capitalize())

    #  Game Settings
    floor = 1
    trader_price = 20


    while my_hero.is_dead() is False:
        print("Floor : ", floor)
        trader = Trader(5, trader_price, 5, trader_price)

        my_hero.show_general_stats()
        Floor(my_hero, floor, trader)

        if my_hero.is_dead() is False:
            # Once ce floor is completed, increase the trader price and "Ah shit, here we go again"
            print("New floor")
            floor += 1
            trader_price += floor + 5
        else:
            print("Sorry but you died at the floor", floor)
            print("Thanks for playing ;) noob")
            break
