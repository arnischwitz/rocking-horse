# creep.py
#
#
#
# ARN 1-26-19


import threading


class Creep:

    def __init__(self):
        pass

    def act(self):
        pass
        # random method

    def jump(self, room):
        room.add_to_contents(self)

    def whisper(self, msg):
        print(msg)
