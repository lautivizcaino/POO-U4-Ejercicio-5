import tkinter as tk

class PeliculasList(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master)
        self.ListaBox=tk.Listbox(self,**kwargs,width=35)
        scroll=tk.Scrollbar(self,command=self.ListaBox.yview)
        self.ListaBox.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y) 
        self.ListaBox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    def insertar(self, pelicula, index=tk.END): 
        text = "{}".format(pelicula.getTitulo()) 
        self.ListaBox.insert(index, text)
    def bind_doble_click(self, callback): 
        handler = lambda _: callback(self.ListaBox.curselection()[0])
        self.ListaBox.bind("<Double-Button-1>", handler)

class PeliculasData(tk.LabelFrame):
    fields=('Titulo','Resumen','Lenguaje','Fecha de lanzamiento','Géneros')
    __values:list
    def __init__(self,master,**kwargs):
        super().__init__(master,text='Datos',padx=10,pady=10,**kwargs)
        self.frame=tk.Frame(self)
        self.__values=[tk.StringVar() for i in range(5)]
        self.datos=list(map(self.crearCampo,enumerate(self.fields),enumerate(self.__values)))
        self.frame.pack(side=tk.RIGHT,fill=tk.Y)
    
    def crearCampo(self, field,value): 
        position, text = field 
        position,textv= value
        label = tk.Label(self.frame, text=text)
        if position==1:
            dato=tk.Label(self.frame,textvariable=textv,width=90,height=5,justify='left',wraplength=550) 
        else:
            dato = tk.Label(self.frame,textvariable=textv,width=50) 
        label.grid(row=position, column=0, pady=5) 
        dato.grid(row=position, column=1, pady=5) 
        return dato
    
    def mostrarEstadoPeliculaEnFormulario(self, pelicula):
        self.__values[0].set(pelicula.getTitulo()) 
        self.__values[1].set(pelicula.getResumen())
        self.__values[2].set(pelicula.getLenguaje())
        self.__values[3].set(pelicula.getFecha())
        self.__values[4].set(pelicula.getGeneros()) 

class PeliculasView(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Lista de Peliculas')
        self.lista=PeliculasList(self)
        self.data=PeliculasData(self)
        self.lista.pack(side=tk.LEFT, padx=20, pady=20)
        self.data.pack(side=tk.RIGHT,padx=10,pady=10)
    def setControlador(self, ctrl): 
        self.lista.bind_doble_click(ctrl.seleccionarPelicula)
    def agregarPelicula(self, pelicula): 
        self.lista.insertar(pelicula)
    def verPeliculaEnForm(self, pelicula): 
        self.data.mostrarEstadoPeliculaEnFormulario(pelicula)
