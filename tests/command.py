import unittest
from argparse import ArgumentParser
from src.command import Command

class It(Command):
    """It class is a test class derivated
    from Command to test it functionality"""

    def __init__(self, parser):
        super().__init__(
            parser=parser,
            title='it',
            description='it test subcommand',
            help='it test subcommand',
            options=['option']
        )

    def build(self):
        for word in self.getOptions():
            self.__command__.add_argument(
                "-{}".format(word[0]),
                "--{}".format(word),
                action=None,
                dest=word,
                default=False
            )

class Test_M21_Command(unittest.TestCase):

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

        it = It(subparser)
        it.build()

    def test_it_raises_invalid_long_option(self):
        self.assertRaises(
            SystemExit,
            self.parser.parse_args,
            ['it', '--is', 'invalid_option']
        )

    def test_it_raises_invalid_short_option(self):
        self.assertRaises(
            SystemExit,
            self.parser.parse_args,
            ['it', '-i', 'invalid_option']
        )

    def test_it_long_option(self):
        res = self.parser.parse_args(['it', '--option', 'value'])
        self.assertEqual(res.subcommand, 'it')
        self.assertEqual(res.option, 'value')

    def test_it_short_option(self):
        res = self.parser.parse_args(['it', '-o', 'value'])
        self.assertEqual(res.subcommand, 'it')
        self.assertEqual(res.option, 'value')

    def tearDown(self):
        self.parser = None
