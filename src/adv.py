from room import Room
import random
from item import Item
from player import Player

# Declare all the rooms
stuff = {
    'thing': Item("thing", "it's a thing... It must do..... something?"),
    'sword': Item("sword", "a chunk of sharp metal"),
    'grenade': Item("holy hand grenade of antioch", "does what it says on the tin"),
    'gun_blade': Item("gun blade", "idk it's a gun and a sword... what do you want?"),
    'greater': Item("greater healing potion", "It heals you for 4d4 whatever that means in this context.. \
    \nAlso, I don't know what it's greater than because it is the only potion in this game.")
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", stuff[random.choice(list(stuff.keys()))]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", stuff[random.choice(list(stuff.keys()))]),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", stuff[random.choice(list(stuff.keys()))]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", stuff[random.choice(list(stuff.keys()))]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", stuff[random.choice(list(stuff.keys()))]),
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
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Link Cable", room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def room_logic(dir):
    letter = None
    if dir == "":
        pass
    elif dir == "grab":
        new_player.grab(new_player.current_room.stuff)
        letter = None
    else:
        letter = dir + '_to'
        print(letter)
        if not getattr(new_player.current_room, letter):
            print("There's nothing here! I'll head back!")
        else:
            new_player.current_room = getattr(new_player.current_room, letter)
player_input = ""
while player_input != 'q':
    player_input = input("Where would you like to go? (n/s/e/w or q to exit)")
    print(new_player.current_room.name)
    print(new_player.current_room.description)
    print(f"You see something on the ground.  It looks like it's a... a... {new_player.current_room.stuff.name}?  \n{new_player.current_room.stuff.description}")
    room_logic(player_input)
    player_input = new_player.current_room
print("thanks for playing")