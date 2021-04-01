from src.info import Info


class M21(object):

    NAME = Info.getName()
    VERSION = Info.getVersion()
    DESCRIPTION = Info.getDescription()

    def __init__(self):
        self.__stream__ = None
        self.__namespace__ = None

    def setStream(self, stream):
        self.__stream__ = stream

    def getStream(self):
        return self.__stream__

    def setNamespace(self, c):
        self.__namespace__ = c

    def getNamespace(self):
        return self.__namespace__
