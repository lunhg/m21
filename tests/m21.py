import unittest
from src.m21 import M21


class Test_M21(unittest.TestCase):

    def setUp(self):
        self.m21 = M21()

    def testUnsetStream_from_unsetSearch(self):
        self.m21.unsetSearch()
        self.assertEqual(self.m21.getStream(), None)

    def testCommitSearch_composer(self):
        self.m21.setSearch()
        self.m21.setComposer('bach')
        self.m21.commitSearch()
        self.assertEqual(self.m21.getSearch(), True)
        self.assertEqual(self.m21.getComposer(), 'bach')
        self.assertEqual(self.m21.getStream(), 'bach')
        self.assertEqual(self.m21.getStream(),  self.m21.getComposer())

    def testUncommitSearch_composer(self):
        self.m21.uncommitSearch()
        self.assertEqual(self.m21.getSearch(), False)
        self.assertEqual(self.m21.getComposer(), None)
        self.assertEqual(self.m21.getStream(), None)
        self.assertEqual(self.m21.getStream(),  self.m21.getComposer())

    def testCommitSearch_index(self):
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

    def test_pushSearch_Exception(self):
        self.m21.setSearch()
        self.m21.commitSearch()
        self.assertRaises(Exception, self.m21.pushSearch)
        self.m21.uncommitSearch()

    def test_pushSearch_composer(self):
        self.m21.setSearch()
        self.m21.setComposer('bach')
        self.m21.commitSearch()
        self.m21.pushSearch()
        self.assertIsInstance(self.m21.getStream(), list)
        self.assertNotEqual(len(self.m21.getStream()), 0)
        self.m21.uncommitSearch()

    def test_pushSearch_index(self):
        self.m21.setSearch()
        self.m21.setIndex('bwv1')
        self.m21.commitSearch()
        self.m21.pushSearch()
        self.assertIsInstance(self.m21.getStream(), list)
        self.assertNotEqual(len(self.m21.getStream()), 0)
        self.m21.uncommitSearch()

    def test_pushSearch_composer_index(self):
        self.m21.setSearch()
        self.m21.setComposer('bach')
        self.m21.setIndex('bwv1')
        self.m21.commitSearch()
        self.m21.pushSearch()
        self.assertIsInstance(self.m21.getStream(), list)
        self.assertNotEqual(len(self.m21.getStream()), 0)
        self.m21.uncommitSearch()

    def test_pushSearch_composer_index_zero_length(self):
        self.m21.setSearch()
        self.m21.setComposer('test')
        self.m21.setIndex('test')
        self.m21.commitSearch()
        self.m21.pushSearch()
        self.assertIsInstance(self.m21.getStream(), list)
        self.assertEqual(len(self.m21.getStream()), 0)
        self.m21.uncommitSearch()

if (__name__ == '__main__'):
    unittest.main()
