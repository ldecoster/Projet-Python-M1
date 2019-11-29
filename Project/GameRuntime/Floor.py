import random
from Project.Characters.Fighter import Fighter
from Project.Characters.Hero import Hero
from Project.Characters.Monster import Monster
from Project.Items.ArmorItem import ArmorItem
from Project.Items.RandomItem import RandomItem
from Project.GameRuntime.Texts import *
from Project.GameRuntime.UserChoice import *


class Floor:
    def __init__(self, my_hero, floor, trader):
        clear_csl()
        room_number = random.randint(7, 15)  # Random number of maps

        monster_rate = 58
        trader_rate = 9
        item_rate = 18
        nothing_rate = 15
        if monster_rate + trader_rate + item_rate + nothing_rate != 100:
            raise Exception("Game not well balanced !!!")

        if isinstance(my_hero, Hero):
            for room in range(1, room_number + 1):
                if my_hero.is_dead():
                    break
                else:
                    print("")
                    print("")
                    print("~ Room number", room)
                    if room == room_number:
                        print("Last room")
                    else:
                        print("")
                        if user_choice_yes_no("An action is about to happen, do you want to open your inventory ?"
                                              " Yes {y} / No {n}"):
                            my_hero.show_inventory()
                        rnd_action_number = random.randint(1, 100)
                        if rnd_action_number <= monster_rate:
                            print("--- Fight ---")
                            monster = Monster(my_hero.level)
                            while True:
                                print("You have", my_hero.life_points, "life points and", my_hero.mana_points, "mana")
                                if user_choice_attack("You are about to attack a monster."
                                                      " Would like to use a {spell} or a regular attack {reg} ?"):
                                    # Magic attack
                                    if user_choice_spell("Which spell to use ? {heal} / {damage}"):
                                        my_hero.magical_spell()
                                    else:
                                        my_hero.magical_spell(monster)
                                # Regular attack
                                else:
                                    my_hero.attack(monster)
                                # If the attack killed the monster, get the rewards and break the loop
                                if monster.has_been_killed(my_hero):
                                    my_hero.add_gold(monster.gold)
                                    my_hero.gain_experience(monster.loot_experiences)
                                    print("You still have", my_hero.life_points, "after the fight")
                                    break
                                # Else, time to the monster to attack the hero
                                else:
                                    print("The monster is not dead yet. It attacks you")
                                    monster.attack(my_hero)
                                    if my_hero.is_dead():
                                        break
                            if my_hero.is_dead():
                                print("You died !")
                                break
                        elif rnd_action_number <= monster_rate + trader_rate:
                            print("--- Trade ---")
                            if user_choice_yes_no("You found a trader, do want to talk to him ? Yes {y} / No {n}"):
                                trader_greeting_text(my_hero.name)
                                while user_choice_yes_no("Would you want to buy some potions ? Yes {y} / No {n}"):
                                    trader.show_available_potions()
                                    if user_choice_heal_mana_potion("Which potion ? Heal {heal} / Mana {mana}"):
                                        trader.sell_potion(my_hero, "heal")
                                    else:
                                        trader.sell_potion(my_hero, "mana")
                                print("You say goodbye to the trader and keep walking...")
                                continue
                            else:
                                print("You didn't talked to the trader and keep walking...")
                                continue
                        elif rnd_action_number <= monster_rate + trader_rate + item_rate:
                            print("--- Item ---")
                            item = RandomItem(my_hero.level)
                            my_hero.deal_with_new_loot(item.item)
                            my_hero.update()
                        elif rnd_action_number <= monster_rate + trader_rate + item_rate + nothing_rate:
                            print("--- Nothing ---")
                            print("The room is empty. So you just go ahead...")
                            continue
                        else:
                            print("--- Nothing ---")
                            print("The room is empty. So you just go ahead...")
                            continue
        else:
            raise Exception("Fatal exception, you failed at coding your own game")


# Clear la console
def clear_csl():
    for x in range(5):
        print("\n")
