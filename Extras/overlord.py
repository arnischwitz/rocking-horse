# overlord.py
#
#
#
# ARN 1-26-19


from Extras import ghost, creep

import random


class Overlord:

    def __init__(self, world):
        self.game_world = world

        self.cmd_options = ['[\\Home]:', '[\\Home]:', '[\\Home]:', '[\\Home]:', '[\\Home]:', '[\\Home]:',
                            '[\\HOME]:', '[\\HOME]:', '[\\HOME]:', '[\\HOME]:', '[\\HOME]:',
                            '[\\home]:', '[\\home]:', '[\\home]:', '[\\home]:',
                            '[\\H]:', '[\\H]:', '[\\H]:',
                            '[\\h]:', '[\\h]:',
                            '[\\hell]:']

    def update(self):
        new_ghost = ghost.Ghost(self.game_world.get_rand_room(), '~')
        new_ghost.haunt()

        # spawn new creep
        # call act()

        # spawn new ghoul
        # call act()

        return random.choice(self.cmd_options)
