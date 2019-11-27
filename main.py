from Project.GameRuntime.Init import beginning

print("Bienvenue dans le jeu !")
choice = 0
while choice != 1:
    print("1 : Jouer 2 : faire un truc ?")
    choice = int(input())
    if choice == 1:
        beginning()
    elif choice == 2:
        print("faire un autre truc ?")
