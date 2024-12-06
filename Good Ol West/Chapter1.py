# Chapter 1: Escape from Dry Creek

def chapter1(game_state):
    print("\nChapter 1: Escape from Dry Creek")
    print("You’re an outlaw cornered in the town of Dry Creek. The sheriff’s men are closing in.")
    print("You have three options:")
    print("1. Fight your way out.")
    print("2. Sneak out through the back alleys.")
    print("3. Talk to the bartender and gather information.")

    while True:
        choice = input("What do you do? (1/2/3): ")

        if choice == "1":
            print("\nYou draw your revolver and face the sheriff’s men head-on!")
            print("\nThe fight is intense. Bullets fly everywhere. Do you aim for the sheriff’s deputy or dive for cover?")
            sub_choice = input("What do you do? (aim/dive): ").lower()
            if sub_choice == "aim":
                print("\nYour shot hits true! The deputy falls, and the others retreat momentarily.")
                game_state["outcome"] = "fight_outcome"
                return game_state
            elif sub_choice == "dive":
                print("\nYou dive for cover but are cornered. The sheriff’s men overwhelm you. GAME OVER.")
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry == "yes":
                    continue
                else:
                    print("Closing the game...")
                    return

        elif choice == "2":
            print("\nYou slip into the shadows, navigating the back alleys of Dry Creek.")
            print("\nYou move cautiously through the alleys. Suddenly, you hear footsteps. Do you hide in a barrel or climb onto a roof?")
            sub_choice = input("What do you do? (hide/climb): ").lower()
            if sub_choice == "hide":
                print("\nYou hide in a barrel, holding your breath as the deputies pass. It works!")
                game_state["outcome"] = "sneak_outcome"
                return game_state
            elif sub_choice == "climb":
                print("\nYou try to climb, but the creaky wood gives you away. The deputies catch you. GAME OVER.")
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry == "yes":
                    continue
                else:
                    print("Closing the game...")
                    return

        elif choice == "3":
            print("\nYou approach the bartender, hoping he can help you.")
            print("\nThe bartender eyes you warily. Do you offer him gold or threten him for information?")
            sub_choice = input("What do you do? (gold/threten): ").lower()
            if sub_choice == "gold":
                print("\nThe bartender accepts your gold and tells you about a secret tunnel. You escape just in time!")
                game_state["outcome"] = "talk_outcome"
                return game_state
            elif sub_choice == "threten":
                print("\nThe bartender refuses to cooperate, and you waste too much time. The sheriff’s men arrive. GAME OVER.")
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry == "yes":
                    continue
                else:
                    print("Closing the game...")
                    return

        else:
            print("Invalid choice. Please pick 1, 2, or 3.")
