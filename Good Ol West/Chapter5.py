# Chapter 5: The Final Showdown

def chapter5(game_state):
    print("Chapter 5: The Final Showdown")
    print("Jake and Sheriff Hartman meet face-to-face in a Western standoff. This is the final test.")

    choice = input("Do you want to (A) Negotitate with Hartman or (B) Fight Hartman? ").lower()  # typo in 'Negotitate'

    if choice == "a":
        print(
            "You try to negotiate with Hartman. If you’ve been good to your gang, he might strike a deal. Otherwise, he’ll just shoot you.")  # typo in 'negotiat'
        gang_loyalty = input("Do you think your gang is loyal enough to vouch for you? (yes/no): ").lower()

        if gang_loyalty == "yes":
            print("Your gang backs you up, and Hartman agrees to a deal. You escape alive, but the gold is lost.")
            game_state["outcome"] = "negotiate_success"
        elif gang_loyalty == "no":
            print("Hartman doesn’t trust you. He shoots you down in cold blood. GAME OVER.")
            retry = input("Do you want to try again? (yes/no): ").lower()
            if retry == "yes":
                return chapter5(game_state)
            else:
                exit()
        else:
            print("Invalid choice! Pick 'yes' or 'no'.")
            return chapter5(game_state)

    elif choice == "b":
        print("It’s a standoff. You draw your weapon and fight, but who will be left standing?")
        fight_result = input("Do you want to (1) Shoot first or (2) Wait for Hartman to make the first move? ").lower()

        if fight_result == "1":
            print("You shoot first, but Hartman is faster. He hits you. GAME OVER.")
            retry = input("Do you want to try again? (yes/no): ").lower()
            if retry == "yes":
                return chapter5(game_state)
            else:
                exit()
        elif fight_result == "2":
            print("You wait for Hartman to draw, and you’re quicker. You win the standoff!")
            game_state["outcome"] = "fight_success"
        else:
            print("Invalid choice! Pick '1' or '2'.")
            return chapter5(game_state)

    else:
        print("Invalid choice! Pick 'A' or 'B'.")
        return chapter5(game_state)  # Retry if input is invalid

    return game_state

