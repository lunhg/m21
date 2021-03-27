import unittest
from src.m21 import M21


class Test_M21_Commit(unittest.TestCase):

    def setUp(self):
        self.m21 = M21()

    def test_commitSearch_composer(self):
        self.m21.setSearch()
        self.m21.setComposer('bach')
        self.m21.commitSearch()
        self.assertEqual(self.m21.getSearch(), True)
        self.assertEqual(self.m21.getComposer(), 'bach')
        self.assertEqual(self.m21.getStream(), 'bach')
        self.assertEqual(self.m21.getStream(),  self.m21.getComposer())

    def test_uncommitSearch_composer(self):
        self.m21.uncommitSearch()
        self.assertEqual(self.m21.getSearch(), False)
        self.assertEqual(self.m21.getComposer(), None)
        self.assertEqual(self.m21.getStream(), None)
        self.assertEqual(self.m21.getStream(),  self.m21.getComposer())

    def test_commitSearch_index(self):
        self.m21.setSearch()
        self.m21.setIndex('bwv1')
        self.m21.commitSearch()
        self.assertEqual(self.m21.getSearch(), True)
        self.assertEqual(self.m21.getIndex(), 'bwv1')
        self.assertEqual(self.m21.getStream(), 'bwv1')
        self.assertEqual(self.m21.getStream(),  self.m21.getIndex())

    def test_uncommitSearch_index(self):
        self.m21.uncommitSearch()
        self.assertEqual(self.m21.getSearch(), False)
        self.assertEqual(self.m21.getIndex(), None)
        self.assertEqual(self.m21.getStream(), None)

    def test_commitSearch_composer_index(self):
        self.m21.setSearch()
        self.m21.setComposer('bach')
        self.m21.setIndex('bwv1')
        self.m21.commitSearch()
        self.assertEqual(self.m21.getSearch(), True)
        self.assertEqual(self.m21.getComposer(), 'bach')
        self.assertEqual(self.m21.getIndex(), 'bwv1')
        self.assertEqual(self.m21.getStream(), 'bach/bwv1')
        self.assertEqual(self.m21.getStream(),  "{}/{}".format(
            self.m21.getComposer(),
            self.m21.getIndex()
        ))

    def test_uncommitSearch_composer_index(self):
        self.m21.uncommitSearch()
        self.assertEqual(self.m21.getSearch(), False)
        self.assertEqual(self.m21.getComposer(), None)
        self.assertEqual(self.m21.getIndex(), None)
        self.assertEqual(self.m21.getStream(), None)
if (__name__ == '__main__'):
    unittest.main()
