import unittest
from src.cli import Cli
from src.search import Search


class Test_M21_Cli(unittest.TestCase):

    def setUp(self):
        self.cli = Cli()

    def test_instantiation(self):
        self.assertEqual(self.cli.getStream(), None)
        self.assertEqual(self.cli.getSearch(), False)
        self.assertEqual(self.cli.getComposer(), None)
        self.assertEqual(self.cli.getIndex(), None)
        self.assertEqual(self.cli.getParser(), None)
        self.assertEqual(self.cli.getSubparser(), None)
        self.assertEqual(self.cli.getArguments(), None)

    def test_simple_build(self):
        self.cli.build()
        self.assertNotEqual(self.cli.getParser(), None)
        self.assertNotEqual(self.cli.getSubparser(), None)
        self.assertEqual(self.cli.getArguments(), None)

    def test_search_build(self):
        self.cli.build(Search)
        self.assertNotEqual(self.cli.getParser(), None)
        self.assertNotEqual(self.cli.getSubparser(), None)
        self.assertEqual(self.cli.getArguments(), None)

    def test_search_parse(self):
        self.cli.build(Search)
        self.cli.parse(['search'])
        self.assertNotEqual(self.cli.getParser(), None)
        self.assertNotEqual(self.cli.getSubparser(), None)
        self.assertNotEqual(self.cli.getArguments(), None)
        self.assertEqual(self.cli.getArguments().subcommand, 'search')

    def test_search_long_composer_option_parse_exception(self):
        self.cli.build(Search)
        self.assertRaises(SystemExit,
                          self.cli.parse,
                          ['search', '--composer'])

    def test_search_short_composer_option_parse_exception(self):
        self.cli.build(Search)
        self.assertRaises(SystemExit,
                          self.cli.parse,
                          ['search', '-c'])

    def test_search_long_index_option_parse_exception(self):
        self.cli.build(Search)
        self.assertRaises(SystemExit,
                          self.cli.parse,
                          ['search', '--index'])

    def test_search_short_index_option_parse_exception(self):
        self.cli.build(Search)
        self.assertRaises(SystemExit,
                          self.cli.parse,
                          ['search', '-i'])

    def test_search_long_composer_and_index_options_parse_exception(self):
        self.cli.build(Search)
        self.assertRaises(SystemExit,
                          self.cli.parse,
                          ['search', '--composer', '--index'])

    def test_search_short_composer_and_index_options_parse_exception(self):
        self.cli.build(Search)
        self.assertRaises(SystemExit,
                          self.cli.parse,
                          ['search', '-c', '-i'])

    def test_search_long_composer_option_parse_success(self):
        self.cli.build(Search)
        self.cli.parse(['search', '--composer', 'test'])
        self.assertNotEqual(self.cli.getParser(), None)
        self.assertNotEqual(self.cli.getSubparser(), None)
        self.assertNotEqual(self.cli.getArguments(), None)
        self.assertEqual(self.cli.getArguments().subcommand, 'search')
        self.assertEqual(self.cli.getArguments().composer, 'test')

    def test_search_short_composer_options_parse_success(self):
        self.cli.build(Search)
        self.cli.parse(['search', '-c', 'test'])
        self.assertNotEqual(self.cli.getParser(), None)
        self.assertNotEqual(self.cli.getSubparser(), None)
        self.assertNotEqual(self.cli.getArguments(), None)
        self.assertEqual(self.cli.getArguments().subcommand, 'search')
        self.assertEqual(self.cli.getArguments().composer, 'test')

    def test_search_long_index_option_parse_success(self):
        self.cli.build(Search)
        self.cli.parse(['search', '--index', 'test'])
        self.assertNotEqual(self.cli.getParser(), None)
        self.assertNotEqual(self.cli.getSubparser(), None)
        self.assertNotEqual(self.cli.getArguments(), None)
        self.assertEqual(self.cli.getArguments().subcommand, 'search')
        self.assertEqual(self.cli.getArguments().index, 'test')

    def test_search_short_index_options_parse_success(self):
        self.cli.build(Search)
        self.cli.parse(['search', '-i', 'test'])
        self.assertNotEqual(self.cli.getParser(), None)
        self.assertNotEqual(self.cli.getSubparser(), None)
        self.assertNotEqual(self.cli.getArguments(), None)
        self.assertEqual(self.cli.getArguments().subcommand, 'search')
        self.assertEqual(self.cli.getArguments().index, 'test')

    def test_search_long_composer_and_index_options_parse_success(self):
        self.cli.build(Search)
        self.cli.parse(['search', '--composer', 'test', '--index', 'test'])
        self.assertNotEqual(self.cli.getParser(), None)
        self.assertNotEqual(self.cli.getSubparser(), None)
        self.assertNotEqual(self.cli.getArguments(), None)
        self.assertEqual(self.cli.getArguments().subcommand, 'search')
        self.assertEqual(self.cli.getArguments().composer, 'test')
        self.assertEqual(self.cli.getArguments().index, 'test')

    def test_search_short_composer_and_index_options_parse_success(self):
        self.cli.build(Search)
        self.cli.parse(['search', '-c', 'test', '-i', 'test'])
        self.assertNotEqual(self.cli.getParser(), None)
        self.assertNotEqual(self.cli.getSubparser(), None)
        self.assertNotEqual(self.cli.getArguments(), None)
        self.assertEqual(self.cli.getArguments().subcommand, 'search')
        self.assertEqual(self.cli.getArguments().composer, 'test')
        self.assertEqual(self.cli.getArguments().index, 'test')


    def tearDown(self):
        self.cli = None
