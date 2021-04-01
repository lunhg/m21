from src.command import Command
from music21 import corpus


class Search(Command):

    def __init__(self, parser):
        super().__init__(
            parser=parser,
            title='search',
            description='search for entries in music21 corpus',
            help='search for entries in music21 corpus',
            options=corpus.manager.listSearchFields()
        )

    def build(self):
        for word in self.getOptions():
            self.getCommand().add_argument(
                "--{}".format(word),
                help="search for entries with {} predicate".format(word),
                action=None,
                dest=word,
                default=False
            )
