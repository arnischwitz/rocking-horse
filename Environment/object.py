# object.py
#
# Object class: abstract objects that player puts in rooms
#
# ARN 1-25-19


class Object:

    kind = 'OBJECT'

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
