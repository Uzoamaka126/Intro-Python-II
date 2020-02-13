from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "sheath"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "sword"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "bread"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "torch"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "water"),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
destinations = ["n", "s", "w", "e"]
items = ["sword", "sheath", "water", "bread", "flag"]

from player import Player
# create a starting room
starting_room = room['outside']
direction = input("enter direction")

# Make a new player object that is currently in the 'outside' room.
default_player = Player('one', starting_room, 'sword')

# Write a loop that:
while True:

# * Prints the current room name
    def get_user_current_room():
        print(default_player.room)
# * Prints the current description (the textwrap module might be useful here).
    
# * Waits for user input and decides what to do.
    def get_user_input():
        user = input("Where do you want to go now:")
        user = user.split(" ")
        print(user)
        return user
# If the user enters a cardinal direction, attempt to move to the room there.
    if(default_player.room)

# Print an error message if the movement isn't allowed.

def set_room_details(room):
    print("Error")
    print(f"You went: {direction}")
    print(f"You are currently in: {default_player.room.name}")
    print(room.description)
    # Make the room be able to hold multiple items
    if len(room.inventory == 0):
        print("Sorry, there are no items!")
    else:
        for item in room.inventories:
            print(f"Here, have this item: {item}")
    

# If the user enters "q", quit the game.
