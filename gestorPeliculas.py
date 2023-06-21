from pelicula import Pelicula

class GestorPeliculas:
    __indice=0
    __peliculas=None
    def __init__(self) -> None:
        self.__peliculas=[]

    def agregarPelicula(self,pelicula):
        self.__indice+=1
        self.__peliculas.append(pelicula)
    
    def getPeliculas(self):
        return self.__peliculas
    
    def toJSON(self): 
        d = dict(
            __class__=self.__class__.__name__, 
            peliculas=[pelicula.toJSON() for pelicula in self.__peliculas] 
            ) 
        return d