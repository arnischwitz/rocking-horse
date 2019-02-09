# room.py
#
# Room class, these are the building blocks of all folders in the game. They contain all other objects
#
# ARN 1-25-19


class Room:

    kind = 'ROOM'

    def __init__(self, name, parent_room):
        self.name = name
        self.parent_room = parent_room

        self.contents = []
        self.connected_rooms = {}

        if self.parent_room is not None:
            self.connected_rooms[self.parent_room.get_name()] = self.parent_room
            self.parent_room.add_connected_room(self)

    def __del__(self):
        pass

    def get_name(self):
        return self.name

    def get_contents(self):
        return self.contents

    def add_to_contents(self, new_item):
        self.contents.append(new_item)

    def rem_from_contents(self, old_item):
        if old_item in self.contents:
            self.contents.remove(old_item)

    def add_connected_room(self, new_room):
        if new_room not in self.connected_rooms:
            self.connected_rooms[new_room.get_name()] = new_room

    def rem_connected_room(self, old_room):
        if old_room.get_name() in self.connected_rooms:
            del self.connected_rooms[old_room.get_name()]

    def get_connected_rooms(self):
        return self.connected_rooms
