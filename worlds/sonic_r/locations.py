from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import SonicRWorld

LOCATION_NAME_TO_ID = {
    "Resort Island Sonic Token 1": 1,
    "Resort Island Sonic Token 2": 2,
    "Resort Island Sonic Token 3": 3,
    "Resort Island Sonic Token 4": 4,
    "Resort Island Sonic Token 5": 5,
    "Radical City Sonic Token 1": 6,
    "Radical City Sonic Token 2": 7,
    "Radical City Sonic Token 3": 8,
    "Radical City Sonic Token 4": 9,
    "Radical City Sonic Token 5": 10,
    "Reactive Factory Sonic Token 1": 11,
    "Reactive Factory Sonic Token 2": 12,
    "Reactive Factory Sonic Token 3": 13,
    "Reactive Factory Sonic Token 4": 14,
    "Reactive Factory Sonic Token 5": 15,
    "Regal Ruin Sonic Token 1": 16,
    "Regal Ruin Sonic Token 2": 17,
    "Regal Ruin Sonic Token 3": 18,
    "Regal Ruin Sonic Token 4": 19,
    "Regal Ruin Sonic Token 5": 20,
    "Resort Island Chaos Emerald": 21,
    "Radical City Chaos Emerald 1": 23,
    "Radical City Chaos Emerald 2": 24,
    "Reactive Factory Chaos Emerald 1": 25,
    "Reactive Factory Chaos Emerald 2": 26,
    "Regal Ruin Chaos Emerald 1": 27,
    "Regal Ruin Chaos Emerald 2": 28,
    "Resort Island Grand Prix Win": 29,
    "Radical City Grand Prix Win": 30,
    "Reactive Factory Grand Prix Win": 31,
    "Regal Ruin Grand Prix Win": 32,
    "Radiant Emerald Grand Prix Win": 33,
    "Resort Island Challenge Race Win": 34,
    "Radical City Challenge Race Win": 35,
    "Reactive Factory Challenge Race Win": 36,
    "Regal Ruin Challenge Race Win": 37,
}

class SonicRLocation(Location):
    game = "SonicR"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: SonicRWorld) -> None:
    create_regular_locations(world)


def create_regular_locations(world: SonicRWorld) -> None:
    menu                            = world.get_region("Menu")
    resort_island                   = world.get_region("Resort Island")
    resort_island_challenge_race    = world.get_region("Resort Island Challenge Race")
    radical_city                    = world.get_region("Radical City")
    radical_city_challenge_race     = world.get_region("Radical City Challenge Race")
    reactive_factory                = world.get_region("Reactive Factory")
    reactive_factory_challenge_race = world.get_region("Reactive Factory Challenge Race")
    regal_ruin                      = world.get_region("Regal Ruin")
    regal_ruin_challenge_race       = world.get_region("Regal Ruin Challenge Race")
    radiant_emerald                 = world.get_region("Radiant Emerald")

    resort_island_locations = get_location_names_with_ids([
        "Resort Island Sonic Token 1",
        "Resort Island Sonic Token 2",
        "Resort Island Sonic Token 3",
        "Resort Island Sonic Token 4",
        "Resort Island Sonic Token 5",
        "Resort Island Chaos Emerald",
        "Resort Island Grand Prix Win",
    ])
    resort_island_challenge_race_locations = get_location_names_with_ids([
        "Resort Island Challenge Race Win",
    ])
    radical_city_locations = get_location_names_with_ids([
        "Radical City Sonic Token 1",
        "Radical City Sonic Token 2",
        "Radical City Sonic Token 3",
        "Radical City Sonic Token 4",
        "Radical City Sonic Token 5",
        "Radical City Chaos Emerald 1",
        "Radical City Chaos Emerald 2",
        "Radical City Grand Prix Win",
    ])
    radical_city_challenge_race_locations = get_location_names_with_ids([
        "Radical City Challenge Race Win",
    ])
    reactive_factory_locations = get_location_names_with_ids([
        "Reactive Factory Sonic Token 1",
        "Reactive Factory Sonic Token 2",
        "Reactive Factory Sonic Token 3",
        "Reactive Factory Sonic Token 4",
        "Reactive Factory Sonic Token 5",
        "Reactive Factory Chaos Emerald 1",
        "Reactive Factory Chaos Emerald 2",
        "Reactive Factory Grand Prix Win",
    ])
    reactive_factory_challenge_race_locations = get_location_names_with_ids([
        "Reactive Factory Challenge Race Win",
    ])
    regal_ruin_locations = get_location_names_with_ids([
        "Regal Ruin Sonic Token 1",
        "Regal Ruin Sonic Token 2",
        "Regal Ruin Sonic Token 3",
        "Regal Ruin Sonic Token 4",
        "Regal Ruin Sonic Token 5",
        "Regal Ruin Chaos Emerald 1",
        "Regal Ruin Chaos Emerald 2",
        "Regal Ruin Grand Prix Win",
    ])
    regal_ruin_challenge_race_locations = get_location_names_with_ids([
        "Regal Ruin Challenge Race Win",
    ])
    radiant_emerald_locations = get_location_names_with_ids([
        "Radiant Emerald Grand Prix Win",
    ])
    resort_island.add_locations(resort_island_locations, SonicRLocation)
    resort_island_challenge_race.add_locations(resort_island_challenge_race_locations, SonicRLocation)
    radical_city.add_locations(radical_city_locations, SonicRLocation)
    radical_city_challenge_race.add_locations(radical_city_challenge_race_locations, SonicRLocation)
    reactive_factory.add_locations(reactive_factory_locations, SonicRLocation)
    reactive_factory_challenge_race.add_locations(reactive_factory_challenge_race_locations, SonicRLocation)
    regal_ruin.add_locations(regal_ruin_locations, SonicRLocation)
    regal_ruin_challenge_race.add_locations(regal_ruin_challenge_race_locations, SonicRLocation)
    radiant_emerald.add_locations(radiant_emerald_locations, SonicRLocation)
