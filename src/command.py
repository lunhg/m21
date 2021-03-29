import src.options as options


class Command(object):

    def __init__(self, **kwargs):
        self.parser = kwargs.get('parser')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.help = kwargs.get('help')
        self.arguments = kwargs.get('arguments')
        self.command = self.parser.add_parser(
            self.title,
            description=self.description,
            help=self.help
        )

    def yieldArguments(self):
        for a in self.arguments:
            for key, val in options.__dict__.items():
                if(key == a):
                    yield val

    def build(self):
        for listArgs in self.yieldArguments():
            self.__build__(listArgs)
