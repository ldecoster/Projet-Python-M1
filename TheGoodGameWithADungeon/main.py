from TheGoodGameWithADungeon.GameRuntime.Init import *
from TheGoodGameWithADungeon.GameRuntime.UserChoice import *
from TheGoodGameWithADungeon.GameRuntime.Texts import *


welcome_message()

if user_choice_1_2("Play {1} / Quit {2}"):
    print("")
    initialise_game()
else:
    print("Bye bye")
