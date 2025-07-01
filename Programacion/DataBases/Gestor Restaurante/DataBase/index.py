from flask import *
from conectar import *
from find import *
from buscar import *

app = Flask(__name__)

@app.route('/')

def home():
    db = conexion()
    datos = db.restaurants.find()

    return render_template('index.html', datos = datos)

@app.route('/buscar', methods=['GET','POST'])
def buscar():
    if request.method == 'POST':
        id = request.get('id')
        if id:
            buscar = Buscar(id)
            restaurante = buscar.buscar()

            return render_template('index.html', datos = [restaurante])
        else:
            return render_template('index.html', datos = [])
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)