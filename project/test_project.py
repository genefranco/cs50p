from project import skill_check
from classes import Progress, Player, Investigator


def test_skill_check():
    rng = [1, 0, -1, -1, -1, -2, -3, -4]
    assert skill_check() in rng


def test_investigation_phase():
    progress = Progress(3, 2, 1, 0)
    assert progress.actions_left == 3
    assert progress.shroud == 2
    assert progress.clues == 1
    assert progress.agenda_count == 0


def test_player_hand_initialization():
    player = Player()
    assert player.show_hand() == None


def test_investigator_attributes_initialization():
    character = Investigator("Placeholder", 1, 2, 3, 4, 5)
    assert character.name == "Placeholder"
    assert character.health == 1
    assert character.sanity == 2
    assert character.willpower == 3
    assert character.intellect == 4
    assert character.agility == 5
