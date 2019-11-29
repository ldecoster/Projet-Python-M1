from Project.GameRuntime.Init import *
from Project.GameRuntime.UserChoice import *

while True:
    if user_choice_1_2("Welcome : Play {1} / Other {2}"):
        launch_game()
    else:
        print("Not yet implemented :(")
