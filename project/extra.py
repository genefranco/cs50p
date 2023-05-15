'''
# Game Flow
def round_sequence():
    print("Round sequence goes as follows:")
    # Player action phase
    print("1) Investigation Phase")
    # Enemy, if present, re-engages if disengaged or attacks
    print("2) Enemy Phase")
    # Draw a card and gain a resource
    print("3) Upkeep Phase")
    # Mythos countdown
    print("4) Mythose Phase")


class Monster(Card):
    def __init__(self, name, description, attack, health)
        super().__init__(name, description)
        self.attack = attack
        self.health = health

    def attack(self, target):
        # execute attack on target
        pass

class Item(Card):
    def __init__(self, name, description, effects):
        super()__init__(name, description)
        self.effects = effects

    def use(self, targets):
        # execute item effects on target
        pass


def mythos_phase():
    spawn_rate = random.randrange(3)
    if spawn_rate == 0:
        battle()
    else:
        false_alarm = ("You hear a thud outside... but nothing happens\n")
        for _ in false_alarm:
            sys.stdout.write(_)
            sys.stdout.flush()
            time.sleep(0.07)
        investigate()


Put into play 'Hallway', 'Cellar', 'Attic', and 'Parlor'
Discard each enemy in the Study.
Place Investigator in the Hallway
Remove the Study from the game

'''