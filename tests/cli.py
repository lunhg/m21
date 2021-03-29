import sys
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
        self.assertEqual(self.cli.getSubcommands(), None)
        self.assertEqual(self.cli.getArguments(), None)

    def test_buildParser(self):
        raised = False
        try:
            self.cli.buildParser()
        except:
            raised = True
        self.assertFalse(raised, 'Cli.buildParser raised Exception')
        self.assertNotEqual(self.cli.getParser(), None)
        self.assertNotEqual(self.cli.getSubparser(), None)


    def test_buildSubcommand_search(self):
        raised = False
        try:
            self.cli.buildParser()
            self.cli.buildSubcommand(Search)
        except:
            raised = True
        self.assertFalse(raised, "Cli.buildSubcommand raised Exception")

    def tearDown(self):
        self.cli = None
