from argparse import ArgumentParser
from src.m21 import M21
from src.search import Search


class Cli(M21):
    """A class to define the command line interface for music21.
    This class inherits the properties and methods from M21 and add
    functionality to it in command line.

    Three main methods are used:
        - Cli.build: a static method that build a OptionParser from properties
        - parse: a instance method that parses all options given in Cli.build
        - run: run the OptionParser
    """
    def __init__(self):
        super().__init__()
        self.__parser__ = None
        self.__subparser__ = None
        self.__subcommands__ = None
        self.__arguments__ = None

    def getParser(self):
        return self.__parser__

    def getSubparser(self):
        return self.__subparser__

    def getSubcommands(self):
        return self.__subcommands__

    def getArguments(self):
        return self.__arguments__

    def buildParser(self):
        self.__parser__ = ArgumentParser(
            prog=M21.NAME,
            description=M21.DESCRIPTION
        )

        self.__subparser__ = self.__parser__.add_subparsers(
            title='subcommands',
            description='valid subcommands',
            dest='subcommand'
        )

    def buildVersion(self):
        self.__parser__.add_argument(
            '-v',
            '--version',
            action='version',
            version=M21.VERSION
        )

    def buildSubcommand(self, Command):
        command = Command()
        command.addToSubparser(self.__subparser__)

    def addSubcommandArguments(self, subcommand, options):
        v = "_".join(options[1].split("-"))
        a = "-%s" % options[0]
        b = "--%s" % options[1]
        if options[2] is not None:
            subcommand.add_argument(a,
                                    b,
                                    action=options[2],
                                    help=options[3],
                                    dest=v,
                                    default=False)

        elif options[1] == "measures":
            subcommand.add_argument(a,
                                    b,
                                    action=options[2],
                                    help=options[3],
                                    dest=v,
                                    default=False,
                                    nargs=2)
        else:
            subcommand.add_argument(a,
                                    b,
                                    help=options[3],
                                    dest=v,
                                    default=False)

    def parse(self, args):
        print(args)
        if(len(args) >0):
            self.__arguments__ = self.__parser__.parse_args(args)
        else:
            self.__arguments__ = self.__parser__.parse_args()

    def execute(self):
        if (self.__arguments__ is not None and self.__arguments__.subcommand == 'search'):

            self.setSearch()
            if (self.__arguments__.composer):
                self.setComposer(self.__arguments__.composer)

            if (self.__arguments__.index):
                self.setIndex(self.__arguments__.index)

            self.commitSearch()
            self.fetchSearch()

    def print(self):
        if (self.__arguments__ is not None and self.__arguments__.subcommand == 'search'):
            print(self.getStream())

    @staticmethod
    def build(*args):
        cli = Cli()

        # build defaults
        cli.buildParser()
        cli.buildVersion()

        # add subcommands
        for klass in args:
            cli.buildSubcommand(klass)

        return cli


if (__name__ == '__main__'):
    cli = Cli.build(Search)
    cli.parse()
    cli.execute()
    cli.print()
