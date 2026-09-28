from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import SonicRWorld


def create_and_connect_regions(world: SonicRWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: SonicRWorld) -> None:
    menu                            = Region("Menu", world.player, world.multiworld)
    resort_island                   = Region("Resort Island", world.player, world.multiworld)
    resort_island_challenge_race    = Region("Resort Island Challenge Race", world.player, world.multiworld)
    radical_city                    = Region("Radical City", world.player, world.multiworld)
    radical_city_challenge_race     = Region("Radical City Challenge Race", world.player, world.multiworld)
    reactive_factory                = Region("Reactive Factory", world.player, world.multiworld)
    reactive_factory_challenge_race = Region("Reactive Factory Challenge Race", world.player, world.multiworld)
    regal_ruin                      = Region("Regal Ruin", world.player, world.multiworld)
    regal_ruin_challenge_race       = Region("Regal Ruin Challenge Race", world.player, world.multiworld)
    radiant_emerald                 = Region("Radiant Emerald", world.player, world.multiworld)

    regions = [
        menu,
        resort_island,
        resort_island_challenge_race,
        radical_city,
        radical_city_challenge_race,
        reactive_factory,
        reactive_factory_challenge_race,
        regal_ruin,
        regal_ruin_challenge_race,
        radiant_emerald,
    ]
    world.multiworld.regions += regions


def connect_regions(world: SonicRWorld) -> None:
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

    menu.connect(resort_island, "Menu to Resort Island")
    resort_island.connect(resort_island_challenge_race, "Resort Island to Resort Island Challenge Race")
    menu.connect(radical_city, "Menu to Radical City")
    radical_city.connect(radical_city_challenge_race,  "Radical City to Radical City Challenge Race")
    menu.connect(reactive_factory, "Menu to Reactive Factory")
    reactive_factory.connect(reactive_factory_challenge_race, "Reactive Factory to Reactive Factory Challenge Race")
    menu.connect(regal_ruin, "Menu to Regal Ruin")
    regal_ruin.connect(regal_ruin_challenge_race, "Regal Ruin to Regal Ruin Challenge Race")
    menu.connect(radiant_emerald, "Menu to Radiant Emerald")
