import unittest
from person import Person

# TODO
class TestPerson(unittest.TestCase):

    def setUp(self):
        print('Test start.')
        self.p1 = Person('Bill', 'Gates', 15)
        self.p2 = Person('Steve', 'Jobs', 25)

    def test_get_full_name(self):
        self.assertEqual(self.p1.get_full_name(), 'Bill Gates')
        self.assertEqual(self.p2.get_full_name(), 'Steve Jobs')
