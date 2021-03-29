from src.command import Command


class Search(Command):

    def __init__(self, parser):
        super().__init__(
            parser=parser,
            title='search',
            description='search for entries in music21 corpus',
            help='search for entries in music21 corpus',
            arguments=['composer', 'index']
        )

    def __build__(self, lst):
        v = "_".join(lst[1].split("-"))
        a = "-%s" % lst[0]
        b = "--%s" % lst[1]
        self.command.add_argument(a, b, action=lst[2], help=lst[3], dest=v,
                                  default=False)
