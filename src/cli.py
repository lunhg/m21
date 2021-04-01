import json
from music21 import corpus
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

    def setParser(self, c):
        self.__parser__ = c

    def getParser(self):
        return self.__parser__

    def getSubcommand(self):
        return self.getNamespace().subcommand

    def getOptions(self):
        return vars(self.getNamespace()).keys()

    def getOptionValue(self, key):
        return getattr(self.getNamespace(), key)

    def setOptionValue(self, key, val):
        return setattr(self.getNamespace(), key, val)

    def build(self, *args):
        parser = ArgumentParser(
            prog=M21.NAME,
            description=M21.DESCRIPTION
        )

        parser.add_argument(
            '-v',
            '--version',
            action='version',
            version=M21.VERSION
        )

        subparser = parser.add_subparsers(
            title='subcommands',
            description='valid subcommands',
            dest='subcommand'
        )

        if (len(args) > 0):
            for Command in args:
                command = Command(subparser)
                command.build()

        self.setParser(parser)

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

    def parse(self, args=None):
        if(args is not None):
            self.setNamespace(self.__parser__.parse_args(args))
        else:
            self.setNamespace(self.__parser__.parse_args())

    def __fetch__(self, command):
        if (self.getSubcommand() == command):
            for key in self.getOptions():
                if (key != 'subcommand'):
                    val = self.getOptionValue(key)
                    if (val):
                        res = {'name': val, 'results': []}
                        for r in corpus.search(val, field=key):
                            __r__ = {
                                'corpus': r.corpusName,
                                'path': r.corpusPath,
                                'metadata':{}
                            }
                            for __k__ in vars(r.metadata).keys():
                                if '_' not in __k__:
                                    __v__ = getattr(r.metadata, __k__)
                                    __r__['metadata'][__k__] = __v__
                            res['results'].append(__r__)
                        res['length'] = len(res['results'])
                        self.setOptionValue(key, res)

    def fetch(self):
        self.__fetch__('search')
