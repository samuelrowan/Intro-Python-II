# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, stuff = []):
        self.name = name
        self.current_room = current_room
        self.stuff = stuff

    def __repr__(self):
        return f"{self.stuff}"

    def grab(self, item):
        self.stuff.append(item)
        print(f'You have {self.stuff}')

#__str__ inteded to be human readable
#__repr__ explicit for development

