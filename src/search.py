import src.options as options


class Search(object):

    def __init__(self):
        super().__init__()
        self.title = 'search'
        self.description = 'search for entries in music21 corpus'
        self.help = 'search for entries in music21 corpus'
        self.arguments = ['composer', 'index']

    def addToSubparser(self, subparser):
        subcommand = subparser.add_parser(
            self.title,
            description=self.description,
            help=self.help
        )

        for a in self.arguments:
            for key, val in options.__dict__.items():
                if (key == a):
                    self.__addArgument__(subcommand, val)
                else:
                    continue

    def __addArgument__(self, subcommand, lst):
        v = "_".join(lst[1].split("-"))
        a = "-%s" % lst[0]
        b = "--%s" % lst[1]
        subcommand.add_argument(a,
                                b,
                                action=lst[2],
                                help=lst[3],
                                dest=v,
                                default=False)
