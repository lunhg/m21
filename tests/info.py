import unittest
from src.info import Info
from src.m21 import M21


class Test_M21_Info(unittest.TestCase):

    def testName(self):
        self.assertEqual(Info.getName(), M21.NAME)

    def testVersion(self):
        self.assertEqual(Info.getVersion(), M21.VERSION)

    def testDescription(self):
        self.assertEqual(Info.getDescription(), M21.DESCRIPTION)


if (__name__ == '__main__'):
    unittest.main()
