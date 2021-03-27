import unittest
from src.m21 import M21


class Test_M21_Fetch(unittest.TestCase):

    def setUp(self):
        self.m21 = M21()

    def test_fetchSearch_Exception(self):
        self.m21.setSearch()
        self.m21.commitSearch()
        self.assertRaises(Exception, self.m21.fetchSearch)
        self.m21.uncommitSearch()

    def test_fetchSearch_composer(self):
        self.m21.setSearch()
        self.m21.setComposer('bach')
        self.m21.commitSearch()
        self.m21.fetchSearch()
        self.assertIsInstance(self.m21.getStream(), list)
        self.assertNotEqual(len(self.m21.getStream()), 0)
        self.m21.uncommitSearch()

    def test_fetchSearch_index(self):
        self.m21.setSearch()
        self.m21.setIndex('bwv1')
        self.m21.commitSearch()
        self.m21.fetchSearch()
        self.assertIsInstance(self.m21.getStream(), list)
        self.assertNotEqual(len(self.m21.getStream()), 0)
        self.m21.uncommitSearch()

    def test_fetchSearch_composer_index(self):
        self.m21.setSearch()
        self.m21.setComposer('bach')
        self.m21.setIndex('bwv1')
        self.m21.commitSearch()
        self.m21.fetchSearch()
        self.assertIsInstance(self.m21.getStream(), list)
        self.assertNotEqual(len(self.m21.getStream()), 0)
        self.m21.uncommitSearch()

    def test_fetchSearch_composer_index_zero_length(self):
        self.m21.setSearch()
        self.m21.setComposer('test')
        self.m21.setIndex('test')
        self.m21.commitSearch()
        self.m21.fetchSearch()
        self.assertIsInstance(self.m21.getStream(), list)
        self.assertEqual(len(self.m21.getStream()), 0)
        self.m21.uncommitSearch()
