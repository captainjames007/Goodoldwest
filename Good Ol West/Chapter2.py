# Chapter 2: Mountain Hideout

def chapter2(game_state):
    print("\nChapter 2: Mountain Hideout")
    print("After escaping Dry Creek, you and your gang retreat to a hidden mountain hideout to plan your next move.")
    print("You have two options:")
    print("1. Stay and defend the hideout.")
    print("2. Leave early to prepare for the train heist.")

    while True:
        choice = input("What do you do? (1/2): ")

        if choice == "1":
            print("\nYou decide to stay and fortify the hideout. Sheriff’s men are closing in fast!")
            print("\nDo you set up traps around the hideout or prepare an ambush inside?")
            sub_choice = input("What do you do? (traps/ambush): ").lower()
            if sub_choice == "traps":
                print("\nYour traps work perfectly! The sheriff’s men are caught off guard, and you fend them off successfully.")
                game_state["outcome"] = "defend_hideout"
                return game_state
            elif sub_choice == "ambush":
                print("\nYour ambush plan fails when the sheriff’s men arrive with more reinforcements than expected. GAME OVER.")
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry == "yes":
                    continue
                else:
                    exit()

        elif choice == "2":
            print("\nYou leave early to prepare for the train heist, but you lose valuable time for planning.")
            print("\nOn the way, you encounter a lone deputy. Do you confront him or avoid him?")
            sub_choice = input("What do you do? (confront/avoid): ").lower()
            if sub_choice == "confront":
                print("\nYou confront the deputy and manage to take him out, but the noise alerts nearby patrols. You barely escape.")
                game_state["outcome"] = "early_departure"
                return game_state
            elif sub_choice == "avoid":
                print("\nYou avoid the deputy, but in doing so, you lose your way and end up delayed. GAME OVER.")
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry == "yes":
                    continue
                else:
                    exit()

        else:
            print("Invalid choice. Please pick 1 or 2.")

