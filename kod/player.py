class Thing(object):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Item(Thing):
    """
    Items are Things that are potentially carry-able or interactive in some way,
    either by the player or a Creature of some kind. Items can also be set as
    an immovable scenery object by setting their carry_able attribute to False.
    """
    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool):
        super().__init__(name, description)
        self.carry_able = carry_able
        self.fill_volume = fill_volume  # The amount of space an Item takes up
        self.weight = weight
        # self.enchantments = [list of enchantments] ?

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
                 carry_able: bool = True):
        super().__init__(name, description, fill_volume, weight, carry_able)
        
        self.durability = 100.0  # A percentage

class RangedWeapon(Weapon):
    """
    Bow, spells?, anything throwable perhaps?
    """
    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool = True,
                 effective_range: float = 25.0):

        super().__init__(name, description, fill_volume, weight, carry_able)
        self.effective_range = effective_range  # Could use this in hit probability calculations...

        
class StringBow(RangedWeapon):
    '''
    Really bad bow.
    '''
    def __init__(self,
                  name: str,
                  description: str,
                  fill_volume: float,
                  weight: float,
                  carry_able: bool = True,
                  effective_range: float = 15.0):

    
        super().__init__(name, description, fill_volume, weight, carry_able)
        
        self.name = name
        self.description= description
        self.fill_volume = fill_volume
        self.weight = weight
        self.carry_able = carry_able
        self.effective_range = effective_range
        
        lowrangebow = StringBow('Feather String Bow', 'Great bow for beggingers',
                              4.0, 4.0) #Giving the bow values


class ValkyrieBow(RangedWeapon):
    '''
    Mid-Range Bow
    '''
    def __init__(self,
                  name: str,
                  description: str,
                  fill_volume: float,
                  weight: float,
                  carry_able: bool = True,
                  effective_range: float = 25.0):

        super().__init__(name, description, fill_volume, weight, carry_able)
        
        self.name = name
        self.description= description
        self.fill_volume = fill_volume
        self.weight = weight
        self.carry_able = carry_able
        self.effective_range = effective_range
        
        midrangebow = ValkarieBow('Valkarie Bone Bow', 'Difficult to use, but very deadly',
                                   6.0, 6.0)



