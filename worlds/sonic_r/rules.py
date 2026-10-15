from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import SonicRWorld


def set_all_rules(world: SonicRWorld) -> None:
    set_all_entrance_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: SonicRWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    resort_island_challenge_race_entrance = world.get_entrance("Resort Island to Resort Island Challenge Race")
    radical_city_challenge_race_entrance = world.get_entrance("Radical City to Radical City Challenge Race")
    reactive_factory_challenge_race_entrance = world.get_entrance("Reactive Factory to Reactive Factory Challenge Race")
    regal_ruin_challenge_race_entrance = world.get_entrance("Regal Ruin to Regal Ruin Challenge Race")

    world.set_rule(resort_island_challenge_race_entrance, Has("Progressive Resort Island Sonic Token", count=5))
    world.set_rule(radical_city_challenge_race_entrance, Has("Progressive Radical City Sonic Token", count=5))
    world.set_rule(reactive_factory_challenge_race_entrance, Has("Progressive Reactive Factory Sonic Token", count=5))
    world.set_rule(regal_ruin_challenge_race_entrance, Has("Progressive Regal Ruin Sonic Token", count=5))

def set_completion_condition(world: APQuestWorld) -> None:
    world.set_completion_rule(HasAll(
        "Blue Chaos Emerald",
        "Green Chaos Emerald",
        "Purple Chaos Emerald",
        "Yellow Chaos Emerald",
        "Orange Chaos Emerald",
        "Red Chaos Emerald",
        "White Chaos Emerald",
        "Sonic"
        ))
