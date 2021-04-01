import unittest
from src.cli import Cli
from src.search import Search
from music21 import corpus


class Test_M21_Cli(unittest.TestCase):

    def setUp(self):
        self.cli = Cli()

    def test_instantiation(self):
        self.assertEqual(self.cli.getStream(), None)
        self.assertEqual(self.cli.getParser(), None)
        self.assertEqual(self.cli.getNamespace(), None)

    def test_non_existent_option_parse_exception(self):
        self.cli.build()
        self.assertRaises(SystemExit,
                          self.cli.parse,
                          ["--this-command-not-exist"])

    def test_parse_search_subcommand(self):
        self.cli.build(Search)
        for key in corpus.manager.listSearchFields():
            self.cli.parse([
                'search',
                "--{}".format(key),
                'test'
            ])
            self.assertEqual(self.cli.getSubcommand(), 'search')
            self.assertEqual(key in self.cli.getOptions(), True)
            self.assertEqual(self.cli.getOptionValue(key), 'test')

    def test_fetch_search_subcommand(self):
        self.cli.build(Search)
        query = 'asdf78tasifagsbdfjsd'
        for key in corpus.manager.listSearchFields():
            self.cli.parse([
                'search',
                "--{}".format(key),
                query
            ])
            self.cli.fetch()
            self.assertIsInstance(self.cli.getOptionValue(key), dict)
            self.assertEqual(self.cli.getOptionValue(key)['name'], query)
            self.assertEqual(self.cli.getOptionValue(key)['length'], 0)
            self.assertEqual(len(self.cli.getOptionValue(key)['results']), 0)

    def test_fetch_search_subcommand_composer_option(self):
        self.cli.build(Search)
        for composer in ['bach', 'mozart', 'beethoven']:
            self.cli.parse([
                'search',
                "--composer",
                composer
            ])
            self.cli.fetch()
            self.assertIsInstance(self.cli.getOptionValue('composer'), dict)
            self.assertEqual(
                self.cli.getOptionValue('composer')['name'],
                composer
            )
            self.assertNotEqual(
                self.cli.getOptionValue('composer')['length'],
                0
            )
            self.assertIsInstance(
                self.cli.getOptionValue('composer')['results'],
                list
            )
            self.assertNotEqual(
                len(self.cli.getOptionValue('composer')['results']),
                0
            )

    def tearDown(self):
        self.cli = None
