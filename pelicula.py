
class Pelicula:
    __titulo:str
    __resumen:str
    __lenguaje:str
    __fecha:str
    __generos:list
    def __init__(self,titulo,resumen,lenguaje,fecha,generos) -> None:
        self.__titulo=titulo
        self.__resumen=resumen
        self.__lenguaje=lenguaje
        self.__fecha=fecha
        self.__generos=generos
    
    def getTitulo(self):
        return self.__titulo
    def getResumen(self):
        return self.__resumen
    def getLenguaje(self):
        return self.__lenguaje
    def getFecha(self):
        return self.__fecha
    def getGeneros(self):
        return self.__generos
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                titulo=self.__titulo,
                resumen=self.__resumen,
                lenguaje=self.__lenguaje,
                fecha=self.__fecha,
                generos=self.__generos
            )
        )
        return d
    
    def __str__(self) -> str:
        return '%s %s %s %s %s'%(self.__titulo,self.__resumen,self.__lenguaje,self.__fecha,self.__generos)