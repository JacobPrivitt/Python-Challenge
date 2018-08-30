from typing import List, Optional


class Thing(object):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Item(object):
    """
    Items are Things that are potentially carry-able or interactive in some way,
    either by the player or a Creature of some kind. Items can also be set as
    an immovable scenery object by setting their carry_able attribute to False.
    """

    def __init__(self,
                 name: str,
                 # Removed attack because an Item won't necessarily be a Weapon (i.e. Food is an Item)
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool):
        self.name = name
        self.description = description
        self.fill_volume = fill_volume
        self.weight = weight
        self.carry_able = carry_able


class Container(Item):
    """
    Containers are Items which can hold other Items. They can only hold Items equal to
    or less than their fill_capacity. This is different than weight, because Containers
    can hold items over their max_weight, but the item's durability will slowly tick
    down every turn.
    """

    def __init__(self,  # Default values aren't necessarily needed and might be removed
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool,
                 fill_capacity: float,
                 max_weight: float
                 ):
        super().__init__(name, description, fill_volume, weight, carry_able)
        self.fill_capacity = fill_capacity
        self.max_weight = max_weight

        self.current_fill = 0.0
        self.current_weight = 0.0


class Weapon(Item):
    # TODO: Maybe player trait requirements
    # required_strength = 3
    # required_agility = 2
    # etc.
    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool):
        super().__init__(name, description, fill_volume, weight, carry_able)

        self.durability = 100.0  # A percentage


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

                 swing_radius: float):
        super().__init__(name, description, fill_volume, weight, carry_able)
        self.swing_radius = swing_radius  # Could use this in hit probability calculations...


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
                 effective_range: float):
        super().__init__(name, description, fill_volume, weight, carry_able)
        self.effective_range = effective_range  # Could use this in hit probability calculations...



class Creature(Thing):
    def __init__(self,
                 name: str,
                 description: str,
                 max_health: float,
                 items: List[Item] = None):
        super().__init__(name, description)
        self.max_health = max_health

        if items is None:
            self.items = []
        else:
            self.items = items


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
        self.hostile = hostile
        self.race = race


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
        self.hostile = hostile
        self.species = species


class Location(object):
    def __init__(self,
                 x: int = None,
                 y: int = None,
                 z: int = None,
                 map_set: str = "__default__",
                 string: str = None):
        # The set of rooms this belongs to. Used to specify particular worlds/dimensions/etc.
        # Value could be something like "Over-world" or "Underworld" or "Earth" or "Mirror-Dimension"
        self._map_set = map_set

        if x is None and y is None and z is None:
            # All else fails, coordinates default to zero
            self.x = 0
            self.y = 0
            self.z = 0
            if string is not None:
                self.set_location(string)
        else:
            self.x = x
            self.y = y
            self.z = z

    def set_location(self, string: str):
        # Takes str argument in the format "(x,y,z)"
        temp_x = self.x
        temp_y = self.y
        temp_z = self.z
        coordinates = string.strip("()").split(",")
        try:
            self.x = int(coordinates[0].strip(" "))
            self.y = int(coordinates[1].strip(" "))
            self.z = int(coordinates[2].strip(" "))
        except IndexError:
            # If all three coordinates aren't supplied, revert values
            self.x = temp_x
            self.y = temp_y
            self.z = temp_z

    @property
    def map_set(self):
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
                 items: List[Item] = None,
                 creatures: List[Creature] = None):
        super().__init__(name, description)
        self.location = location

        if items is None:
            self.items = []
        else:
            self.items = items

        if creatures is None:
            self.creatures = []
        else:
            self.creatures = creatures


class RoomMap(object):
    """
    RoomMap class stores references to and tracks the location of all Rooms in existence.
    There is no need to instantiate this class, as the methods are static and separate
    worlds/dimensions/etc. can be specified by the Location objects being passed to the class.
    """

    _rooms = {}

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
    def remove_room(loc: Location):
        try:
            del RoomMap._rooms[RoomMap._location_to_key(loc)]
        except KeyError:
            # Key already doesn't exist; no need to do anything else.
            pass


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
