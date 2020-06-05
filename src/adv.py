from room import Room

# Declare all the rooms
# using objects, we set the key to an individual name and then the value to an Instance of the Room Class

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
# covers the whole movement that is available for the player. If the movement is available for the player, 
room['outside'].n_to = room['foyer'] #only can move to the north
room['foyer'].s_to = room['outside'] # from the foyer of 
room['foyer'].n_to = room['overlook'] # go forward from foyer to overlook
room['foyer'].e_to = room['narrow'] # From foyer go left  to narrow
room['overlook'].s_to = room['foyer'] # go right from overlook to foyer
room['narrow'].w_to = room['foyer'] # go right to foyer from narrow
room['narrow'].n_to = room['treasure'] # go straight to treasure
room['treasure'].s_to = room['narrow'] # From treasure, go back to narrow


# create a starting room
direction = input("enter direction")

# Make a new player object that is currently in the 'outside' room.
from player import Player
destinations = ["n", "s", "w", "e"]
items = ["sword", "sheath", "water", "bread", "flag"]

# Write a loop that:
while True:

# We would want a welcome message for the user who happens to be currently in the outside room
    starting_room = room['outside']
    default_player = Player('Traveller', starting_room, 'sword')
    print(f"Welcome O brave {default_player}")
    cmd = input('\nChoose n/s/w/e: ')

# Main
# * Prints the current room name  
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

def set_room_details(room):
    print("\n-----------------------------------------")
    print(f"You are currently at the: {default_player.room.name}")
    print(room.description)
    # Make the room be able to hold multiple items
    if len(room.inventory == 0):
        print("Sorry, there are no items!")
    else:
        for item in room.inventories:
            print(f"Here, have this item: {item}")
    

# def get_user_input():
#         user = input("Where do you want to go now:")
#         user = user.split(" ")
#         print(user)
#         return user