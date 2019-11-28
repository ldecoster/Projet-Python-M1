def user_choice_yes_no(message):
    user_choice = ""
    while user_choice != ("y" or "n"):
        print(message)
        user_choice = input("Your choice : ")
        if user_choice == "y":
            return True
        elif user_choice == "n":
            return False


def user_choice_1_2(message):
    user_choice = ""
    while user_choice != ("1" or "2"):
        print(message)
        user_choice = input("Your choice : ")
        if user_choice == "1":
            return True
        elif user_choice == "2":
            return False


def user_choice_heal_mana_potion(message):
    user_choice = ""
    while user_choice != ("heal" or "mana"):
        print(message)
        user_choice = input("Your choice : ")
        if user_choice == "heal":
            return True
        elif user_choice == "mana":
            return False


def user_choice_lvl_up(message):
    user_choice = ""
    while user_choice != ("lifepoints" or "mana" or "damage"):
        print(message)
        user_choice = input("Your choice : ")
        if user_choice == "lifepoints":
            return "lifepoints"
        elif user_choice == "mana":
            return "mana"
        elif user_choice == "damage":
            return "damage"
