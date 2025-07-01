from flask import *
import requests

app = Flask(__name__)

@app.route('/')
def index():
    datos = requests.get('http://127.0.0.1:2000/')
    if datos.status_code == 200:
        propiedades = datos.json()
        return render_template('index.html', propiedades=propiedades)
    else:
        return jsonify({'error':'Error al obtener los datos desde la ruta de la api Node.js'})

        
@app.route('/buscar', methods=['POST'])
def buscar():
    name = request.form['name']
    print(name)
    datos = requests.get(f"http://127.0.0.1:2001/propiedad/{name}")
    print(datos.status_code)
    
    if datos.status_code == 200:                
        propiedades = datos.json()
        if not propiedades:
            propiedades = []
        print(propiedades)
        return render_template('index.html', propiedades=propiedades)
    elif datos.status_code == 404:
        return render_template('index.html', propiedades=[], message=f'Propiedad no encontrada {name}' )
    else:
        return render_template('index.html', propiedades=[], message='Error al obtener los datos desde la ruta de la api Node.js')

    
    
@app.route('/update', methods=['POST'])
def update():
    data = request.json

    try:
        response = requests.post('http://127.0.0.1:2003/update', json=data)

        if response.status_code == 200:
            return jsonify({"message": "Propiedad actualizada correctamente"}), 200
        else:
            return jsonify({"error": "Error al actualizar la propiedad"}), response.status_code

    except requests.RequestException as e:
        return jsonify({"error": f"Error de conexión: {str(e)}"}), 500


@app.route('/delete', methods=['POST'])
def delete():
    data = request.json
    
    try:
        # Llamada al servicio de eliminación en el puerto 2004
        response = requests.post('http://127.0.0.1:2004/delete', json=data)
        
        if response.status_code == 200:
            return jsonify({"message": "Propiedad eliminada correctamente"}), 200
        else:
            return jsonify({"error": "Error al eliminar la propiedad"}), response.status_code
    
    except requests.RequestException as e:
        return jsonify({"error": f"Error de conexión: {str(e)}"}), 500

        
@app.route('/insert', methods=['POST'])
def insert_property():
    data = request.json  # Cambia a request.json para recibir JSON
    print(data)  # Añade un print para depuración

    response = requests.post('http://localhost:2002/insert', json=data)
    if response.status_code == 201:
        return redirect(url_for('index'))  # Cambia 'home' a 'index'
    else:
        return f"Error al agregar la propiedad: {response.text}", response.status_code

if __name__ == '__main__':
    app.run(debug=True)