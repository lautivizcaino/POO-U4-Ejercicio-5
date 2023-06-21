from Vista import PeliculasView
from controlador import ControladorPeliculas
from repositorioPeliculas import RepositorioPeliculas
def main():
    repo=RepositorioPeliculas()
    vista=PeliculasView()
    ctrl=ControladorPeliculas(repo,vista)
    vista.setControlador(ctrl)
    ctrl.start()

if __name__=='__main__':
    main()