from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

import math

# files
from data_loader import load_data
import som

app = Flask(__name__)
cors = CORS(app)

data = None


@app.route("/test")
def test():
    return jsonify({'hello': 'world'})


@app.route("/execute", methods=['POST'])
def execute():
    body = request.json
    # Obtener las columnas del body
    # rows = body['rows']
    # columns = body['columns']

    # cantidad de clusters a ejecutar
    clusters = body['clusters']
    # Las dimensiones a evaluar
    dimensions = body['dimensions']

    # Eligiendo las columnas
    filtered_data = []
    for col in dimensions:
        filtered_data.append(data[col])

    # Creando los items
    items = []
    size = len(data['name'])
    cols_count = len(dimensions)

    for i in range(size):
        row = []
        for j in range(cols_count):
            if(math.isnan(filtered_data[j][i])):
                row.append(0)
            else:
                row.append(filtered_data[j][i])
        items.append(row)

    rows = 1
    cols = clusters
    # Realizar el algoritmo con las columnas elegidas por el usuario?
    result = som.som(data['name'], items, rows, cols)

    return jsonify(result)


if __name__ == "__main__":

    # Cargar los datos desde el archivo
    data = load_data()

    # Iniciar servidor
    port = 5000
    print("Server started on port 5000")
    app.run(debug=False, host="127.0.0.1", port=port, threaded=True)
