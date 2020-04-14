# Implement a class to hold room information. This should have name and description attributes.

class Room:
    def __init__(self, name, items, description, n_to, s_to, e_to, w_to):        
        self.name = name
        self.description = description
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def add_items_to_room(self, item):
        self.items.append(item)

    # def get_items_from_room(self, item):
    #     return getattr(self.items)