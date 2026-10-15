from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class Difficulty(Choice):
    """
    Sets the default difficulty when connecting to the game. This can be changed in the options menu after connecting.
    """
    display_name = "Difficulty"
    option_easy = 0
    option_normal = 1
    option_hard = 2
    default = 1

class Weather(Choice):
    """
    Sets the default weather when connecting to the game. This can be changed in the options menu after connecting.
    """
    display_name = "Weather"
    option_randomweather = 0
    option_clear = 1
    option_rain = 2
    option_snow = 3
    default = 0

@dataclass
class SonicROptions(PerGameCommonOptions):
    difficulty: Difficulty
    weather: Weather

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [Difficulty],
        [Weather],
    ),
]

option_presets = {
    "Speedrunner": {
        "difficulty": 0,
        "weather": 3,
    },
    "Speedrunner Hard": {
        "difficulty": 2,
        "weather": 3,
    },
}
