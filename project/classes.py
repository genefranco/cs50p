import random


# Show changes in set parameters after input actions
class Progress:
    def __init__(self, actions_left, shroud, clues, agenda_count):
        self.actions_left = actions_left
        self.shroud = shroud
        self.clues = clues
        self.agenda_count = agenda_count

    def show_progress(self):
        print(f"Actions left: {self.actions_left}")
        print(f"Shroud level: {self.shroud}")
        print(f"Clues: {self.clues}")
        print(f"Agenda: {self.agenda_count}")


class Card:
    def __init__(self, name):
        self.name = name


class Investigator(Card):
    def __init__(self, name, health, sanity, willpower, intellect, agility):
        super().__init__(name)
        self.health = health
        self.sanity = sanity
        self.willpower = willpower
        self.intellect = intellect
        self.agility = agility

    # Show change in character statistics when changes are made
    def show_stats(self):
        print(f"Health: {self.health}, Sanity: {self.sanity}")
        print(
        f"Willpower: {self.willpower}, Intellect: {self.intellect}, Agility: {self.agility}"
        )


class Asset(Card):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def __repr__(self):
        return f"{self.name}"

    def get_value(self):
        return int(self.value)


# Cards to be used to alter character intellect parameters
class Deck(Card):
    def __init__(self, name):
        super().__init__(name)
        self.cards = [
            Asset("Magnifying Glass", 1),
            Asset("Magnifying Glass", 1),
            Asset("Magnifying Glass", 1),
            Asset("Flashlight", 2),
            Asset("Flashlight", 2),
            Asset("Encyclopedia", 3),
        ]
        self.shuffle()

    # Shuffle list for random draws
    def shuffle(self):
        random.shuffle(self.cards)

    # Draw from the top of the deck
    def draw_card(self):
        card = self.cards.pop()
        return card

    # Return card to the bottom of the deck
    def return_card(self, card):
        self.cards.insert(0, card)


class Player:
    def __init__(self):
        self.hand = []

    def draw_card(self, deck):
        card = deck.draw_card()
        self.hand.append(card)
        return card

    # Call return_card function when card is used
    def return_card_to_deck(self, deck, card):
        self.hand.remove(card)
        deck.return_card(card)

    def show_hand(self):
        print([card.name for card in self.hand])