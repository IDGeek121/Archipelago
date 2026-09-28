from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import SonicRWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
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


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class SonicRLocation(Location):
    game = "SonicR"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: SonicRWorld) -> None:
    create_regular_locations(world)
    #create_events(world)


def create_regular_locations(world: SonicRWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
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


def create_events(world: SonicRWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    top_left_room = world.get_region("Top Left Room")
    final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
