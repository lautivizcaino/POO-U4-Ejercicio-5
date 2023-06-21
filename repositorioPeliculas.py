import requests
from pelicula import Pelicula 
from objectEncoder import ObjectEncoder 
from gestorPeliculas import GestorPeliculas 
class RepositorioPeliculas: 
    __manejador=None 
    def __init__(self): 
        self.__manejador=GestorPeliculas()
        self.obtenerPeliculasAPI()
    def obtenerListaPeliculas(self): 
        return self.__manejador.getPeliculas() 
    def agregarPelicula(self, pelicula): 
        self.__manejador.agregarPelicula(pelicula) 
        return pelicula 

    def obtenerPeliculasAPI(self):
        url = 'https://api.themoviedb.org/3/discover/movie?api_key=94250e737aa6cef176757c4d2dff1a53'
        data = requests.get(url)
        if data.status_code==200:
            data = data. json()
            peliculas=data['results']
            for pelicula in peliculas:
                titulo=pelicula['original_title']
                resumen=pelicula['overview']
                lenguaje=pelicula['original_language']
                fecha=pelicula['release_date']
                generosID=pelicula['genre_ids']
                generos=self.obtenerGenerosAPI(generosID)
                unaPelicula=Pelicula(titulo,resumen,lenguaje,fecha,generos)
                self.agregarPelicula(unaPelicula)

    def obtenerGenerosAPI(self,generosID):
        url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=94250e737aa6cef176757c4d2dff1a53'
        data = requests.get(url)
        if data.status_code==200:
            data = data. json()
            generos=data['genres']
            i=0
            generosLista=[]
            while i<len(generos):
                for genero in generosID:
                    if generos[i]['id']==genero:
                        generosLista.append(generos[i]['name'])
                i+=1
            return generosLista
        
        