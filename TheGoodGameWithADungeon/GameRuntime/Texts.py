def welcome_message():
    print("""
    +------------------------------------------------------------------------------------+
    | Welcome to our game                                                                |
    | You will find different choices during your game                                   |
    | All you will have to do is to type the key-word that is surrounded by {}           |
    | And then press enter. If you mistype, you will be able to prompt again your choice |
    +------------------------------------------------------------------------------------+
    """)


def trader_greeting_text(hero_name):
    print("""
    Hello {}. Welcome in my shop !
    What do you want to buy ?
    I have everything you always wanted to have
    *He's looking away because he only has shitty potions*
    I'm just joking ahah
    """.format(hero_name))


def room_text(room):
    print("""
    Room number {}
    """.format(room))


def last_room_text():
    print("""
    Last room
    """)


def fight_text():
    print("""
    --- Fight ---
    """)


def trade_text():
    print("""
    --- Trade ---
    """)


def item_text():
    print("""
    --- Item ---
    """)


def nothing_text():
    print("""
    --- Nothing ---
    The room is empty. So you just go ahead...
    """)


def points_text(life_points, mana_points):
    print("""
    You have {} life points and {} mana
    """.format(life_points, mana_points))


def life_remains_text(life_points):
    print("""
    You still have {} after the fight
    """.format(life_points))


def monster_attack_text():
    print("""
    The monster is not dead yet. It attacks you
    """)


def death_text():
    print("""
    You died !
    """)


def trader_goodbye_text():
    print("""
    You say goodbye to the trader and keep walking...
    """)


def trader_not_talked_text():
    print("""
    You didn't talked to the trader and keep walking...
    """)


def trader_not_enough_gold_text():
    print("""
    Sorry, you don't have enough golds
    """)


def trader_no_more_potions_text():
    print("""
    Sorry, the potion you want have already been sold out
    """)


def trader_potions_availability(heal_potion_number, heal_potion_price, mana_potion_number, mana_potion_price):
    print("""
    I have those following potions :
    # {} heal potion(s) at a price of {} golds
    # {} mana potion(s) at a price of {} golds
    """.format(heal_potion_number, heal_potion_price, mana_potion_number, mana_potion_price))


def fighter_all_life_points_text():
    print("""
    Nothing happened. You already have all your life points
    """)


def monster_killed_text():
    print("""
    Monster killed !
    """)


def hero_max_level_text():
    print("""
    You already reached the max level
    """)


def hero_new_level_text(level):
    print("""
    *** Congratulation, you gained a new level ! ***
    You are now level {}
    """.format(level))


def hero_all_mana_points_text():
    print("""
    Nothing happened. You already have all your mana
    """)

def hero_life_points_change_text(before, after):
    print("""
    Your life points changed from {} to {}
    """.format(before, after))


def hero_mana_points_change_text(before, after):
    print("""
    Your mana points changed from {} to {}
    """.format(before, after))


def hero_no_use_heal_potion_text():
    print("""
    Potion not used as you already have all your life points
    """)


def hero_no_use_mana_potion_text():
    print("""
    Potion not used as you already have all your mana points
    """)


def hero_inventory_text(heal_potion_number, mana_potion_number, golds):
    print("""
    You have {} heal potion(s) and {} mana potion(s)
    You also have {} golds
    """.format(heal_potion_number, mana_potion_number, golds))


def hero_no_heal_potion_text():
    print("""
    You don't have any heal potion
    """)


def hero_no_mana_potion_text():
    print("""
    You don't have any mana potion
    """)


def hero_life_regained_text(life_points):
    print("""
    You regained some health. You now have {} life points
    """.format(life_points))


def hero_magic_attack_text():
    print("""
    Magic attack performed against the monster
    """)


def hero_spell_failed_text():
    print("""
    Spell failed
    """)


def hero_mana_points_after_spell_text(mana_points):
    print("""
    Mana points after the spell
    """.format(mana_points))


def hero_not_enough_mana_text():
    print("""
    Not enough mana to perform a spell. Doing a regular attack instead
    """)


def hero_improve_stat_text():
    print("""
    Choose the stat you want to improve
    """)


def hero_lvl_up_life_points_text(max_life_points):
    print("""
    Maximum life points : {} -> {})
    """.format(max_life_points-10, max_life_points))


def hero_lvl_up_mana_points_text(max_mana_points):
    print("""
    Maximum mana points : {} -> {})
    """.format(max_mana_points-10, max_mana_points))


def hero_lvl_up_damage_text(total_min_damage, total_max_damage):
    print("""
    Damage : {} / {} -> {} / {})
    """.format(total_min_damage - 3, total_max_damage - 3, total_min_damage, total_max_damage))


def hero_new_loots_text():
    print("""
    New loots received :
    """)


def hero_unknown_item_text():
    print("""
    Unknown item
    """)


def hero_new_armor_found(armor_type):
    print("""
    You found a new {}
    """.format(armor_type))


def hero_new_no_armor_text(armor_type):
    print("""
    You currently have no {}
    The new one has the following stats :
    """.format(armor_type))


def hero_new_exists_armor_text(item_type):
    print("""
    You already have an equipped {}
    Its current stats are :
    """.format(item_type))


def hero_new_armor_text(item_type):
    print("""
    The new {} has the following stats :
    """.format(item_type))


def hero_item_equipped_text(item_type):
    print("""
    {} equipped
    """.format(item_type))


def hero_item_not_equipped_text(item_type):
    print("""
    {} not equipped
    """.format(item_type))


def hero_weapon_equipped_text():
    print("""
    Weapon equipped
    """)


def hero_weapon_not_equipped_text():
    print("""
    Weapon not equipped
    """)


def hero_new_weapon_found_text():
    print("""
    You found a new weapon
    """)


def hero_weapon_1_empty_text():
    print("""
    Your weapon 1 location is empty
    The new weapon has the following stats :
    """)


def hero_weapon_2_empty_text():
    print("""
    Your weapon 2 location is empty
    The new weapon has the following stats :
    """)


def hero_weapons_not_empty_text():
    print("""
    Both weapon 1 and 2 location are not empty
    """)


def hero_weapon_1_stats_text():
    print("""
    Weapon 1 current stats are :
    """)


def hero_weapon_2_stats_text():
    print("""
    Weapon 2 current stats are :
    """)


def hero_new_weapon_stats_text():
    print("""
    The new weapon has the following stats :
    """)


def hero_jewel_equipped_text():
    print("""
    Jewel equipped
    """)


def hero_jewel_not_equipped_text():
    print("""
    Jewel not equipped
    """)


def hero_new_jewel_found_text():
    print("""
    You found a new jewel
    """)


def hero_jewel_1_empty_text():
    print("""
    Your jewel 1 location is empty
    The new jewel has the following stats :
    """)


def hero_jewel_2_empty_text():
    print("""
    Your jewel 2 location is empty
    The new jewel has the following stats :
    """)


def hero_jewels_not_empty_text():
    print("""
    Both jewel 1 and 2 location are not empty
    """)


def hero_jewel_1_stats_text():
    print("""
    Jewel 1 current stats are :
    """)


def hero_jewel_2_stats_text():
    print("""
    Jewel 2 current stats are :
    """)


def hero_new_jewel_stats_text():
    print("""
    The new jewel has the following stats :
    """)


def hero_show_stats_text(life_points, max_life_points, mana_points, max_mana_points, protection_points, dodge_rate,
                         parry_rate, critical_hit_rate, min_damage, max_damage):
    print("""
    - Life points : {}
    - Max life points : {} 
    - Mana points : {}
    - Max mana points : {}
    - Protection points : {}
    - Dodge rate : {}
    - Parry rate : {}
    - Critical hit rate : {}
    - Min damage : {}
    - Max damage : {}
     """.format(life_points, max_life_points, mana_points, max_mana_points, protection_points, dodge_rate, parry_rate,
                critical_hit_rate, min_damage, max_damage))