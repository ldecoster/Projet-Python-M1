import pickle
import os


def load_save():
    """Load the save file"""
    if os.path.isfile("save"):
        with open("save", "rb") as file:
            my_hero = pickle.load(file)
            floor = pickle.load(file)
            trader_price = pickle.load(file)
            return [my_hero, floor, trader_price]
    return False


def save(my_hero, floor, trader_price):
    """Save the current hero with the floor and trader price"""
    with open("save", "wb+") as file:
        pickle.dump(my_hero, file)
        pickle.dump(floor, file)
        pickle.dump(trader_price, file)
