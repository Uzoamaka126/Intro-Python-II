# Implement a class to hold room information. This should have name and
# description attributes.''
class Room:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.inventory = inventory

    def add_items(self, item):
        self.inventory.append(item)



        


# hasattr(current_location, 'n_to')
# hasattr(current_location, 's_to')
# hasattr(current_location, 'e_to')
# hasattr(current_location, 'w_to')