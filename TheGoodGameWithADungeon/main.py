from TheGoodGameWithADungeon.GameRuntime.Init import *
from TheGoodGameWithADungeon.GameRuntime.UserChoice import *

if user_choice_1_2("Welcome : Play {1} / Quit {2}"):
    initialise_game()
else:
    print("Bye bye")
