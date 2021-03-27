import unittest
from src.m21 import M21


class Test_M21_Index(unittest.TestCase):

    def setUp(self):
        self.m21 = M21()

    def test_setIndex(self):
        self.m21.setIndex('test')
        self.assertEqual(self.m21.getIndex(), 'test')

    def test_unsetIndex(self):
        self.m21.unsetIndex()
        self.assertEqual(self.m21.getIndex(), None)

    def tearDown(self):
        self.m21 = None
