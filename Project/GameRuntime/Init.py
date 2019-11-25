from Project.Characters.Hero import Hero
from pprint import pprint


def beginning():
    print("Hello, welcome to our game.")
    hero_name = input("Please enter your name : ")
    my_hero = Hero(0, 1, 0, 0, 0.0, 0.0, 0, 0, hero_name, 0, 0.0, 10)

    pprint(vars(my_hero))
    print("Your name is now : " + my_hero.name)
