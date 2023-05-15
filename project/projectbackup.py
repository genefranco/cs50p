import sys
import time
import random
from classes import Player, Investigator, Deck, Progress


def main():
    welcome = "Welcome to the Text-Based Arkham Horror Card Game\n"
    for char in welcome:
        print(char, end="", flush=True)
        time.sleep(0.05)

    while True:
        try:
            user_input = input("Type 'START' to begin or 'EXIT' to leave:\n").lower().strip()
            if user_input == "start":
                gamestart()
            if user_input == "exit":
               sys.exit("Good Bye!")
        except KeyboardInterrupt:
            sys.exit()


def gamestart():
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

    investigation_phase()


def investigation_phase():
    print("=" * 69)  # Nice...
    player = Player()
    character = Investigator("Ms Baker", 6, 8, 5, 2, 2, 3)
    deck = Deck("My Deck")
    progress = Progress(3,2,0,0)
    progress.show_progress()
    character.show_stats()
    player.show_hand()
    while progress.actions_left > 0 and progress.agenda_count != 3:
        invest_original = character.intellect + skill_check()
        invest_check = invest_original
        print("=" * 69)
        action = (
            input(
                "Will you 'INVESTIGATE', 'DRAW' a card, or 'USE' an asset?"
                ).lower().strip()
        )
        if action == "investigate":
            progress.actions_left -= 1
            if invest_check >= progress.shroud:
                progress.clues += 1
                print("You look around the bookcase and find a clue!")
                progress.show_progress()
            else:
                # Player loses 1 sanity upon failed skill check
                character.sanity -= 1
                print("You flip thru some papers scattered on the desk and find nothing.")
                progress.show_progress()
        # Draws a card from the Deck class if there are remaining cards
        elif action == "draw":
            progress.actions_left -= 1
            if len(deck.cards) == 0:
                print("There are no more cards left in the deck.")
                pass
            elif len(player.hand) == 5:
                print("Your hand is full, please use a card before drawing a new card"
            else:
                drawn_card = player.draw_card(deck)
                print("=" * 69)
                print(f"You drew a '{drawn_card.name}.'")
                progress.show_progress()
                player.show_hand()
        # Use a card in your hand if available
        elif action == "use":
            if len(player.hand) == 0:
                print("You have no cards in hand to use...")
                pass
            else:
                progress.actions_left -= 1
                card_name = input("Which card would you like to use? ").strip()
                card_found = False
                for card in player.hand:
                    if card.name.lower() == card_name.lower():
                        print(f"You used the '{card_name}.'")
                        character.intellect += card.value
                        player.return_card_to_deck(deck, card)
                        card_found = True
                        progress.show_progress()
                        character.show_stats()
                        player.show_hand()
                if not card_found:
                    print("Card not found in hand")
        if progress.clues >= 3:
            room_cleared()
            break
        if progress.actions_left == 0 and progress.agenda_count != 3:
            progress.agenda_count += 1
            progress.actions_left = 3
            character.health -= 1
            character.sanity -= 1
            print("=" * 69)
            print("You take pause as you hear a thud outside the room...")
            progress.show_progress()
    else:
        agenda()


def skill_check():
    # Standard difficulty
    standard = [1, 0, -1, -1, -1, -2, -2, -3, -4]
    return random.choice(standard)


def room_cleared():
    scenario_0_end = (
        "You notice edges of your recently purchased rug has become\n"
        "tattered and mud-stained. Curious, you pull the rug back\n"
        "revealing an exit you've been long searching for.\n"
        "Slowly turning the knob, the door swings open leading to\n"
        "your hallways. Do you jump down or stay in the study?\n"
    )

    for char in scenario_0_end:
        print(char, end="", flush=True)
        time.sleep(0.04)

    crossroad = input("'Jump' or 'Stay': ")
    if crossroad.lower() == "jump":
        jump = (
            "You jump through the doorway, landing on your feet on soft\n"
            "dirt. The door to the study slams shut above you. The smell\n"
            "of burning wood fills the narrow hall, intermingled with \n"
            "the scent of rot and decay.\n"
        )
        for char in jump:
            print(char, end="", flush=True)
            time.sleep(0.04)

    elif crossroad == "stay":
        agenda()

# Change into a class
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
