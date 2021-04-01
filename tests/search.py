import unittest
from argparse import ArgumentParser
from src.search import Search
from music21 import corpus

class Test_M21_Search(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser(
            prog='test',
            description='test command'
        )

        subparser = self.parser.add_subparsers(
            title='subcommand',
            description='test subcommand',
            dest='subcommand'
        )

        search = Search(subparser)
        search.build()

    def test_search_raises_invalid_long_option(self):
        self.assertRaises(
            SystemExit,
            self.parser.parse_args,
            ['search', '--is', 'invalid_option']
        )

    def test_search_options(self):
        for key in corpus.manager.listSearchFields():
            namespace = self.parser.parse_args(['search', "--{}".format(key), 'test'])
            self.assertEqual(namespace.subcommand, 'search')
            self.assertEqual(getattr(namespace, key), 'test')

    def tearDown(self):
        self.parser = None
