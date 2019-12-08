from TheGoodGameWithADungeon.Characters.Hero import Hero
from TheGoodGameWithADungeon.GameRuntime.Floor import Floor
from TheGoodGameWithADungeon.Characters.Trader import Trader
from TheGoodGameWithADungeon.GameRuntime.UserChoice import *
from TheGoodGameWithADungeon.GameRuntime.Save import *


def create_new_game():
    """Create a brand new game with default parameters"""
    print("Loading a new game...")
    hero_name = input("Please enter your name : ")
    my_hero = Hero(name=hero_name.capitalize())
    floor = 1
    trader_price = 20
    return [my_hero, floor, trader_price]


def initialise_game():
    """Config the game"""
    print("Hello, welcome to our game.")

    if user_choice_yes_no("Do you want to load a save ? Yes {y} / No {n}"):
        """Load the save"""
        game_save = load_save()
        # If none save exists yet!
        if game_save is False:
            print("There is currently none game save")
            game_parameters = create_new_game()
        # Else a save already exists, loading it
        else:
            print("Save found")
            print("Loading game with it...")
            game_parameters = game_save
    else:
        """Start a new game"""
        game_parameters = create_new_game()

    #  Game Settings
    my_hero = game_parameters[0]
    floor = game_parameters[1]
    trader_price = game_parameters[2]
    start_game(my_hero, floor, trader_price)


def start_game(my_hero, floor, trader_price):
    """Start game with defined parameters"""
    while my_hero.is_dead() is False:
        print(my_hero.name, "is now at the floor", floor)
        trader = Trader(5, trader_price, 5, trader_price)

        my_hero.show_general_stats()
        Floor(my_hero, floor, trader)

        # Once the floor is completed, increase the trader price and "Ah shit, here we go again"
        if my_hero.is_dead() is False:
            floor += 1
            trader_price += floor + 5
            if user_choice_yes_no("You've just completed a floor, would you like to save your game ? Yes {y} / No {n}"):
                save(my_hero, floor, trader_price)
                print("Game correctly saved")
            else:
                print("The game has not be saved")
        # Else the inner loop has been broken by an event, which means the hero died
        else:
            print("Sorry but you died at the floor", floor)
            print("Thanks for playing ;) noob")
            break
