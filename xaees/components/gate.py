from components.appConfig import Config

class Gate:
    def __init__(self):
        self.__config = Config()

    def read(self):
        self.__GateID = self.__config.gateNo()
        return self.__GateID

