import unittest
from src.m21 import M21


class Test_M21(unittest.TestCase):

    def setUp(self):
        self.m21 = M21()

    def test_setStream_composer(self):
        self.m21.setSearch()
        self.m21.setComposer('test')
        self.m21.setStream(self.m21.getComposer())
        self.assertEqual(self.m21.getStream(), self.m21.getComposer())
        self.assertEqual(self.m21.getStream(), 'test')

    def test_unsetStream_composer(self):
        self.m21.unsetSearch()
        self.m21.unsetStream()
        self.m21.unsetComposer()
        self.assertEqual(self.m21.getSearch(), False)
        self.assertEqual(self.m21.getComposer(), None)
        self.assertEqual(self.m21.getStream(), None)

    def test_setStream_index(self):
        self.m21.setSearch()
        self.m21.setIndex('test')
        self.m21.setStream(self.m21.getIndex())
        self.assertEqual(self.m21.getStream(), self.m21.getIndex())
        self.assertEqual(self.m21.getStream(), 'test')

    def test_unsetStream_index(self):
        self.m21.unsetSearch()
        self.m21.unsetStream()
        self.m21.unsetIndex()
        self.assertEqual(self.m21.getSearch(), False)
        self.assertEqual(self.m21.getIndex(), None)
        self.assertEqual(self.m21.getStream(), None)

    def test_setStream_composer_index(self):
        self.m21.setSearch()
        self.m21.setComposer('test')
        self.m21.setIndex('test')
        self.m21.setStream("{}/{}".format(
            self.m21.getComposer(),
            self.m21.getIndex())
        )
        self.assertEqual(
            self.m21.getStream(),
            "{}/{}".format(self.m21.getComposer(), self.m21.getIndex())
        )
        self.assertEqual(self.m21.getStream(), "test/test")

    def test_unsetStream_from_unsetSearch(self):
        self.m21.unsetSearch()
        self.assertEqual(self.m21.getStream(), None)
