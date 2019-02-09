#
#
#
#
#


import random

from Environment.object import Object


class Ghost(Object):

    def __init__(self, room, name, description=''):
        Object.__init__(self, name, description)

        self.room = room

        self.room.add_to_contents(self)

    def move(self, current, target):
        target.add_to_contents(self)
        current.rem_from_contents(self)

    def haunt(self):
        obj = random.choice(self.room.get_contents())
        random.choice(list(self.room.get_connected_rooms().values())).add_to_contents(obj)
        self.room.rem_from_contents(obj)

    def wisk(self, obj, current):
        current.rem_from_contents(obj)

    def empty(self, current):
        for obj in current.get_contents():
            current.rem_from_contents(obj)

    def haunt_full(self, current, target):
        for obj in current.get_contents():
            self.haunt()

    def fill(self, obj, num, current):
        for i in range(num):
            current.add_to_contents(obj)