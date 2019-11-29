from Project.Items.Potion import Potion


class Inventory:
    def __init__(self):
        self.inventory = []

    def count_potions(self):
        """Return the number of heal and mana potions"""
        heal_potion_number = 0
        mana_potion_number = 0
        for item in self.inventory:
            if isinstance(item, Potion):
                if item.potion_type == "heal":
                    heal_potion_number += 1
                elif item.potion_type == "mana":
                    mana_potion_number += 1
        return heal_potion_number, mana_potion_number

    def add_item(self, item):
        """Add any item to the inventory"""
        self.inventory.append(item)

    def remove_potion(self, potion_type):
        """Remove heal or mana potion from the inventory"""
        for index in range(len(self.inventory)):
            self_item = self.inventory[index]
            if isinstance(self_item, Potion) and self_item.potion_type == potion_type:
                potion = self.inventory.pop(index)
                return potion
        raise Exception("No potion found")
