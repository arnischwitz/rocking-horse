# world.py
#
# Class to track world state and operate on the world map
#
# ARN 1-25-19


import random


class World:

    def __init__(self, root_room):
        self.root_room = root_room

        self.room_map = {self.root_room.get_name(): self.root_room}

        self.game_running = None

    def get_room_map(self):
        return self.room_map

    def add_room(self, new_room):
        if new_room not in self.room_map:
            self.room_map[new_room.get_name()] = new_room
        else:
            return 'There is already a room with that name'

    def remove_room(self, old_room):
        if old_room.get_name() in self.room_map:
            for rm in old_room.get_connected_rooms():
                self.room_map[rm].rem_connected_room(old_room)
            del old_room
        else:
            return 'There is no room with that name'

    def get_rand_room(self):
        return random.choice(list(self.room_map.values()))

    def set_game_running(self, state):
        self.game_running = state
