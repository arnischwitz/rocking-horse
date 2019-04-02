# main.py
#
# main file for testing purposes
#
# ARN 1-25-19

from Environment import object, room
from Extras import overlord
from System import player, world


def run_introduction():
    print('\n\nWelcome to your new \\Home\n')
    print('I made this file system just for you\n\n')

    print('These commands are available to you (bring up by typing >> command_list)\n')
    print('help - look - what - move - create - destroy - quit\n\n')

    print('These targets are available to you (bring up by typing >> target_list)\n')
    print('room - object\n\n')

    print('Format as follows\n')
    print('command target name argument\n\n')

    print('Have fun in your new \\Home\n')


def construct(home):
    # base home construction
    foyer = room.Room('foyer', home)
    game_world.add_room(foyer)
    foyer.add_to_contents(object.Object('lamp', 'the lamp shines dimly'))
    foyer.add_to_contents(object.Object('coat_rack', 'the rack stands firm'))

    dining = room.Room('dining_room', foyer)
    game_world.add_room(dining)
    dining.add_to_contents(object.Object('table', 'the table has food on it. the food is cold'))
    dining.add_to_contents(object.Object('chair', 'made for sitting'))
    dining.add_to_contents(object.Object('broken_chair', 'too much sitting'))

    hall = room.Room('hallway', foyer)
    game_world.add_room(hall)
    hall.add_to_contents(object.Object('closet', 'storage for coats and misc crap. you hear nothing inside'))

    office = room.Room('office', foyer)
    game_world.add_room(office)
    office.add_to_contents(object.Object('desk', 'power emanates from the desk'))
    office.add_to_contents(object.Object('filing_cabinet', 'filled to the brim with documents. tax documents make up most of the papers'))
    office.add_to_contents(object.Object('piano', 'you press a piano key. it is soft and sweet, but out of tune'))

    kitchen = room.Room('kitchen', hall)
    game_world.add_room(kitchen)
    kitchen.add_to_contents(object.Object('table', 'a small table, scratched by years of use'))
    kitchen.add_to_contents(object.Object('countertop', 'the countertop is lightly covered by dust, dishes, and old mail'))

    kitchen.add_connected_room(dining)
    kitchen.add_connected_room(office)

    dining.add_connected_room(kitchen)
    office.add_connected_room(kitchen)

    upstairs = room.Room('upstairs', foyer)
    game_world.add_room(upstairs)

    downstairs = room.Room('downstairs', kitchen)
    game_world.add_room(downstairs)

    basement = room.Room('basement', downstairs)
    game_world.add_room(basement)


if __name__ == '__main__':
    # create home and game world
    root_home = room.Room('home', None)
    game_world = world.World(root_home)

    # construct home
    construct(root_home)

    # create player and such
    victim = player.Player(root_home, game_world)
    god = overlord.Overlord(game_world)

    # start game
    run_introduction()
    game_world.game_running = True

    cmdline = '[\\Home]:'

    ticker = 0

    while game_world.game_running:
        print(cmdline, end=' ')
        victim.read_input(input())

        if ticker > 5:
            cmdline = god.update()
            ticker = 0

        ticker += 1
