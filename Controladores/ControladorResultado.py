
from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from repositorios.RepositorioResultado import RepositorioResultado
from repositorios.RepositorioMesa import RepositorioMesa
from repositorios.RepositorioCandidato import RepositorioCandidato

class  ControladorResultado():

    def __init__(self):
        print("entro al constructor de la clase controlador Resultado")
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()


 #relacion muchos a muchos
    def crearResultado(self,bodyRequest, idCandidato, idMesa):
        print("creando Resultado...")
        nuevoResultado= Resultado(bodyRequest)
        candidatoActual= Candidato(self.repositorioCandidato.findById(idCandidato))
        mesaActual= Mesa(self.repositorioMesa.findById(idMesa))
        nuevoResultado.candidato =candidatoActual
        nuevoResultado.mesa = mesaActual
        print("Resultado a crear en base de datos...", nuevoResultado.__dict__ )
        return self.repositorioResultado.save(nuevoResultado)



    def buscarResultado(self, idObject):
        print("buscando el Resultado...", idObject)
        resultado= Resultado(self.repositorioResultado.findById(idObject))
        return resultado.__dict__

    def buscarTodosLosResultados(self):
        print("buscar todos los resultados en base de datos...")
        return self.repositorioResultado.findAll()

    def actualizarResultado(self,idResultado,resultado):
        resultadoActual= Resultado(self.repositorioResultado.findById(idResultado))
        print("Actualizando el estudiante ....", resultadoActual)
        resultadoActual.id = resultado["id"]
        resultadoActual.numero_mesa = resultado["numero_mesa"]
        resultadoActual.cedula_candidato = resultado["cedula_candidato"]
        resultadoActual.numero_votos = resultado["numero_votos"]
        self.repositorioResultado.save(resultadoActual)
        return True

    def eliminarResultado(self, idObject):
        print("eliminando el Resultado...", idObject)
        self.repositorioResultado.delete(idObject)
        return True





