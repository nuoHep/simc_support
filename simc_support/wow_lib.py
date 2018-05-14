# -*- coding: utf-8 -*-
## Utility file for class specialisations
## Contains wow classes, specs, dps talent rows,
## races, trinkets

# these values are used throughout the code to determine itemlevel "borders" of items
TRADER_TOKEN = 0  # usually used as a catch up mechanic, drops usually all items from previous content
DUNGEON_ITEMLEVEL = 300  # standard dungeon itemlevel (normal, max level dungeon)
M_PLUS_DROPLEVEL = 340  # highest available itemlevel from m+ dungeons. weekly chest is NOT included here
TITANFORGE_CAP = 355  # currently highest itemlevel titanforging cap


class Trinket(object):
  """docstring for trinket"""

  def __init__(
    self,
    name,
    item_id,
    min_itemlevel,
    max_itemlevel,
    max_itemlevel_drop,
    agility,
    intellect,
    strength,
    melee,
    ranged,
    legendary=False
  ):
    super(Trinket, self).__init__()
    self.name: str = str(name)
    self.item_id: str = str(item_id)
    self.min_itemlevel: int = int(min_itemlevel)
    self.max_itemlevel: int = int(max_itemlevel)
    self.max_itemlevel_drop: int = int(max_itemlevel_drop)
    self.agility: bool = bool(agility)
    self.intellect: bool = bool(intellect)
    self.strength: bool = bool(strength)
    self.melee: bool = bool(melee)
    self.ranged: bool = bool(ranged)
    self.legendary: bool = bool(legendary)


__class_data = {
  "Death_Knight": {
    "talents": "1110011",
    "id": 6,
    "specs": {
      "Blood": {
        "role": "melee",
        "stat": "str",
        "id": 250,
      },
      "Frost": {
        "role": "melee",
        "stat": "str",
        "id": 251,
      },
      "Unholy": {
        "role": "melee",
        "stat": "str",
        "id": 252,
      }
    }
  },
  "Demon_Hunter": {
    "talents": "1110111",
    "id": 12,
    "specs": {
      "Havoc": {
        "role": "melee",
        "stat": "agi",
        "id": 577,
      },
      "Vengance": {
        "role": "melee",
        "stat": "agi",
        "id": 581,
      }
    }
  },
  "Druid": {
    "talents": "1000111",
    "id": 11,
    "specs": {
      "Balance": {
        "role": "ranged",
        "stat": "int",
        "id": 102,
      },
      "Feral": {
        "role": "melee",
        "stat": "agi",
        "id": 103,
      },
      "Guardian": {
        "role": "melee",
        "stat": "agi",
        "id": 104,
      }
    }
  },
  "Hunter": {
    "talents": "1101011",
    "id": 3,
    "specs": {
      "Beast_Mastery": {
        "role": "ranged",
        "stat": "agi",
        "id": 253,
      },
      "Marksmanship": {
        "role": "ranged",
        "stat": "agi",
        "id": 254,
      },
      "Survival": {
        "role": "melee",
        "stat": "agi",
        "id": 255,
      }
    }
  },
  "Mage": {
    "talents": "1011011",
    "id": 8,
    "specs": {
      "Arcane": {
        "role": "ranged",
        "stat": "int",
        "id": 62,
      },
      "Fire": {
        "role": "ranged",
        "stat": "int",
        "id": 63,
      },
      "Frost": {
        "role": "ranged",
        "stat": "int",
        "id": 64,
      }
    }
  },
  "Monk": {
    "talents": "1010011",
    "id": 10,
    "specs": {
      "Brewmaster": {
        "role": "melee",
        "stat": "agi",
        "id": 268,
      },
      "Windwalker": {
        "role": "melee",
        "stat": "agi",
        "id": 269,
      }
    }
  },
  "Paladin": {
    "talents": "1101001",
    "id": 2,
    "specs": {
      "Protection": {
        "role": "melee",
        "stat": "str",
        "id": 66,
      },
      "Retribution": {
        "role": "melee",
        "stat": "str",
        "id": 70,
      }
    }
  },
  "Priest": {
    "talents": "1001111",
    "id": 5,
    "specs": {
      "Shadow": {
        "role": "ranged",
        "stat": "int",
        "id": 258,
      }
    }
  },
  "Rogue": {
    "talents": "1110111",
    "id": 4,
    "specs": {
      "Assassination": {
        "role": "melee",
        "stat": "agi",
        "id": 259,
      },
      "Outlaw": {
        "role": "melee",
        "stat": "agi",
        "id": 260,
      },
      "Subtlety": {
        "role": "melee",
        "stat": "agi",
        "id": 261,
      }
    }
  },
  "Shaman": {
    "talents": "1001111",
    "id": 7,
    "specs": {
      "Elemental": {
        "role": "ranged",
        "stat": "int",
        "id": 262,
      },
      "Enhancement": {
        "role": "melee",
        "stat": "agi",
        "id": 263,
      }
    }
  },
  "Warlock": {
    "talents": "1101011",
    "id": 9,
    "specs": {
      "Affliction": {
        "role": "ranged",
        "stat": "int",
        "id": 265,
      },
      "Demonology": {
        "role": "ranged",
        "stat": "int",
        "id": 266,
      },
      "Destruction": {
        "role": "ranged",
        "stat": "int",
        "id": 267,
      }
    }
  },
  "Warrior": {
    "talents": "1010111",
    "id": 1,
    "specs": {
      "Arms": {
        "role": "melee",
        "stat": "str",
        "id": 71,
      },
      "Fury": {
        "role": "melee",
        "stat": "str",
        "id": 72,
      },
      "Protection": {
        "role": "melee",
        "stat": "str",
        "id": 73,
      }
    }
  }
}

__races = {
  "alliance": {
    "draenei": (
      "warrior", "paladin", "hunter", "priest", "shaman", "mage", "monk",
      "death_knight"
    ),
    "dwarf": (
      "warrior", "paladin", "hunter", "rogue", "priest", "shaman", "mage",
      "warlock", "monk", "death_knight"
    ),
    "gnome": (
      "warrior", "hunter", "rogue", "priest", "mage", "warlock", "monk",
      "death_knight"
    ),
    "human": (
      "warrior", "paladin", "hunter", "rogue", "priest", "mage", "warlock",
      "monk", "death_knight"
    ),
    "nightelf": (
      "warrior", "hunter", "rogue", "priest", "mage", "monk", "druid",
      "death_knight"
    ),
    "pandaren": (
      "warrior", "hunter", "rogue", "priest", "shaman", "mage", "monk"
    ),
    "worgen": (
      "warrior", "hunter", "rogue", "priest", "mage", "warlock", "druid",
      "death_knight"
    ),
    "void_elf": (
      "warrior", "hunter", "rogue", "priest", "mage", "warlock", "monk"
    ),
    "lightforged_draenei": ("warrior", "paladin", "hunter", "priest", "mage"),
    #"dark_iron_dwarf": ("shaman")
  },
  "horde": {
    "bloodelf": (
      "warrior", "paladin", "hunter", "rogue", "priest", "mage", "warlock",
      "monk", "death_knight"
    ),
    "goblin": (
      "warrior", "hunter", "rogue", "priest", "shaman", "mage", "warlock",
      "death_knight"
    ),
    "orc": (
      "warrior", "hunter", "rogue", "shaman", "mage", "warlock", "monk",
      "death_knight"
    ),
    "pandaren": (
      "warrior", "hunter", "rogue", "priest", "shaman", "mage", "monk"
    ),
    "tauren": (
      "warrior", "paladin", "hunter", "priest", "shaman", "monk", "druid",
      "death_knight"
    ),
    "troll": (
      "warrior", "hunter", "rogue", "priest", "shaman", "mage", "warlock",
      "monk", "druid", "death_knight"
    ),
    "undead": (
      "warrior", "hunter", "rogue", "priest", "mage", "warlock", "monk",
      "death_knight"
    ),
    "nightborne": (
      "warrior", "hunter", "rogue", "priest", "mage", "warlock", "monk"
    ),
    "highmountain_tauren": ("warrior", "hunter", "shaman", "monk", "druid"),
    #"maghar_orc": ("shaman")
  }
}

__trinket_list = [
  # dungeon trinkets
  Trinket(
    "My'das Talisman", "158319", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Rezan's Gleaming Eye", "158712", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Vessel of Skittering Shadows", "159610", DUNGEON_ITEMLEVEL,
    TITANFORGE_CAP, TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Harlan's Loaded Dice", "155881", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Lustrous Golden Plumage", "159617", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Briny Barnacle", "159619", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Galecaller's Boon", "159614", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Conch of Dark Whispers", "159620", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Dead-Eye Spyglass", "159623", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Hadal's Nautilus", "159622", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Tiny Electromental in a Jar", "158374", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Merektha's Fang", "158367", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Razdunk's Big Red Button", "159611", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Tik'ali's Resonating Heart", "159612", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  # The Underrot
  Trinket(
    "Lingering Sporepods", "159626", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, True, False, False
  ),
  Trinket(
    "Rotcrusted Voodoo Doll", "159624", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Vial of Animated Blood", "159625", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  Trinket(
    "Jes' Howler", "159627", DUNGEON_ITEMLEVEL, TITANFORGE_CAP, TRADER_TOKEN,
    False, False, True, False, False
  ),
  Trinket(
    "Cannonball Hurdler", "159628", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, True, False, False, False, False
  ),
  Trinket(
    "Ignition Mage's Fuse", "159615", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Lady Waycrest's Music Box", "159631", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Balefire Branch", "159630", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, True, False, False, False
  ),
  Trinket(
    "Gorecrusted Butcher's Block", "159616", DUNGEON_ITEMLEVEL, TITANFORGE_CAP,
    TRADER_TOKEN, False, False, True, False, False
  ),
  # Trinket(
  #   "", "", DUNGEON_ITEMLEVEL, TITANFORGE_CAP, TRADER_TOKEN,
  #   False, False, False, False, False
  # ),
]


def is_melee(wow_class, wow_spec):
  """True if spec is melee spec.

  Arguments:
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Returns:
    bool -- True, if role of the spec is 'melee'.
  """

  return get_role(wow_class, wow_spec) == "melee"


def is_ranged(wow_class, wow_spec):
  """True if spec is a ranged spec.

  Arguments:
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Returns:
    bool -- True, if role of the spec is 'ranged'.
  """

  return get_role(wow_class, wow_spec) == "ranged"


def get_mask_for_spec(wow_class, wow_spec):
  """Mask to get appropriate Trinkets.

  Arguments:
    wow_class {str} -- world of warcraft class name
    wow_spec {str} -- world of warcraft spec name

  Returns:
    tuple(melee{bool}, ranged{bool}, main_stat_agi{bool}, main_stat_int{bool}, main_stat_str{bool}) -- Returns a bool tuple mask to match the True's with Trinket
  """

  melee = is_melee(wow_class, wow_spec)
  ranged = is_ranged(wow_class, wow_spec)
  main_stat = get_main_stat(wow_class, wow_spec)
  main_stat_agi = main_stat == "agi"
  main_stat_int = main_stat == "int"
  main_stat_str = main_stat == "str"

  return (melee, ranged, main_stat_agi, main_stat_int, main_stat_str)


def get_trinkets_for_spec(wow_class, wow_spec):
  """New function to return all available trinkets for a spec

  Arguments:
    wow_class {str} -- name of the wow class
    wow_spec {str} -- name of the wow spec

  Returns:
    list[Trinket] -- List of all Trinkets
  """

  melee, ranged, agility, intellect, strength = get_mask_for_spec(
    wow_class, wow_spec
  )
  return_list = []
  for trinket in __trinket_list:
    if melee and trinket.melee:
      return_list.append((
        trinket.name, trinket.item_id, trinket.min_itemlevel,
        trinket.max_itemlevel, trinket.max_itemlevel_drop
      ))
    elif ranged and trinket.ranged:
      return_list.append((
        trinket.name, trinket.item_id, trinket.min_itemlevel,
        trinket.max_itemlevel, trinket.max_itemlevel_drop
      ))
    elif agility and trinket.agility:
      return_list.append((
        trinket.name, trinket.item_id, trinket.min_itemlevel,
        trinket.max_itemlevel, trinket.max_itemlevel_drop
      ))
    elif intellect and trinket.intellect:
      return_list.append((
        trinket.name, trinket.item_id, trinket.min_itemlevel,
        trinket.max_itemlevel, trinket.max_itemlevel_drop
      ))
    elif strength and trinket.strength:
      return_list.append((
        trinket.name, trinket.item_id, trinket.min_itemlevel,
        trinket.max_itemlevel, trinket.max_itemlevel_drop
      ))
  return return_list


def get_second_trinket_for_spec(wow_class, wow_spec):
  main_stat = get_main_stat(wow_class, wow_spec)
  if main_stat == "agi":
    #return ',id=,ilevel={}'.format(DUNGEON_ITEMLEVEL if DUNGEON_ITEMLEVEL > TRADER_TOKEN else TRADER_TOKEN)
    return ''
  if main_stat == "int":
    #return ',id=,ilevel={}'.format(DUNGEON_ITEMLEVEL if DUNGEON_ITEMLEVEL > TRADER_TOKEN else TRADER_TOKEN)
    return ''
  if main_stat == "str":
    #return ',id=,ilevel={}'.format(DUNGEON_ITEMLEVEL if DUNGEON_ITEMLEVEL > TRADER_TOKEN else TRADER_TOKEN)
    return ''


def get_trinket_id(trinket_name):
  """Return the trinket id as string. Function can handly extended names like 'Pancakes Specialtext' and will still return the ID of 'Pancakes' in this case.

  Arguments:
    trinket_name {str} -- trinket name

  Returns:
    str -- item ID as string
  """

  for trinket in __trinket_list:
    # ordered like this to allows look ups of extended names like "Norgannons + 15" to yield an ID
    if trinket.name in trinket_name:
      return trinket.item_id


def get_all_trinkets():
  """Get a list of all known trinket names.

  Returns:
    list[trinket_name{str}] -- List of all trinket names.
  """

  all_trinkets = []
  for trinket in __trinket_list:
    all_trinkets.append(trinket.name)
  return all_trinkets


def __generate_talent_combinations(blueprint, wow_class, wow_spec):
  """Generate all talent combinations matching blueprint. You're an enduser? Use get_talent_combinations(...).

  Arguments:
    blueprint {str} -- [description]
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Returns:
    list[talent_combination{str}] -- [description]
  """

  if not ("x" in blueprint or "-" in blueprint):
    return [blueprint]
  data_talents = get_dps_talents(wow_class)
  pattern = ""

  for i in range(0, 7):
    if (blueprint[i] == "-" or blueprint[i] == "x") and data_talents[i] == "0":
      pattern += "0"
    else:
      pattern += blueprint[i]

  combinations = []
  for first in range(4):
    for second in range(4):
      for third in range(4):
        for forth in range(4):
          for fivth in range(4):
            for sixth in range(4):
              for seventh in range(4):
                combination = str(first) + str(second) + str(third) + str(
                  forth
                ) + str(fivth) + str(sixth) + str(seventh)
                add_it = True

                # check whether the generated talent combination fits the wanted blueprint
                for i in range(7):
                  if (not (pattern[i] == "-" or pattern[i] == "x")
                     ) and not combination[i] == pattern[i]:
                    add_it = False
                  if combination[i] == "0" and (
                    pattern[i] == "-" or pattern[i] == "x"
                  ):
                    add_it = False
                if add_it:
                  combinations += [combination]

  return combinations


def is_talent_combination(talent_combination):
  """Check the talent_combination for valid format.

  Arguments:
    talent_combination {str} -- [description]

  Returns:
    bool -- True, if the format matches the required format of get_talent_combinations
  """

  if talent_combination == None:
    return False
  if not type(talent_combination) is str:
    return False
  if talent_combination == "":
    return True
  if len(talent_combination) == 7:
    for letter in talent_combination:
      if not (
        letter == "0" or letter == "1" or letter == "2" or letter == "3" or
        letter == "-" or letter == "x"
      ):
        return False
    return True
  elif len(talent_combination) == 2:
    for letter in talent_combination:
      if not (
        letter == "0" or letter == "1" or letter == "2" or letter == "3"
      ):
        return False
    return True
  # Would've been for talent combinations that set certain rows to a value without declaring anything else.
  # Like 42 would set the forth row to the second talent. 4253 would set 4. row to 2 and 5. to 3
  #elif len(talent_combination) % 2 == 0:
  #  for i in range(0, len(talent_combination)):
  #    if (i + 1) % 2 == 1 and not int(talent_combination[i]) in range(1,8):
  #      return False
  #    elif not int(talent_combination[i]) in range(0,4):
  #      return False
  #  return True
  else:
    return False


def get_talent_combinations(wow_class, wow_spec, user_input=""):
  """Get a list of all valid dps talent combinations for a wow_class and wow_spec. If user_input is given the provided mask is used for this genertion and pruning of the talent combination list.

  Arguments:
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Keyword Arguments:
    user_input {str} -- Mask to determine whether a combination is valid or not. Class inherent masks are used in addition to the user input. Input can either be empty, of len 2 or len 7. len two is understood as a mask for the last two valid dps rows. len seven is understood as a mask for all talent rows. Write 'x' or '-' as a placeholder. Example: '201xx03' will generate 9 talent combinations if both x are dps talents. (default: {""})

  Returns:
    list[talent_combination{str}] -- List of all valied talent combinations for a class.
  """

  combinations = []

  if user_input == "" or user_input == None:
    combinations = __generate_talent_combinations(
      "xxxxxxx", wow_class, wow_spec
    )

  elif len(user_input) == 2:
    combinations = __generate_talent_combinations(
      "xxxxx" + user_input, wow_class, wow_spec
    )

  elif len(user_input) == 7:
    combinations = __generate_talent_combinations(
      user_input, wow_class, wow_spec
    )

  else:
    # something unexpected occured
    return None

  return combinations


def get_classes():
  """Get a list of all wow classes.

  Returns:
    list[wow_class_name{str}] -- List of all wow class names.
  """

  classes = []
  for wow_class in __class_data:
    classes.append(wow_class)
  return classes


def get_classes_specs():
  """Get a list of all wow classes and wow specs.

  Returns:
    List[Tuple(String, String)] -- List of all wow_class and wow_spec combinations
  """

  class_list = get_classes()
  full_list = []
  for wow_class in class_list:
    for spec in get_specs(wow_class):
      full_list.append((wow_class, spec))
  return full_list


def get_races():
  """Get a list of all wow race names.

  Returns:
    list[wow_race_name{str}] -- List of all wow race names
  """

  races = []
  for faction in __races.keys():
    for race in __races[faction].keys():
      if not race in races:
        races.append(race)
  return races


def get_races_for_class(wow_class):
  """Get a list of all available races to the given wow_class.

  Arguments:
    wow_class {str} -- wow class name

  Returns:
    list[wow_race_name{str}] -- List of all available races to the given wow_class.
  """

  race_list = []
  for faction in __races.keys():
    for race in __races[faction].keys():
      # additionally prevent double races like pandaren
      if str(wow_class).lower() in __races[faction][race
                                                   ] and not race in race_list:
        race_list.append(race)
  return race_list


def get_role(wow_class, wow_spec):
  """Get the role of the given wow class and wow spec.

  Arguments:
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Returns:
    str -- role ('ranged'/'melee')
  """

  return __class_data[wow_class.title()]["specs"][wow_spec.title()]["role"]


def get_class_id(wow_class: str) -> int:
  """Get the wow ID of the given class.

  Arguments:
    wow_class {str} -- [description]

  Returns:
    int -- wow_class_id
  """

  return __class_data[wow_class.title()]["id"]


def get_spec_id(wow_class: str, wow_spec: str) -> int:
  """Get the ID of a given spec.

  Arguments:
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Returns:
    int -- wow_spec_id
  """

  return __class_data[wow_class.title()]["specs"][wow_spec.title()]["id"]


def get_main_stat(wow_class, wow_spec):
  """Get the main stat of a class and spec.

  Arguments:
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Returns:
    str -- main stat (agi / int / str)
  """

  return __class_data[wow_class.title()]["specs"][wow_spec.title()]["stat"]


def get_dps_talents(wow_class, wow_spec=""):
  """Return the dps talent mask for a spec. DPS talents are represented by a '1', non-DPS talent are represented by a '0' (zero).

  Arguments:
    wow_class {str} -- [description]

  Keyword Arguments:
    wow_spec {str} -- wow spec, usually not needed as of Legion. Specs of one class share the same utility rows, not necessarily the talents there,though (default: {""})

  Returns:
    str -- talent mask, e.g. '1011101'
  """

  return __class_data[wow_class.title()]["talents"]


def get_specs(wow_class):
  """Get a list of spec names for a given wow class.

  Arguments:
    wow_class {str} -- [description]

  Returns:
    list[wow_spec{str}] -- List of all available wow specs of the wow_class.
  """

  spec_collection = []
  for spec in __class_data[wow_class.title()]["specs"]:
    spec_collection.append(spec)
  return spec_collection


def is_class(wow_class):
  """True, if wow_class is class of WoW.

  Arguments:
    wow_class {str} -- [description]

  Returns:
    boold -- True if wow_class is class of WoW.
  """

  for base_class in get_classes():
    if wow_class.lower() == base_class.lower():
      return True
  return False


def is_race(race):
  """True, if race is a wow race.

  Arguments:
    race {str} -- [description]

  Returns:
    bool -- True, if race is a wow race.
  """

  if race in get_races():
    return True
  return False


def is_spec(wow_spec):
  """True, if wow_spec is a spec in WoW.

  Arguments:
    wow_spec {str} -- [description]

  Returns:
    bool -- True, if wow_spec is a spec in WoW.
  """

  spec_list = []
  classes = get_classes()
  for wow_class in classes:
    specs = get_specs(wow_class)
    for spec in specs:
      spec_list.append(spec)
  for spec in spec_list:
    if wow_spec.lower() == spec.lower():
      return True
  return False


def is_class_spec(wow_class, wow_spec):
  """True, if wow_spec and wow_class match.

  Arguments:
    wow_class {str} -- [description]
    wow_spec {str} -- [description]

  Returns:
    bool -- True, if wow_class and wow_spec match.
  """

  if is_class(wow_class):
    if is_spec(wow_spec):
      for spec in get_specs(wow_class):
        if wow_spec.lower() == spec.lower():
          return True
  return False


def is_dps_talent_combination(talent_combination, wow_class):
  """Determines whether a given talent combination is a valid talent combination of the wow_class.

  Arguments:
    talent_combination {str} -- [description]
    wow_class {str} -- [description]

  Returns:
    bool -- True, if all dps talent rows have a talent selected and all utility rows have no talent selected.
  """

  for i in range(0, 7):
    if talent_combination[i] == "0" and __class_data[wow_class]["talents"
                                                               ][i] == "1":
      return False
    elif not talent_combination[i] == "0" and __class_data[wow_class][
      "talents"
    ][i] == "0":
      return False
  return True
