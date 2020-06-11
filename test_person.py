import unittest
from person import Person

# TODO
class TestPerson(unittest.TestCase):

    def setUp(self):
        print('Test start.')
        self.p1 = Person('Bill', 'Gates', 15)
        self.p2 = Person('Steve', 'Jobs', 25)
