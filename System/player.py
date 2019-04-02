# player.py
#
# Class for player control functionality
#
# ARN 1-25-19


from Environment import object, room


class Player:

    def __init__(self, start_room, world):
        self.cmd_str = ''
        self.current_room = start_room
        self.game_world = world

        self.commands = ['look', 'move', 'create', 'destroy', 'quit', 'what', 'command_list', 'target_list', 'help']
        self.targets = ['room', 'object']

    # Read user input and prepare to process
    def read_input(self, user_input):
        self.cmd_str = user_input.lower().split()

        if len(self.cmd_str) <= 0:
            print('that is not a command, enter a valid command')

        elif len(self.cmd_str) == 1:
            if self.cmd_str[0] == 'command_list' or self.cmd_str[0] == 'target_list' or self.cmd_str[0] == 'quit':
                cmd_to_call = getattr(self, self.cmd_str[0])
                cmd_to_call()
            else:
                print('pick a valid target')

        elif self.cmd_str[0] in self.commands:
            if self.cmd_str[1] in self.targets:
                cmd_to_call = getattr(self, self.cmd_str[0])
                cmd_to_call()

            else:
                print('could not discern target')

        else:
            print('could not issue command')

        self.reset_input()

    def reset_input(self):
        self.cmd_str = ''

    def set_current_room(self, new_room):
        self.current_room = new_room

    def get_current_room(self):
        return self.current_room

    # Command functions
    def look(self):
        if self.cmd_str[1] == 'room':
            print('room: ' + self.current_room.get_name())
            print('connected rooms: ')
            for rm in self.current_room.get_connected_rooms():
                print(rm)

        elif self.cmd_str[1] == 'object':
            for obj in self.current_room.get_contents():
                if obj.get_name() == self.cmd_str[2]:
                    print('object: ' + obj.get_name())
                    print('info: ' + ' '.join(obj.get_description()))

        else:
            print('you see nothing')

    def move(self):
        if self.cmd_str[2] in self.current_room.get_connected_rooms():
            self.set_current_room(self.game_world.get_room_map().get(self.cmd_str[2]))
            print('you move to ' + self.current_room.get_name())

        else:
            print('you can not move')

    def create(self):
        if self.cmd_str[1] == 'room' and len(self.cmd_str) == 3:
            self.game_world.add_room(room.Room(self.cmd_str[2], self.current_room))
            print('created ' + self.cmd_str[2])

        elif self.cmd_str[1] == 'object':
            self.current_room.add_to_contents(object.Object(self.cmd_str[2], self.cmd_str[3:]))
            print('created ' + self.cmd_str[2])

        else:
            print('could not birth ' + self.cmd_str[1])

    def destroy(self):
        if self.cmd_str[1] == 'room':
            self.game_world.remove_room(self.game_world.get_room_map().get(self.cmd_str[2]))
            print('destroyed ' + self.cmd_str[1])

        elif self.cmd_str[1] == 'object':
            for obj in self.get_current_room().get_contents():
                if obj.get_name() == self.cmd_str[2]:
                    self.get_current_room().rem_from_contents(obj)

        else:
            print('could not obliviate ' + self.cmd_str[1])

    def what(self):
        if self.cmd_str[1] == 'room':
            print('room: ' + self.current_room.get_name())
            print('objects in room: ')
            for obj in self.current_room.get_contents():
                    print(obj.get_name())

    def quit(self):
        self.game_world.set_game_running(False)

    def command_list(self):
        print(' - '.join(self.commands) + '\n')

    def target_list(self):
        print(' - '.join(self.targets) + '\n')

    def help(self):
        print('type the name of the command or target you need help with (or \'all\' for all): ', end=' ')
        option = input().lower()

        if option == 'look':
            print('use this command to learn information about the target')
            print('look room [room name]')
            print('look object [object name]')

        elif option == 'move':
            print('use this command move between connected rooms')
            print('move room [room name]')

        elif option == 'create':
            print('use this command to create targets')
            print('create room [room name] [room size - How many objects can this room hold? (0-10)]')
            print('create object [object name] [object description]')

        elif option == 'destroy':
            print('use this command to destroy targets')
            print('destroy room [room name]')
            print('destroy object [object name]')

        elif option == 'quit':
            print('you can use this command to try and quit the game')
            print('quit')

        elif option == 'help':
            print('there is no home for you here now go away')

        elif option == 'what':
            print('use this command when you forget the room name or the objects in the room')
            print('what room')

        elif option == 'command_list':
            print('brings up a list of commands')
            print('command_list')

        elif option == 'target_list':
            print('brings up a list of targets')
            print('target_list')

        elif option == 'room':
            print('will aim a command at a room')
            print('[command] room [room name]')

        elif option == 'object':
            print('will aim a command at an object')
            print('[command] object [object name] [object description]')

        elif option == 'all':
            print('i changed my mind')

        else:
            print('not a command or target')