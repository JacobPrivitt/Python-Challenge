class Thing(object):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


'''
class Item(object):
    """
    Items are Things that are potentially carry-able or interactive in some way,
    either by the player or a Creature of some kind. Items can also be set as
    an immovable scenery object by setting their carry_able attribute to False.
    """
    def __init__(self,
                 name: str,
                 attack: int,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool):
      
        super().__init__(name, description, attack)
      
        self.name = name
        self.attack = attack
        self.description = description
        self.fill_volume = fill_volume
        self.weight = weight
        self.carry_able = carry_able
        
        # The amount of space an Item takes up
       
        # self.enchantments = [list of enchantments] ?

'''
class Item(object):

    """
    Items are Things that are potentially carry-able or interactive in some way,
    either by the player or a Creature of some kind. Items can also be set as
    an immovable scenery object by setting their carry_able attribute to False.
    """
    
    def __init__(self,
                 name: str,
                 attack: int,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool):

        self.name = name
        self.attack = attack
        self.description = description
        self.fill_volume = fill_volume
        self.weight = weight
        self.carry_able = carry_able


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def print_items(self):
        print('\t'.join(['Name', 'Atk', 'Desc', 'Vol', 'Wei', 'CA']))
        for item in self.items.values():
            print('\t'.join([str(x) for x in [item.name, item.attack, item.description, item.fill_volume, item.weight, item.carry_able]]))


inventory = Inventory()
inventory.add_item(Item('Sword', 5, 'Bad', 5.0, 5.0, True))
inventory.print_items()
