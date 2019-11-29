

class LootsInventory:
    """Content of loots_inventory is permanent for Monster class but always temporary for Hero class"""
    def __init__(self, loots_inventory):
        self.loots_inventory = loots_inventory

    def add_loots(self, loots):
        """Add all loots to itself"""
        self.loots_inventory = loots
