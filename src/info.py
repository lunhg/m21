class Info(object):

    @staticmethod
    def getName():
        return "m21"

    @staticmethod
    def getVersion():
        return "0.0.1"

    @staticmethod
    def getDescription():
        return "\n".join([
            "Tool build on top of music21 library",
            "for automation on some automated tasks",
            "in computer assisted musicology and composition"
        ])

    @staticmethod
    def getAuthors():
        return {
            "lunhg": "lunhg@github"
        }
