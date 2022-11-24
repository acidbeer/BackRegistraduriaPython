from repositorios.RepositorioCandidato import RepositorioCandidato
from repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido

class ControladorCandidato():
    def __init__(self):
        print("Entro al constructor de la clase controlador candidato")
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def crearCandidato(self,bodyRequest):
        print("Creando el Candidato...")
        nuevoCandidato = Candidato(bodyRequest)
        print("Candidato a crear en la base de datos 1", nuevoCandidato)
        print("Candidato a crear en base de datos 2", nuevoCandidato.__dict__)
        self.repositorioCandidato.save(nuevoCandidato)
        return True

    def buscarCandidato(self, idObject):
        print("buscando el Candidato..", idObject)
        candidato = Candidato(self.repositorioCandidato.findById(idObject))
        return candidato.__dict__

    def buscarTodosLosCandidatos(self):
        print("Buscando todos los candidatos en base de datos...")
        return self.repositorioCandidato.findAll()

    def actualizarCandidato(self,id, candidato):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        print("Actualizando el candidato...", candidatoActual)
        candidatoActual.numero_resolucion= candidato["numero_resolucion"]
        candidatoActual.nombre = candidato["nombre"]
        candidatoActual.apellido = candidato["apellido"]
        candidatoActual.cedula = candidato["cedula"]
        self.repositorioCandidato.save(candidatoActual)
        return True

    def eliminarCandidato(self, idObject):
        print("Eliminando el candidato....", idObject)
        self.repositorioCandidato.delete(idObject)
        return True


    def asignarPartido(self, idCandidato,id_Partido):
        candidatoActual= Candidato(self.repositorioCandidato.findById(idCandidato))
        partidoActual = Partido(self.repositorioPartido.findById(id_Partido))
        print("Partido encontrado...", partidoActual.__dict__)
        print("candidato encontrado..", candidatoActual)
        candidatoActual.partido= partidoActual
        print("candidato actualizado",candidatoActual)
        return self.repositorioCandidato.save(candidatoActual)





