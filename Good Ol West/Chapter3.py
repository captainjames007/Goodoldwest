# Chapter 3: The Gold Train

def chapter3(game_state):
    print("\nChapter 3: The Gold Train")
    print("With plans in motion, Jake and his gang prepare to intercept the gold train as it passes through a narrow canyon.")
    print("You have two options:")
    print("1. Set up an ambush to stop the train.")
    print("2. Board the train and fight the guards head-on.")

    while True:
        choice = input("What do you do? (1/2): ")

        if choice == "1":
            print("\nYou decide to set up an ambush along the canyon pass. The train approaches, and your gang springs into action!")
            print("\nDo you target the engine car to disable the train or focus on the guards in the rear cars?")
            scnd_choice = input("What do you do? (engine/guards): ").lower()
            if scnd_choice == "engine":
                print("\nYour gang disables the train by stopping the engine! The guards surrender, and the gold is yours.")
                game_state["outcome"] = "ambush_success"
                return game_state
            elif scnd_choice == "guards":
                print("\nFocusing on the guards proves to be a mistake. Reinforcements arrive, and you’re overwhelmed. GAME OVER.")
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry == "yes":
                    continue
                else:
                    exit()

        elif choice == "2":
            print("\nYou and your gang board the moving train, ready for a fight!")
            print("\nDo you charge straight for the gold car or try to eliminate the guards one by one?")
            scnd_choice = input("What do you do? (gold/guards): ").lower()
            if scnd_choice == "gold":
                print("\nYou charge straight for the gold car, but the guards overwhelm you in the confined space. GAME OVER.")
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry == "yes":
                    continue
                else:
                    exit()
            elif scnd_choice == "guards":
                print("\nEliminating the guards one by one proves effective. You secure the train and claim the gold!")
                game_state["outcome"] = "train_fight_success"
                return game_state

        else:
            print("Invalid choice. Please pick 1 or 2.")
