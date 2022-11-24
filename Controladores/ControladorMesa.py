from repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print("Entro al constructor de la clase controlador Mesa..")
        self.repositorioMesa= RepositorioMesa()

    def crearMesa(self,bodyRequest):
            print("Creando la Mesa")
            nuevaMesa= Mesa(bodyRequest)
            print("Mesa a crear en base de datos ",nuevaMesa .__dict__)
            self.repositorioMesa.save(nuevaMesa)
            return True

    def buscarMesa(self,idMesa):
            print("Buscando la Mesa..",idMesa)
            mesa = Mesa(self.repositorioMesa.findById(idMesa))
            return mesa.__dict__

    def buscarTodosLasMesas(self):
            print("Buscando todos las mesas en base de datos")
            return self.repositorioMesa.findAll()

    def actualizarMesa(self, idMesa,mesa):
            mesaActual= Mesa(self.repositorioMesa.findById(idMesa))
            print("Actualizar la Mesa..",mesaActual)
            mesaActual.numero = mesa["numero"]
            mesaActual.cantidad_inscritos = mesa["cantidad_inscritos"]
            self.repositorioMesa.save(mesaActual)
            return True

    def eliminarMesa(self, idMesa):
            print("Eliminando Mesa..",idMesa)
            self.repositorioMesa.delete(idMesa)
            return True

