import music21
from .info import Info


class M21(object):

    NAME = Info.getName()
    VERSION = Info.getVersion()
    DESCRIPTION = Info.getDescription()

    def __init__(self, **kwargs):
        self.__stream__ = None
        self.__search__ = kwargs.get('search') or False
        self.__composer__ = kwargs.get('composer') or None
        self.__index__ = kwargs.get('index') or None
        self.__searchMetadata__ = None
        self.__searchDatas__ = None

    def setStream(self, stream):
        self.__stream__ = stream

    def unsetStream(self):
        self.__stream__ = None

    def getStream(self):
        return self.__stream__

    def getSearch(self):
        return self.__search__

    def setSearch(self):
        self.__search__ = True

    def unsetSearch(self):
        self.__search__ = False

    def setComposer(self, composer):
        self.__composer__ = composer

    def unsetComposer(self):
        self.__composer__ = None

    def getComposer(self):
        return self.__composer__

    def setIndex(self, index):
        self.__index__ = index

    def unsetIndex(self):
        self.__index__ = None

    def getIndex(self):
        return self.__index__

    def commitSearch(self):
        print("=== M21.commitSearch")
        print("search:   {}".format(self.__search__))
        print("composer: {}".format(self.__composer__))
        print("index:    {}".format(self.__index__))

        if(self.__search__):
            if(self.__composer__ and not self.__index__):
                self.__stream__ = self.__composer__

            elif(not self.__composer__ and self.__index__):
                self.__stream__ = self.__index__

            elif(self.__composer__ and self.__index__):
                self.__stream__ = "{}/{}".format(
                    self.__composer__,
                    self.__index__
                )
            else:
                self.__stream__ = None
        else:
            self.__stream__ = None

        print("stream:   {}".format(self.__stream__))

    def uncommitSearch(self):
        self.unsetSearch()
        self.unsetComposer()
        self.unsetIndex()
        self.unsetStream()

    def fetchSearch(self):
        data = music21.corpus.search(self.__stream__)
        self.__stream__ = []
        for d in data:
            self.__stream__.append(d.sourcePath)
