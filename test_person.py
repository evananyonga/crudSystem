from models import Person
import unittest


class TestModels(unittest.TestCase):

    def test_can_retrieve_name(self):
        self.assertEqual("", Person.name('some_name'))
