from repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        print("entro al constructor de la clase controlador Partido")
        self.repositorioPartido = RepositorioPartido()

    def crearPartido(self,bodyRequest):
        print("creando el Partido..")
        nuevoPartido = Partido(bodyRequest)
        print("Partido a crear en la base de datos..",nuevoPartido.__dict__)
        self.repositorioPartido.save(nuevoPartido)
        return True

    def buscarPartido(self,idObject):
        print("buscando el Partido", idObject)
        partido = Partido(self.repositorioPartido.findById(idObject))
        return partido.__dict__

    def buscarTodosLosPartidos(self):
        print("Buscando todos los partidos en base de datos...")
        return self.repositorioPartido.findAll()

    def actualizarPartido(self,idPartido, partido):
        partidoActual = Partido(self.repositorioPartido.findById(idPartido))
        print("Actualizando el Partido...", partidoActual)
        partidoActual.id = partido["id"]
        partidoActual.nombre = partido["nombre"]
        partidoActual.lema = partido["lema"]
        self.repositorioPartido.save(partidoActual)
        return True

    def eliminarPartido(self, idObject):
        print("Eliminando el Partido...", idObject)
        self.repositorioPartido.delete(idObject)
        return True









