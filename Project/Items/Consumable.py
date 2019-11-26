

class Consumable:
    def __init__(self, property_type, property_value):
        # can be restore_life_points, restore_mana_points, direct_damages
        self.property_type = property_type
        self.property_value = property_value
