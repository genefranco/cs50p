import sys
import time
import random
from classes import Player, Investigator, Deck, Progress

# Start Up Screen
def main():
    welcome = "Welcome to the Text-Based Arkham Horror Card Game\n"
    for char in welcome:
        print(char, end="", flush=True)
        time.sleep(0.05)

    while True:
        try:
            print("[Please type capitalized words to continue when prompted.]")
            user_input = (
                input("Type 'START' to begin or 'EXIT' to leave:\n").lower().strip()
            )
            if user_input == "start":
                print("=" * 20)
                print("Trapped in the Study")
                print("=" * 20)
                scenario_0 = (
                    "As you walk thru the door to begin your investigation,\n"
                    "the door suddenly vanishes leaving nothing but a solid wall...\n"
                    "You must 'INVESTIGATE' the area to find yourself another exit.\n"
                )

                for char in scenario_0:
                    print(char, end="", flush=True)
                    time.sleep(0.04)

                # Game Flow Instructions
                print("=" * 69)
                print(
                    "Input Instructions:\n"
                    "------------------\n"
                    "During input prompt, actions you may use include:\n"
                    "'INVESTIGATE'\n'DRAW'\n'USE'\n"
                    "Input is case insensitive"
                )

                investigation_phase()
            elif user_input == "exit":
                sys.exit("Good Bye!")
            else:
                pass
        except KeyboardInterrupt:
            sys.exit()


# Gameplay Loop
def investigation_phase():
    print("=" * 69)  # Nice...
    player = Player()
    character = Investigator("Ms Baker", 6, 8, 5, 2, 3)
    deck = Deck("My Deck")
    progress = Progress(3, 2, 0, 3)
    progress.show_progress()
    character.show_stats()
    player.show_hand()
    while progress.actions_left > 0 and progress.agenda_count != 0:
        invest_original = character.intellect + skill_check()
        invest_check = invest_original
        print("=" * 69)
        action = (
            input("Will you 'INVESTIGATE', 'DRAW' a card, or 'USE' an asset? ")
            .lower()
            .strip()
        )
        # Action required for collecting 'clues' to advance
        if action == "investigate":
            progress.actions_left -= 1
            if invest_check >= progress.shroud:
                progress.clues += 1
                print("=" * 69)
                print("You look around the bookcase and find a clue!")
                print("=" * 69)
                progress.show_progress()
            else:
                # Player loses 1 sanity upon failed skill check
                character.sanity -= 1
                print("=" * 69)
                print(
                    "You flip thru some papers scattered on the desk and find nothing."
                )
                print("=" * 69)
                progress.show_progress()
        # Draws a card from the Deck class if there are remaining cards
        elif action == "draw":
            progress.actions_left -= 1
            draw_check = character.willpower + skill_check()
            if len(deck.cards) == 0:
                print("There are no more cards left in the deck.")
                pass
            elif len(player.hand) == 5:
                print("Your hand is full, please use a card before drawing a new card")
            elif draw_check >= progress.shroud:
                drawn_card = player.draw_card(deck)
                print("=" * 69)
                print(f"You drew a '{drawn_card.name}.'")
                progress.show_progress()
                player.show_hand()
            else:
                print("=" * 69)
                print("You failed to draw a card...")
                progress.show_progress()
        # Use a card in your hand if available
        elif action == "use":
            player.show_hand()
            if len(player.hand) == 0:
                print("You have no cards in hand to use...")
                pass
            else:
                progress.actions_left -= 1
                card_name = input("Which card would you like to use? ").strip().lower()
                card_found = False
                for card in player.hand:
                    if card_name == card.name.lower():
                        card_found = True
                        print(f"You used the '{card_name}.'")
                        print("=" * 69)
                        character.intellect += card.value
                        player.return_card_to_deck(deck, card)
                        progress.show_progress()
                        character.show_stats()
                        player.show_hand()
                if not card_found:
                    print("Card not found in hand")
                    pass
        if progress.clues >= 3:
            room_cleared()
            break
        if progress.actions_left == 0 and progress.agenda_count > 0:
            agenda_check = character.agility + skill_check()
            if agenda_check > progress.shroud:
                progress.actions_left = 3
                print("=" * 69)
                print(
                    "You quickly notice falling ceiling debris and safely move aside."
                )
                print("=" * 69)
                progress.show_progress()
                character.show_stats()
            else:
                progress.agenda_count -= 1
                progress.actions_left = 3
                character.health -= 1
                character.sanity -= 1
                print("=" * 69)
                print("A rat runs past your feet. Startled, you fall and take damage.")
                print("=" * 69)
                progress.show_progress()
                character.show_stats()
        if character.health == 0 or character.sanity == 0:
            agenda()
    else:
        agenda()


# Adds a random element to input actions
def skill_check():
    rng = [1, 0, -1, -1, -1, -2, -3, -4]
    return random.choice(rng)


# Flavour text for successfully collecting enough clues
def room_cleared():
    print("=" *69)
    scenario_0_end = (
        "You notice edges of your recently purchased rug has become tattered\n"
        "and mud-stained. Curious, you pull the rug back revealing the exit\n"
        "you've been long searching for. As you slowly turning the knob, the\n"
        "door swings open leading to the hallways...\n"
        "Do you jump down or stay in the study?\n"
    )

    for char in scenario_0_end:
        print(char, end="", flush=True)
        time.sleep(0.04)

    crossroad = input("'JUMP' or 'STAY'?: \n")
    if crossroad.lower() == "jump":
        print("=" *69)
        jump = (
            "You jump through the doorway, landing your feet on soft dirt.\n"
            "The door to the study slams shut above you. The smell of\n"
            "burning wood smothers the narrow hall, intermingled with \n"
            "the rot and decay. You find yourself out of one predicament\n"
            "and into another. Unfortunately, your story ends here."
        )
        for char in jump:
            print(char, end="", flush=True)
            time.sleep(0.04)
            break

        tbc = "Story to be continued."
        for char in tbc:
            print(char, end="", flush=True)
            time.sleep(0.05)
            break

    elif crossroad == "stay":
        agenda()


# Flavour text for failing to escape the study
def agenda():
    agenda0 = (
        "\nWhat's Going On?!\n"
        "It is late at night.  You are holed up in your study,\n"
        "researching the bloody disappearances that have been\n"
        "taking place in the region. A few hours into your research\n"
        "you hear the sound of strange chanting coming from your\n"
        "parlor down the hall. At the same time, you hear dirt\n"
        "churning, as if something were digging beneath the floor.\n\n"
        "Your house continues to change before your very eyes. The\n"
        "walls have decayed, and the ground in many rooms has turned\n"
        "to dirt. It is almost as if you have been trasported\n"
        "somewhere else entirely, although every now and again you\n"
        "recognize elements of your former home.\n"
    )

    for char in agenda0:
        print(char, end="", flush=True)
        time.sleep(0.04)
    sys.exit("Scenario Failed")


if __name__ == "__main__":
    main()
