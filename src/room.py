# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def add_items_to_room(self, item):
        self.items.append(item)

    def get_items_from_room(self, item):
        return getattr(self.item)