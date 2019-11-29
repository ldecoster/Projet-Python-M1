from Project.GameRuntime.Init import *
from Project.GameRuntime.UserChoice import *

if user_choice_1_2("Welcome : Play {1} / Quit {2}"):
    launch_game()
else:
    print("Bye bye")
