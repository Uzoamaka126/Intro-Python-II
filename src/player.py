# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player:
    def __init__(self, name, room, inventory):
        self.name = name
        self.room = room
        self.inventory = inventory

        def getCurrentRoom(self, room):
            self.room = room

        def add_inventory_item(self, item):
            self.inventory.append(item)