from typing import List, Dict, Tuple, Optional, Any
import json


class MetaThing(type):
    """
    MetaThing is a metaclass that ensures the default_actions from each class is inherited by its subclasses
    """
    def __new__(mcs, name: str, bases: Tuple[type], namespace: Dict[str, Any]):
        arg_key = "_class_specific_actions"
        attr_key = "default_actions"

        # Check for existence of _class_specific_accepted_verbs attribute in class definition
        if arg_key in namespace:
            # Create default_accepted_verbs class attribute and set it equal to _class_specific_accepted_verbs
            class_specific = namespace[arg_key]
            del namespace[arg_key]
        else:
            # Initialize default_accepted_verbs class attribute as an empty dict
            class_specific = {}

        result: MetaThing = type.__new__(mcs, name, bases, namespace)
        result.default_accepted_verbs = class_specific

        # Iterate through all immediate base classes
        for base in bases:
            # Check if a base class has its own default_actions attribute
            if hasattr(base, attr_key):
                # If yes, add all key/value pairs from base class's attribute to current class's attribute
                for key, value in getattr(base, attr_key).items():
                    # Only inherit pairs that are not already defined by current class
                    if key not in result.default_accepted_verbs:
                        result.default_accepted_verbs[key] = value

        return result


class Thing(object, metaclass=MetaThing):
    _class_specific_actions: Dict[str, str] = {"do": "stuff", "look": "other_stuff"}

    def __init__(self, name: str, description: str):
        self.name: str = name
        self.description: str = description


class Item(Thing):
    """
    Items are Things that are potentially carry-able or interactive in some way,
    either by the player or a Creature of some kind. Items can also be set as
    an immovable scenery object by setting their carry_able attribute to False.
    """

    _class_specific_actions: Dict[str, str] = {"new": "more_stuff", "do": "overwritten_stuff"}

    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool):
        super().__init__(name, description)
        self.fill_volume: float = fill_volume
        self.weight: float = weight
        self.carry_able: bool = carry_able


class Effect(Thing):
    def __init__(self,
                 name: str,
                 description: str,
                 effect_type: str,
                 lingering: bool,
                 linger_time: int = None,
                 damage: float = None,
                 healing: float = None,
                 stats: Dict[str, float] = None):
        super().__init__(name, description)
        self.effect_type: str = effect_type
        self.lingering: bool = lingering
        self.linger_time: int = linger_time
        self.damage: float = damage
        self.healing: float = healing

        """
        self.stats is a dict with keys that name the stat and float values that are added to the stat
        ex. { "Strength": -1.0, "Speed": 2.5 }  # This would give a Creature +2.5 Speed but -1.0 Strength
        """
        if stats is None:
            self.stats: Dict[str, float] = {}
        else:
            self.stats: Dict[str, float] = stats


class Consumable(Item):
    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool,
                 effects: List[Effect]):
        super().__init__(name, description, fill_volume, weight, carry_able)
        self.effects: List[Effect] = effects


class Container(Item):
    """
    Containers are Items which can hold other Items. They can only hold Items equal to
    or less than their fill_capacity. This is different than weight, because Containers
    can hold items over their max_weight, but the item's durability will slowly tick
    down every turn.
    """

    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool,
                 fill_capacity: float,
                 max_weight: float):
        super().__init__(name, description, fill_volume, weight, carry_able)
        self.fill_capacity: float = fill_capacity
        self.max_weight: float = max_weight

        self.current_fill: float = 0.0
        self.current_weight: float = 0.0
        self._items: List[Item] = []

    def add_item(self, item: Item) -> bool:
        if item.fill_volume > (self.fill_capacity - self.current_fill):
            return False
        else:
            self._items.append(item)
            self.current_fill += item.fill_volume
            self.current_weight += item.weight
            return True

    # TODO: Add remove_item()

    @property
    def weight(self) -> float:
        return self.weight + self.current_weight


class Weapon(Item):
    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool,
                 base_damage: float,
                 required_stats: Dict[str, int] = None,
                 effects: List[Effect] = None):
        super().__init__(name, description, fill_volume, weight, carry_able)
        self.base_damage: float = base_damage

        """
        self.required_stats is a dict with keys that name the stat and int values that specify the required levels
        ex. { "Strength": 9, "Wisdom": 2 }  # This would set the stat requirements to 9 Strength and 2 Wisdom
        """
        if required_stats is None:
            self.required_stats: Dict[str, int] = {}
        else:
            self.required_stats: Dict[str, int] = required_stats

        if effects is None:
            self.effects: List[Effect] = []
        else:
            self.effects: List[Effect] = effects

        self.durability: float = 100.0  # A percentage


class MeleeWeapon(Weapon):
    """
    Sword, dagger, mace, warhammer, etc.
    Has a swing_radius that cannot be exceeded or an attack will always fail
    """

    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool,
                 base_damage: float,
                 swing_radius: float):
        super().__init__(name, description, fill_volume, weight, carry_able, base_damage)
        self.swing_radius: float = swing_radius  # Could use this in hit probability calculations...


class RangedWeapon(Weapon):
    """
    Bow, spells?, anything throwable perhaps?
    Has an effective_range that cannot be exceeded or an attack will always fail
    """

    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool,
                 base_damage: float,
                 effective_range: float):
        super().__init__(name, description, fill_volume, weight, carry_able, base_damage)
        self.effective_range: float = effective_range  # Could use this in hit probability calculations...


class Creature(Thing):
    def __init__(self,
                 name: str,
                 description: str,
                 max_health: float,
                 items: List[Item] = None):
        super().__init__(name, description)
        self.max_health: float = max_health

        if items is None:
            self.items: List[Item] = []
        else:
            self.items: List[Item] = items

        self.active_effects: List[Effect] = []


class SentientCreature(Creature):
    """
    SentientCreatures are Creatures that can talk to other Creatures,
    potentially including the player. These have AI controllers determined
    by their race.
    """

    # A collection of constants defining all possible races in the game
    RACE_DWARF: str = "dwarf"
    RACE_ELF: str = "elf"
    RACE_HUMAN: str = "human"
    RACE_ORC: str = "orc"
    # TODO: Add more race constants OR remove to leave definitions to data files or other external implementation

    def __init__(self,
                 name: str,
                 description: str,
                 max_health: float,
                 items: List[Item] = None,
                 hostile: bool = False,
                 race: str = RACE_HUMAN):
        super().__init__(name, description, max_health, items)
        self.hostile: bool = hostile
        self.race: str = race


class NonSentientCreature(Creature):
    """
    NonSentientCreatures are Creatures that cannot talk to other Creatures.
    These have AI controllers determined by their species.
    """

    # A collection of constants defining all possible species in the game
    SPECIES_DRAGON: str = "dragon"
    SPECIES_GOBLIN: str = "goblin"
    SPECIES_RAT: str = "rat"
    SPECIES_WOLF: str = "wolf"
    # TODO: Add more species constants OR remove to leave definitions to data files or other external implementation

    def __init__(self,
                 name: str,
                 description: str,
                 max_health: float,
                 items: List[Item] = None,
                 hostile: bool = True,
                 species: str = SPECIES_RAT):
        super().__init__(name, description, max_health, items)
        self.hostile: bool = hostile
        self.species: str = species


class Location(object):
    def __init__(self,
                 x: int = None,
                 y: int = None,
                 z: int = None,
                 map_set: str = "__default__",
                 string: str = None):
        # The set of rooms this belongs to. Used to specify particular worlds/dimensions/etc.
        # Value could be something like "Over-world" or "Underworld" or "Earth" or "Mirror-Dimension"
        self._map_set: str = map_set

        if x is None and y is None and z is None:
            # All else fails, coordinates default to zero
            self.x: int = 0
            self.y: int = 0
            self.z: int = 0
            if string is not None:
                self.set_location(string)
        else:
            self.x = x
            self.y = y
            self.z = z

    def set_location(self, string: str) -> bool:
        # Takes str argument in the format "(x,y,z)"
        temp_x = self.x
        temp_y = self.y
        temp_z = self.z
        coordinates = string.strip("()").split(",")
        try:
            self.x = int(coordinates[0].strip(" "))
            self.y = int(coordinates[1].strip(" "))
            self.z = int(coordinates[2].strip(" "))
            return True
        except IndexError:
            # If all three coordinates aren't supplied, revert values
            self.x = temp_x
            self.y = temp_y
            self.z = temp_z
            return False

    @property
    def map_set(self) -> str:
        return self._map_set


class Room(Thing):
    """
    Rooms are Things that Creatures can travel between. They are the building
    blocks of the map and store references to all items and creatures inside of them.
    """

    def __init__(self,
                 name: str,
                 description: str,
                 location: Location,
                 # TODO: Possibly simplify following parameters to single list of Things
                 items: List[Item] = None,
                 creatures: List[Creature] = None):
        super().__init__(name, description)
        self.location: Location = location

        if items is None:
            self.items: List[Item] = []
        else:
            self.items: List[Item] = items

        if creatures is None:
            self.creatures: List[Creature] = []
        else:
            self.creatures: List[Creature] = creatures


class RoomMap(object):
    """
    RoomMap class stores references to and tracks the location of all Rooms in existence.
    There is no need to instantiate this class, as the methods are static and separate
    worlds/dimensions/etc. can be specified by the Location objects being passed to the class.
    """

    _rooms: Dict[str, Room] = {}

    @staticmethod
    def _location_to_key(loc: Location) -> str:
        # Returns a unique string based on coordinates given by loc
        return loc.map_set + "_" + str(loc.x) + "_" + str(loc.y) + "_" + str(loc.z)

    @staticmethod
    def get_room(loc: Location) -> Optional[Room]:
        # If Room at loc does not exist, returns None
        key = RoomMap._location_to_key(loc)
        if key in RoomMap._rooms:
            return RoomMap._rooms[RoomMap._location_to_key(loc)]
        else:
            return None

    @staticmethod
    def room_exists(loc: Location) -> bool:
        # Returns True if Room at loc exists, false if not
        # In most cases, it is more efficient to just call get_room and check for None.
        # Only call this function if you will not need a reference to the room later.
        return False if RoomMap.get_room(loc) is None else True

    @staticmethod
    def set_room(loc: Location, room: Room) -> None:
        RoomMap._rooms[RoomMap._location_to_key(loc)] = room

    @staticmethod
    def move_room(old_loc: Location, new_loc: Location) -> bool:
        # Overwrites any room already in new_loc
        # Returns True if successful and False if unsuccessful (i.e. Room in old_loc doesn't exist)
        room = RoomMap.get_room(old_loc)
        if room is None:
            return False
        else:
            RoomMap.set_room(new_loc, room)
            RoomMap.remove_room(old_loc)
            return True

    @staticmethod
    def swap_rooms(first_loc: Location, second_loc: Location) -> bool:
        first_room = RoomMap.get_room(first_loc)
        second_room = RoomMap.get_room(second_loc)
        if first_room is None or second_room is None:
            return False
        else:
            RoomMap.set_room(first_loc, second_room)
            RoomMap.set_room(second_loc, first_room)
            return True

    @staticmethod
    def remove_room(loc: Location) -> None:
        try:
            del RoomMap._rooms[RoomMap._location_to_key(loc)]
        except KeyError:
            # Key already doesn't exist; no need to do anything else.
            pass


'''
This is just an example of how to use json files, viewer discretion  is advised.

I don't think we will have to use individual json files for each item, but every time i try to put
all the bows in one file it gives me an error and I don't get paid enough for this shit to keep trying.
'''


def get_json(file_path_and_name):
    with open(file_path_and_name, 'r') as f:
        return json.load(f)


myObj = get_json('json_files/bows.json')
# Iterate through Weapons, which is a Python list
for weapon in myObj['Weapons']:
    # Iterate through each weapon's key/value pairs (each weapon is a Python dictionary)
    for key in weapon:
        # Print out name of attribute and then value of attribute
        print(key, weapon[key])


myObj2 = get_json('json_files/armor1.json')
for armor in myObj2['Armor1']:
    for key in armor:
         print(key, armor[key])

"""
Process of creating an Items in the world:

(1) JSON file is read:
{
    "rooms": [
        {
            "name": "Starting Room",
            "description": "The room is dark and oddly humid, with a pungent odor of rotting corpses.",
            "location": "(0,0)",
            "items": [
                {
                    "type": "MeleeWeapon",
                    "name": "Rusty Sword",
                    "description": "It's a dull sword, worn by time. The sword was probably only used as decoration.",
                    # No need for carry_able because the default value will be used.
                    "weight": 10.0,
                    "swing_radius": 2.0
                }
            ]
        },
        {
            "name": "Next Room",
            "location": "(0,1)",
            "items": []  # Not necessary because an empty list is the default
        }
    ]
}

(2) Rooms are created, and then objects are placed in them:
rooms = parsed_json.rooms
for cur_room in rooms:
    room = Room(cur_room.name, cur_room.description, cur_room.location)
    for cur_item in cur_room.items
        # switch statement involving cur_item.type
        # ...
        item = MeleeWeapon(name=cur_item.name,
                               description=cur_item.description,
                               weight=cur_item.weight,
                               swing_radius=cur_item.swing_radius
                               )
        room.add_item(item)
    # Most likely a similar loop for NPC placement
.# ....
"""
