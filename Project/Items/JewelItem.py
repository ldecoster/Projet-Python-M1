from Project.Items.Item import Item


class JewelItem(Item):
    def __init__(self, level):
        super().__init__(level)

    def display_stats(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print("The jewel has no stats to display")
        print("+++++++++++++++++++++++++++++++++++++++++++++")
