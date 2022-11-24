from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve


app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado
micontroladorCandidato = ControladorCandidato()
micontroladorMesa = ControladorMesa()
miControladorPartido= ControladorPartido()
micontroladorResultado= ControladorResultado()



@app.route("/candidato",methods=['POST'])
def crearCandidato():
    requestBody= request.get_json()
    print("body request", requestBody)
    result =micontroladorCandidato.crearCandidato(requestBody)
    if result:
        return {"result": "El candidato se creo correctamente"}
    else:
        return jsonify(result)


@app.route("/candidato/<string:idObject>", methods=['GET'])
def buscarCandidato(idObject):
    result = micontroladorCandidato.buscarCandidato(idObject)
    if result is None:
        return {"resultado": "No se encuentra el Candidato en base de datos!"}
    else:
        return jsonify(result)


@app.route("/candidato", methods=['GET'])
def buscarTodosLosCandidatos():
    result = micontroladorCandidato.buscarTodosLosCandidatos()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/candidato/<string:id>", methods=['PUT'])
def actualizarCandidato(id):
    requestBody=request.get_json()
    print("Request body: ", requestBody)
    result = micontroladorCandidato.actualizarCandidato(id,requestBody)
    if result:
        return {"resultado": "Candidato actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Candidato!"}

#relacion uno a muchos

@app.route("/candidato/<string:idCandidato>/partido/<string:id_Partido>",methods=['PUT'])
def asignarPartido(idCandidato,id_Partido):
    result=micontroladorCandidato.asignarPartido(idCandidato,id_Partido)
    return jsonify(result)

@app.route("/candidato/<string:idObject>", methods=['DELETE'])
def eliminarCandidato(idObject):
    result = micontroladorCandidato.eliminarCandidato(idObject)
    if result:
        return {"resultado": "Candidato eliminado!"}
    else:
        return {"resultado": "Error al eliminar el Candidato!"}

##rutas Mesa

@app.route("/mesa",methods=['POST'])
def crearMesa():
    requestBody= request.get_json()
    print("request Body", requestBody)
    result = micontroladorMesa.crearMesa(requestBody)
    if result:
        return{"result": "la mesa se creo correctamente"}
    else:
        return{"result": "Error al crear mesa"}

@app.route("/mesa/<string:idMesa>",methods=['GET'])
def buscarMesa(idMesa):
    result= micontroladorMesa.buscarMesa(idMesa)
    if result is None:
        return {"resultado": "No se encuentra la mesa en base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa",methods=['GET'])
def buscarTodasLasMesas():
    result= micontroladorMesa.buscarTodosLasMesas()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa/<string:idMesa>", methods=['PUT'])
def actualizarMesa(idMesa):
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = micontroladorMesa.actualizarMesa(idMesa,requestBody)
    if result:
        return {"resultado": "Mesa actualizado!"}
    else:
        return {"resultado": "Error al actualizar la Mesa!"}

@app.route("/mesa/<string:idMesa>", methods=['DELETE'])
def eliminarMesa(idMesa):
    result = micontroladorMesa.eliminarMesa(idMesa)
    if result:
        return {"resultado": "Mesa eliminada!"}
    else:
        return {"resultado": "Error al eliminar la Mesa!"}

# rutas de Partido

@app.route("/partidos",methods=['POST'])
def crearPartido():
    data= request.get_json()
    json=miControladorPartido.crearPartido(data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])
def buscarPartido(id):
    result=miControladorPartido.buscarPartido(id)
    if result is None:
        return {"resultado": "No se encuentra el partido en base de datos!"}
    else:
        return jsonify(result)

@app.route("/partidos",methods=['GET'])
def buscarTodosLosPartidos():
    result= miControladorPartido.buscarTodosLosPartidos()
    if not result:
        return {"resultado": "No se encuentran los Partidos"}
    else:
        return jsonify(result)

@app.route("/partidos/<string:idPartido>", methods=['PUT'])
def actualizarPartido(idPartido):
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result= miControladorPartido.actualizarPartido(idPartido,requestBody)
    if result:
        return {"resultado": "Partido actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Partido!"}

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    result= miControladorPartido.deletePartido(id)
    if result is None:
        return {"resultado": "No se elimina el Partido en base de datos!"}
    else:
        return jsonify(result)


# rutas Resultado
## path para la relacion muchos a ,muchos

@app.route("/resultado/candidato/<string:idCandidato>/mesa/<string:idMesa>", methods=['POST'])
def crearResultado(idCandidato, idMesa):
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result=micontroladorResultado.crearResultado(requestBody, idCandidato, idMesa)
    return jsonify(result)

@app.route("/resultado/<string:idObject>",methods=['GET'])
def buscarResultado(idObject):
    result= micontroladorResultado.buscarResultado(idObject)
    if result is None:
        return {"resultado": "No se encuentra el Resultado en base de datos!"}
    else:
        return jsonify(result)

@app.route("/resultado",methods=['GET'])
def buscarTodosLosResultados():
    result= micontroladorResultado.buscarTodosLosResultados()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/resultado/<string:idResultado>",methods=['PUT'])
def actualizarResultado(idResultado):
    requestBody= request.get_json()
    print("Request Body: ", requestBody)
    result=micontroladorResultado.actualizarResultado(idResultado,requestBody)
    if result:
        return {"resultado": "Resultado actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Resultado!"}

@app.route("/resultado/<string:idObject>",methods=['DELETE'])
def eliminarResultado(idObject):
    result= micontroladorResultado.eliminarResultado(idObject)
    if result:
        return {"resultado": "Estudiante eliminado!"}
    else:
        return {"resultado": "Error al eliminar el Estudiante!"}







def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)

    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()

    print("Server running : "+"http://"+dataConfig["url-backend"]+":"+ str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

