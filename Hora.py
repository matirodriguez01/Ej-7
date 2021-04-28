class Hora:
    __hor = 0
    __min = 0
    __seg = 0

    def __init__(self, hor = 0, min = 0, seg = 0):
        self.__hor = hor
        self.__min = min
        self.__seg = seg

    def getHora(self):
        return self.__hor

    def getMin(self):
        return self.__min

    def getSeg(self):
        return self.__seg

    def Mostrar(self):
        return print(f"HORA:{self.__hor}:{self.__min}:{self.__seg}")

    def __radd__(self, x):
            return Hora(self.__hor + x.gethora(), self.__min + x.getminutos(), self.__seg + x.getsegundos())

