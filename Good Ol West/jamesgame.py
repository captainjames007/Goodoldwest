import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5


def main_game():
    print("Welcome to 'Outlaw's Last Ride'! The wild west awaits!")

    game_state = {}

    game_state = Chapter1.chapter1(game_state)

    if game_state.get("outcome") == "fight_outcome":
        print("\nYou fought your way out of Dry Creek and now head to Chapter 2: Mountain Hideout.")
        game_state = Chapter2.chapter2(game_state)
    elif game_state.get("outcome") == "sneak_outcome":
        print("\nYou managed to sneak away without a fight. Now, let's head to Chapter 2: Mountain Hideout.")
        game_state = Chapter2.chapter2(game_state)
    elif game_state.get("outcome") == "talk_outcome":
        print(
            "\nYou had a chat with the bartender, but lost precious time. Sheriff is getting closer. Let's see if you can still make it!")
        game_state = Chapter2.chapter2(game_state)

    if game_state.get("outcome") == "defend_hideout":
        print("\nYou set up the ambush and defended the hideout. Gold is yours!")
        game_state = Chapter3.chapter3(game_state)


    if game_state.get("outcome") == "ambush_outcome":
        print("\nYou successfully ambushed the sheriff’s men. On to Chapter 4: The Chase...")
        game_state = Chapter4.chapter4(game_state)

    if game_state.get("outcome") == "mountain_outcome":
        print("\nYou escaped the chase and now face the final showdown. Moving on to Chapter 5: The Final Showdown...")
        game_state = Chapter5.chapter5(game_state)

    if game_state.get("outcome") == "negotiate_outcome":
        print(
            "\nYou successfully negotiated with Sheriff Hartman and escaped with the gold. But who can trust an outlaw?")
    else:
        print("\nIt was a hard fight, but you made it. The gold’s yours, for better or worse.")


if __name__ == "__main__":
    main_game()
