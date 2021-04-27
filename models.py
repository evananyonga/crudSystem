# import _json


class Person(object):
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    # returns someone's name
    def name(self):
        return "%s %s" % (self.first_name, self.last_name)