from argparse import ArgumentParser
from src.m21 import M21


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
        self.__arguments__ = None

    def getParser(self):
        return self.__parser__

    def getSubparser(self):
        return self.__subparser__

    def getArguments(self):
        return self.__arguments__

    def build(self, *args):
        self.__parser__ = ArgumentParser(
            prog=M21.NAME,
            description=M21.DESCRIPTION
        )

        self.__parser__.add_argument(
            '-v',
            '--version',
            action='version',
            version=M21.VERSION
        )

        self.__subparser__ = self.__parser__.add_subparsers(
            title='subcommands',
            description='valid subcommands',
            dest='subcommand'
        )

        if (len(args) > 0):
            for Command in args:
                command = Command(self.__subparser__)
                command.build()

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
        if(len(args) > 0):
            self.__arguments__ = self.__parser__.parse_args(args)
        else:
            self.__arguments__ = self.__parser__.parse_args()
        print(self.__arguments__)

    def execute(self):
        a = self.getArguments()
        if (a is not None and a.subcommand == 'search'):

            self.setSearch()
            if (a.composer):
                self.setComposer(a.composer)

            if (a.index):
                self.setIndex(a.index)

            self.commitSearch()
            self.fetchSearch()

    def print(self):
        a = self.getArguments()
        if (a is not None and a.subcommand == 'search'):
            print(self.getStream())
