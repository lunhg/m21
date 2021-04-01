class Command(object):
    """A superclass to be implemented as command.
    The inherited classes should implement:
        - the `build` method, where it should define:
            - short and long options (*args)
            - action, help, dest, default (**kwargs)
            - in the end add:
            - self.command.add_argument(*args, **kwargs)
        - the `exec` method, where it should:"""

    def __init__(self, **kwargs):
        self.__parser__ = kwargs.get('parser')
        self.__options__ = kwargs.get('options')
        self.__command__ = self.__parser__.add_parser(
            kwargs.get('title'),
            description=kwargs.get('description'),
            help=kwargs.get('help')
        )

    def getParser(self):
        return self.__parser__

    def getCommand(self):
        return self.__command__

    def getOptions(self):
        return self.__options__
