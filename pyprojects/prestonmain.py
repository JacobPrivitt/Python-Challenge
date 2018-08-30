class Item:
    """
    Items are any Objects that are potentially carry-able or interactive in some way,
    either by the player or a Creature of some kind.
    """
    def __init__(self, name, description, carry_able, fill_volume, weight):
        self.name = name
        self.description = description
        self.carry_able = carry_able
        self.fill_volume = fill_volume  # The amount of space an Item takes up
        self.weight = weight
        # self.enchantments = [list of enchantments] ?


class Container(Item):
    """
    Containers are Items which can hold other Items. They can only hold Items equal to
    or less than their fill_capacity. This is different than weight, because Containers
    can hold items over their max_weight, but the item's durability will slowly tick
    down every turn.
    """
    current_fill = 0.0
    current_weight = 0.0

    def __init__(self,  # Default values aren't necessarily needed and might be removed
                 name="Container",
                 description="It's a container to keep things in.",
                 carry_able=True,
                 fill_volume=10.1,
                 weight=0.5,
                 fill_capacity=10.0,
                 max_weight=15.0
                 ):
        super().__init__(name, description, carry_able, fill_volume, weight)
        self.fill_capacity = fill_capacity
        self.max_weight = max_weight


class Weapon(Item):
    durability = 100.0  # A percentage
    # TODO: Maybe player trait requirements
    # required_strength = 3
    # required_agility = 2
    # etc.

    def __init__(self, name, description, carry_able=True, weight=10.0):
        super().__init__(name, description, carry_able, weight)


class NonRangedWeapon(Weapon):
    """
    Sword, dagger, mace, warhammer, etc.
    Has a swing_radius that cannot be exceeded or an attack will always fail
    """
    def __init__(self, name, description, carry_able=True, weight=15.0, swing_radius=3.0):
        super().__init__(name, description, carry_able, weight)
        self.swing_radius = swing_radius  # Could use this in hit probability calculations...


class RangedWeapon(Weapon):
    """
    Bow, spells?, anything throwable perhaps?
    """
    def __init__(self, name, description, carry_able=True, weight=8.0, effective_range=25.0):
        super().__init__(name, description, carry_able, weight)
        self.effective_range = effective_range  # Could use this in hit probability calculations...


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
                    "type": "NonRangedWeapon",
                    "name": "Rusty Sword",
                    "description": "It's a dull old sword, worn by time. The sword was probably only used as decoration.",
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
        item = NonRangedWeapon(name=cur_item.name,
                               description=cur_item.description,
                               weight=cur_item.weight,
                               swing_radius=cur_item.swing_radius
                               )
        room.add_item(item)
    # Most likely a similar loop for NPC placement
# ....
"""
