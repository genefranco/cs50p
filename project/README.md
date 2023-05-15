# TEXT-BASED ARKHAM HORROR CARD GAME
#### Video Demo: <URL HERE>
    INCLUDE: Title, Name, City, Country.
    Create a short video (<= 3 mins) in which you present your project, as with slides,
    screenshots, voiceover, and/or live action. You may upload to youtube as unlisted.
#### Description:
This project is a text-based card game based off the *H.P. Lovecraft's Cthulu Mythos.* and
contains some ideas from Fantasy Flight's *Arkham Horror Living Card Game.<sup>[1]</sup>
The content in reference in the first scenario found in *The Gathering* set from the game.
Dialogue in this game flush out a string that is printed with a delay. This is something that
is most commonly seen in video games where text is being printed out in a dialogue box. The game
relies on input from the user to execute functions within the game to advance. The user will
have a character with predefined statistic values that will be checked against a constant
during certain actions. More information on this will be available in the "Random Number
Generated Skill Check System" section below. The flow of the game relies on the user to obtain
enough *"clues"* thru using the **"Investigate"** input prompt. If enough *clues* are collected
before the *"Agenda"* reaches 3, you would move onto the next scenario (Not included in this
project as this serves as more of a proof of concept). If the *"Agenda"* count equals 3, you
will be met with *"Failed Scenario"* dialogue.
You have the option to **"Draw"** a card in this game. These cards' function can be executed
using the **Use"** prompt, where your *"Intellect"* parameter will be increased by a set value
based on the value of the card that was used. This allows you to investigate more effectively.
#### In-game Dialogue
As what's commonly seen in video games, dialogue is often displayed as text that is flushed
out in varying speeds. The speed of this text display, outputs characters one at a time, can
often be toggled in the options menu depending on the player's preferences. For the purpose of
this project, I have chosen a speed at which is most comfortable with my speed of reading text.
The code in question looks like this: <sup>[2][3]</sup>
```
dialogue_variable = "dialogue here"
print(dialogue variable, end="", flush=True)
time.sleep(0.04)
```
#### Game Flow
After opting to "start" the game, you will be met with the opening dialogue lining the state of
your current situation. You are presented with the instruction to input promts that are shown as
capitalized words. These are the only inputs that will affect change.
They include **INVESTIGATE**, **DRAW**, and **USE**.

1. **INVESTIGATE** - This will check your *Intellect* value added with the result of *skill_check()*
    against the shroud value. If the value is greater than or equal to the shroud value, you gain a
    clue. Otherwise, lose a point of sanity. Collecting 3 clues will move you to a "positive" outcome.
    Cards can be used to increase the value of your intellect to improve your chance of finding a clue.

```
invest_original = character.intellect + skill_check()
invest_check = invest_orginal
```

2. **DRAW** - This will draw from a deck that is shuffled so that the order of which the cards can be
    drawn will differ throughout each playthrough. The Deck contains the following cards:
    +*Magnifying Glass* - Raises your intellect value by 1.
    +*Flashlight* - Raises your intellect value by 2.
    +*Encyclopedia* - Raises your intellect value by 3.

3. **USE** - If there are cards in your hand, you will be prompt to type in the name of the card. The
    value associated with the card will then be added to your intellect allowing for more succesful
    investigations.
#### Random Number Generated Skill Check System
The game contains variables that will execute differenct functions based on the integer it contains.
The number values that will be used to alter the overall value of your "skill checks" are contained
within a list. This list is shown below:

```
def skill_check():
    # Standard difficulty
    standard = [1, 0, -1, -1, -1, -2, -2, -3, -4]
    return random.choice(standard)
```

The "skill_check" function will be used with the following actions during the
phase with which you are prompt to input actions to affect change.
1.  If you input *"investigate"* in order to gather a clue, *invest_check* is
    the variable which is the sum of your intellect value and the value generated
    from the *skill_check* function. This will be compared with the shroud value.
```
    if action == "investigate":
        progress.actions_left -= 1
        if invest_check >= progress.shroud:
        ...
```
2.  If you input *"draw"* in order to draw a card from the deck, *"draw_check"*
    is the variable which is the sum of your willpower value and the value
    generated from the *skill_check* function. This will be compared with shroud.
```
    elif action == "draw":
        progress.actions_left -= 1
        draw_check = character.willpower + skill_check()
        elif draw_check >= progress.shroud:
        ...
```
3.  When the variable *actions_left* reaches 0 while your *agenda_count*
    is still above 0, your actions will reset, starting you on your next
    turn. Your agility parameter will be summed up with the value recieved
    from the *skill_check* function and compared to the value of shroud.
    If successful, your next turn will start with no change in character
    parameters. Otherwise, the your agenda count, health, and sanity will
    be reduced by a value of 1.

```
    if progress.actions_left == 0 and progress.agenda_count > 0:
        agenda_checkt = character.agility + skill_check()
        if agenda_check > progress.shroud:
            progress.actions_left = 3
            ...
        else:
            progress.agenda_count -= 1
            progress.actions_left = 3
            character.health -= 1
            character.sanity -= 1
            ...
```
#### Flavour Text
The Scenario of the game will take place similarly as does the card game.
For the purpose of this demonstration, only the very first scenario is used.
*Scenario reference from Arkham's Living Card Game: Stage 1, "Trapped"*<sup>[4]</sup>
The Agenda is in reference to the agenda of the Antagonistic characters of the story. [86]
For the purpose of this demonstration, only the first agenda is referenced.
*Agenda reference from Arkham's Living Card Game: Agenda 1a, "What's Going On?!"*<sup>[5]</sup>

#### Separation of Classes from project.py:
Classes with functions used within the project have been placed in a separate
python file *"classes"* to be called by project.py. For the purpose of organization,
"Classes" have been kept in a separate file so that I may come back to look at
the code for debugging and editing purposes without the need to search the main
project file. I also want to avoid unnecessarily clutter in the main project file.

#### Remaining classes and their respective functions:
```
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
```

**"actions_left"**
-This is the amount of actions (text inputs) given to the player before the "agenda" function is executed.
**"shroud"**
-The constant value that is compared to the player's character's intelligence to investigate for clues.
-Values include the integer given from the list included within the "skill_check" function "standard."
**"clues"**
-Given to player if they pass a skill check after the "Investigation" input.
-"room_cleared" function will be executed should the clue variable value reach a threshold of x.
**"agenda_count"**
-Count for agenda_counter goes up when all the actions of the player is exhausted for the turn.
-When the 'actions_left" count is exhausted, the "agenda" function will be executed.

```
class Card:
    def __init__(self, name):
        self.name = name


class Investigator(Card):
    def __init__(self, name, health, sanity, willpower, intellect, combat, agility):
        super().__init__(name)
        self.health = health
        self.sanity = sanity
        self.willpower = willpower
        self.intellect = intellect
        self.combat = combat
        self.agility = agility

    def show_stats(self):
        print(f"Health: {self.health}, Sanity: {self.sanity}")
        print(
        f"Willpower: {self.willpower}, Intellect: {self.intellect}, Combat: {self.combat}, Agility: {self.agility}"
        )


class Asset(Card):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def __repr__(self):
        return f"{self.name}"

    def value(self):
        return int(self.value)


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

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        card = self.cards.pop()
        return card

    def return_card(self, card):
        self.cards.append(card)
```
The *"Card"* class and it's respective subclasses represent the cards
that may have otherwise been used in the physical game (value has
been changed for the purpose of this game.) The deck class handles
the *"Asset"* cards within its deck. The cards are created within the
*"Deck"* class and contain functions that are involved with the
dispensing of drawn cards with the *"drawn_card(self)"* fucntion and
receiving of used cards with the *"return_card(self, card)"* function.
The *"Deck"* class also contains a *"shuffle(self)"* functions so the
cards can be drawn without predictability with each playthrough.

```
class Player:
    def __init__(self):
        self.hand = []

    def draw_card(self, deck):
        card = deck.draw_card()
        self.hand.append(card)
        return card

    def return_card_to_deck(self, deck, card):
        self.hand.remove(card)
        deck.return_card(card)

    def show_hand(self):
        print([card.name for card in self.hand])
```
This class functions the handling of the cards with regards to the
player's use of the cards. Held in a list when drawn and returned
to the bottom of the deck when used with the *"use"* input prompt.


[^1]: https://www.fantasyflightgames.com/en/products/arkham-horror-the-card-game/
[^2]: https://www.includehelp.com/python/flush-parameter-in-python-with-print-function.aspx#:~:text=flush%20parameter%20is%20used%20to,%22True%22%20%E2%80%93%20stream%20flushes.
[^3]: https://realpython.com/python-sleep/
[^4]: https://arkhamdb.com/card/01108
[^5]: https://arkhamdb.com/card/01105

MARKDOWN URL
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
