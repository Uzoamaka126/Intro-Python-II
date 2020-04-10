from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
# setting the properties of the room
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# print(room['outside'].n_to)
choices = ["n", "s", "w", "e"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player("Wanderer", room["outside"])

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# only the room that the new player is in
# get knife  
# #drop potato 
# ["get", "knife"]
#  input = input("fromplayer") 
# input[0] is it a direction
#  or is it get,
#  or is it drop ["n"] 
# this is direction 
# change player room 
 


def get_user_input():
    user = input("Okay, what do you want to do next:")
    user = user.split(" ")
    return user

# take current room and assign it to the new room

def get_room_details(room):
    print(f"you are currently in {room.name}")
    print(f"And it is {room.description}")
    if 
while True:
    print(newPlayer.current_room.name, newPlayer.current_room.description)
    get_user_input();