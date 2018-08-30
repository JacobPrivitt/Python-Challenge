# THE BELOW COULD BE IMPLEMENTED MORE SIMPLY BY JUST CREATING RangedWeapon OBJECTS WITH APPROPRIATE VALUES
# The trick is to only make as many classes are necessary. If a class wouldn't end up having any new
# attributes (as in variables or functions), it could probably be better implemented through an existing class.
# In this instance, we want to leave specific bow names and types to our JSON data files that we can design later.
"""
class StringBow(RangedWeapon):
    # Really bad bow. Feel free to change these, their kinda just place holders.

    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool = True,
                 effective_range: float = 15.0):
        super().__init__(name, description, fill_volume, weight, carry_able)

        self.name = name
        self.description = description
        self.fill_volume = fill_volume
        self.weight = weight
        self.carry_able = carry_able
        self.effective_range = effective_range

        shortrangebow = StringBow('Feather String Bow', 'Great bow for beggingers',
                                  4.0, 4.0)  # Giving the bow values


class ValkyrieBow(RangedWeapon):
    # Mid-Range Bow. Feel free to change these, their kinda just place holders.

    def __init__(self,
                 name: str,
                 description: str,
                 fill_volume: float,
                 weight: float,
                 carry_able: bool = True,
                 effective_range: float = 25.0):
        super().__init__(name, description, fill_volume, weight, carry_able)

        self.name = name
        self.description = description
        self.fill_volume = fill_volume
        self.weight = weight
        self.carry_able = carry_able
        self.effective_range = effective_range

        midrangebow = ValkyrieBow('Valkarie Bone Bow', 'Difficult to use, but very deadly',
                                  6.0, 6.0)
"""
