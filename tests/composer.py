import unittest
from src.m21 import M21


class Test_M21_Composer(unittest.TestCase):

    def setUp(self):
        self.m21 = M21()

    def testSetComposer(self):
        self.m21.setComposer('test')
        self.assertEqual(self.m21.getComposer(), 'test')

    def testUnsetComposer(self):
        self.m21.unsetComposer()
        self.assertEqual(self.m21.getComposer(), None)

    def tearDown(self):
        self.m21 = None
