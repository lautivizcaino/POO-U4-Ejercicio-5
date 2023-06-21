from Vista import PeliculasView
from gestorPeliculas import GestorPeliculas 
from repositorioPeliculas import RepositorioPeliculas
class ControladorPeliculas(object): 
    def __init__(self, repo, vista): 
        self.repo = repo 
        self.vista = vista 
        self.seleccion = -1 
        self.peliculas = list(repo.obtenerListaPeliculas())
    def seleccionarPelicula(self, index): 
        self.seleccion = index
        pelicula = self.peliculas[index] 
        self.vista.verPeliculaEnForm(pelicula)
    def start(self): 
        for p in self.peliculas: 
            self.vista.agregarPelicula(p) 
        self.vista.mainloop() 
