import pickle
import os


def load_save():
    """Load the save.txt file"""
    if os.path.isfile("save.txt"):
        with open("save.txt", "rb") as file:
            my_hero = pickle.load(file)
        print("Loaded")
        return my_hero
    else:
        print("No save yet !")


def save(my_hero):
    """Save the current hero with the floor"""
    with open("save.txt", "wb") as file:
        pickle.dump(my_hero, file)
    print("Saved")
