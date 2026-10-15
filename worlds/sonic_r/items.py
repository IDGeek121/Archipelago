from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import SonicRWorld

ITEM_NAME_TO_ID = {
    "Progressive Resort Island Sonic Token": 1,
    "Progressive Radical City Sonic Token": 2,
    "Progressive Reactive Factory Sonic Token": 3,
    "Progressive Regal Ruin Sonic Token": 4,
    "Blue Chaos Emerald": 5,
    "Green Chaos Emerald": 6,
    "Purple Chaos Emerald": 7,
    "Yellow Chaos Emerald": 8,
    "Orange Chaos Emerald": 9,
    "Red Chaos Emerald": 10,
    "White Chaos Emerald": 11,
    "Ring": 12,
    "Sonic": 13,
    "Tails": 14,
    "Knuckles": 15,
    "Amy": 16,
    "Robotnik": 17,
    "Metal Sonic": 18,
    "Tails Doll": 19,
    "Metal Knuckles": 20,
    "Egg Robo": 21,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Progressive Resort Island Sonic Token": ItemClassification.progression,
    "Progressive Radical City Sonic Token": ItemClassification.progression,
    "Progressive Regal Ruin Sonic Token": ItemClassification.progression,
    "Progressive Reactive Factory Sonic Token": ItemClassification.progression,
    "Blue Chaos Emerald": ItemClassification.progression,
    "Green Chaos Emerald": ItemClassification.progression,
    "Purple Chaos Emerald": ItemClassification.progression,
    "Yellow Chaos Emerald": ItemClassification.progression,
    "Orange Chaos Emerald": ItemClassification.progression,
    "Red Chaos Emerald": ItemClassification.progression,
    "White Chaos Emerald": ItemClassification.progression,
    "Ring": ItemClassification.filler,
    "Sonic": ItemClassification.progression,
    "Tails": ItemClassification.useful,
    "Knuckles": ItemClassification.useful,
    "Amy": ItemClassification.useful,
    "Robotnik": ItemClassification.useful,
    "Metal Sonic": ItemClassification.useful,
    "Tails Doll": ItemClassification.useful,
    "Metal Knuckles": ItemClassification.useful,
    "Egg Robo": ItemClassification.useful,
}

class SonicRItem(Item):
    game = "SonicR"

def get_random_filler_item_name(world: SonicRWorld) -> str:
    return "Ring"


def create_item_with_correct_classification(world: SonicRWorld, name: str) -> SonicRItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return SonicRItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: SonicRWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Progressive Resort Island Sonic Token"),
        world.create_item("Progressive Resort Island Sonic Token"),
        world.create_item("Progressive Resort Island Sonic Token"),
        world.create_item("Progressive Resort Island Sonic Token"),
        world.create_item("Progressive Resort Island Sonic Token"),
        world.create_item("Progressive Radical City Sonic Token"),
        world.create_item("Progressive Radical City Sonic Token"),
        world.create_item("Progressive Radical City Sonic Token"),
        world.create_item("Progressive Radical City Sonic Token"),
        world.create_item("Progressive Radical City Sonic Token"),
        world.create_item("Progressive Regal Ruin Sonic Token"),
        world.create_item("Progressive Regal Ruin Sonic Token"),
        world.create_item("Progressive Regal Ruin Sonic Token"),
        world.create_item("Progressive Regal Ruin Sonic Token"),
        world.create_item("Progressive Regal Ruin Sonic Token"),
        world.create_item("Progressive Reactive Factory Sonic Token"),
        world.create_item("Progressive Reactive Factory Sonic Token"),
        world.create_item("Progressive Reactive Factory Sonic Token"),
        world.create_item("Progressive Reactive Factory Sonic Token"),
        world.create_item("Progressive Reactive Factory Sonic Token"),
        world.create_item("Blue Chaos Emerald"),
        world.create_item("Green Chaos Emerald"),
        world.create_item("Purple Chaos Emerald"),
        world.create_item("Yellow Chaos Emerald"),
        world.create_item("Orange Chaos Emerald"),
        world.create_item("Red Chaos Emerald"),
        world.create_item("White Chaos Emerald"),
    ]

    characters: list[Item] = [
        world.create_item("Sonic"),
        world.create_item("Tails"),
        world.create_item("Knuckles"),
        world.create_item("Amy"),
        world.create_item("Robotnik"),
        world.create_item("Metal Sonic"),
        world.create_item("Tails Doll"),
        world.create_item("Metal Knuckles"),
        world.create_item("Egg Robo"),
    ]

    # For determining the starting character
    starting_character_index = world.random.randint(0, 8)
    world.push_precollected(characters[starting_character_index])
    del characters[starting_character_index]
    itempool += characters

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
