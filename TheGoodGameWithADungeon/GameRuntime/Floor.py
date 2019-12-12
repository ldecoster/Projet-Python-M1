import random
from TheGoodGameWithADungeon.Characters.Hero import Hero
from TheGoodGameWithADungeon.Characters.Monster import Monster
from TheGoodGameWithADungeon.Items.RandomItem import RandomItem
from TheGoodGameWithADungeon.GameRuntime.Texts import *
from TheGoodGameWithADungeon.GameRuntime.UserChoice import *


class Floor:
    def __init__(self, my_hero, floor, trader):
        room_number = random.randint(7, 12)  # Random number of maps

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
                    room_text(room)
                    if room == room_number:
                        last_room_text()

                    if user_choice_yes_no("An action is about to happen, do you want to open your inventory ?"
                                          " Yes {y} / No {n}"):
                        my_hero.show_inventory()

                    rnd_action_number = random.randint(1, 100)
                    if rnd_action_number <= monster_rate:
                        fight_text()
                        monster = Monster(my_hero.level)
                        while True:
                            points_text(my_hero.life_points, my_hero.mana_points)
                            while user_choice_attack("You are about to attack a monster."
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
                                my_hero.monster_killed_number += 1  # stats
                                life_remains_text(my_hero.life_points)
                                break
                            # Else, time to the monster to attack the hero
                            else:
                                monster_attack_text()
                                monster.attack(my_hero)
                                if my_hero.is_dead():
                                    break
                        if my_hero.is_dead():
                            death_text()
                            break
                    elif rnd_action_number <= monster_rate + trader_rate:
                        trade_text()
                        if user_choice_yes_no("You found a trader, do want to talk to him ? Yes {y} / No {n}"):
                            trader_greeting_text(my_hero.name)
                            while user_choice_yes_no("Would you want to buy some potions ? Yes {y} / No {n}"):
                                trader.show_available_potions()
                                if user_choice_heal_mana_potion("Which potion ? Heal {heal} / Mana {mana}"):
                                    trader.sell_potion(my_hero, "heal")
                                    my_hero.heal_potions_bought_number += 1  # stats
                                else:
                                    trader.sell_potion(my_hero, "mana")
                                    my_hero.mana_potions_bought_number += 1  # stats
                            trader_goodbye_text()
                            continue
                        else:
                            trader_not_talked_text()
                            continue
                    elif rnd_action_number <= monster_rate + trader_rate + item_rate:
                        item_text()
                        item = RandomItem(my_hero.level)
                        my_hero.deal_with_new_loot(item.item)
                        my_hero.update()
                    elif rnd_action_number <= monster_rate + trader_rate + item_rate + nothing_rate:
                        nothing_text()
                        continue
                    else:
                        nothing_text()
                        continue
        else:
            raise Exception("Fatal exception, you failed at coding your own game")
