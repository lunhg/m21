import unittest
from src.m21 import M21


class Test_M21_Search(unittest.TestCase):

    def setUp(self):
        self.m21 = M21()

    def testSetSearch(self):
        self.m21.setSearch()
        self.assertEqual(self.m21.getSearch(), True)

    def testUnsetSearch(self):
        self.m21.unsetSearch()
        self.assertEqual(self.m21.getSearch(), False)

    def tearDown(self):
        self.m21 = None
