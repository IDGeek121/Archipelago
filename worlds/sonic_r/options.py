from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  APQuest doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md

class HardMode(Toggle):
    """
    In hard mode, the basic enemy and the final boss will have more health.
    The Health Upgrades become progression, as they are now required to beat the final boss.
    """

    # The docstring of an option is used as the description on the website and in the template yaml.

    # You'll also want to set a display name, which will determine what the option is called on the website.
    display_name = "Hard Mode"

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class SonicROptions(PerGameCommonOptions):
    hard_mode: HardMode

# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [HardMode],
    ),
]

option_presets = {
    "test": {
        "hard_mode": False,
    },
}
