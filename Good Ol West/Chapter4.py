# Chapter 4: The Chase

def chapter4(game_state):
    print("Chapter 4: The Chase")
    print("With the gold in hand, Jake's crew tries to escape, but the sheriff isn’t far behind.")

    choice = input("Do you want to (A) Cross the dangerous mountains, or (B) Head across the open desert? ").lower()

    if choice == "a":
        print("You cross the mountains, gaining some distance but losing gang members to exhaustion.")
        gang_loss = input("Do you want to (1) Push through the final stretch, or (2) Rest and recover? ").lower()

        if gang_loss == "1":
            print("You push through, but several of your gang members fall behind. The sheriff catches up! GAME OVER.")
            retry = input("Do you want to try again? (yes/no): ").lower()
            if retry == "yes":
                return chapter4(game_state)
            else:
                exit()
        elif gang_loss == "2":
            print("You rest for a while, and the sheriff's men pass you. You manage to escape into the wilderness!")
            game_state["outcome"] = "mountain_outcome"
        else:
            print("Invalid choice! Pick '1' or '2'.")
            return chapter4(game_state)

    elif choice == "b":
        print("You head across the desert, but it's a tough journey. The sheriff’s men are relentless.")
        desert_dicision = input("Do you want to (1) Take a shortcut through the canyon, or (2) Keep to the main trail? ").lower()

        if desert_dicision == "1":
            print("The canyon is too treacherous! You lose your way and the sheriff catches up. GAME OVER.")
            retry = input("Do you want to try again? (yes/no): ").lower()
            if retry == "yes":
                return chapter4(game_state)
            else:
                exit()
        elif desert_dicision == "2":
            print("The main trail is long, but you make it through, managing to shake off the sheriff's men!")
            game_state["outcome"] = "desert_outcome"
        else:
            print("Invalid choice! Pick '1' or '2'.")
            return chapter4(game_state)

    else:
        print("Invalid choice! Pick 'A' or 'B'.")
        return chapter4(game_state)

    if game_state["outcome"] == "mountain_outcome":
        print("You managed to escape through the mountains, but not without losses. The sheriff is still on your tail!")
    elif game_state["outcome"] == "desert_outcome":
        print("The desert is unforgiving, but you manage to shake off the sheriff's men. You're almost free!")

    return game_state

