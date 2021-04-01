import unittest
from src.m21 import M21


class Test_M21(unittest.TestCase):

    def setUp(self):
        self.m21 = M21()

    def testInicialization(self):
        self.assertEqual(self.m21.getStream(), None)
        self.assertEqual(self.m21.getNamespace(), None)

    def tearDown(self):
        self.m21 = None
