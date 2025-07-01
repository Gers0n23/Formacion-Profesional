from flask import Flask, render_template, request, redirect, url_for,session, flash
import bcrypt
from conexion import libros, autores, clientes, pedidos,db, usuarios

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/index')
def index():
    # obtiene el resumen de los libros y las ventas
    
    pipeline = [
    {
        "$lookup": {
            "from": "autores",
            "localField": "autor_id",
            "foreignField": "_id",
            "as": "autor_info"
        }
    },
    {
    "$unwind": {
        "path": "$autor_info",
        "preserveNullAndEmptyArrays": True
    }
    },
    {
        "$lookup": {
            "from": "pedidos",
            "localField": "_id",
            "foreignField": "libro_id",
            "as": "pedidos_info"
        }
    },
    {
    "$unwind": {
        "path": "$pedidos_info",
        "preserveNullAndEmptyArrays": True
    }
    },
    {
        "$group": {
            "_id": "$titulo",                         # Agrupar por título
            "titulo": {"$first": "$titulo"},          # Conservar el título
            "precio": {"$first": "$precio"},          # Conservar el precio
            "stock": {"$first": "$stock"},            # Conservar el stock
            "autor_info": {"$first": "$autor_info"},  # Conservar la información del autor
            "cantidad_pedidos": {"$sum": "$pedidos_info.cantidad"},        # Sumar la cantidad de pedidos
            "valor_total_pedidos": {"$sum": "$pedidos_info.total"}         # Sumar el valor total de pedidos
        }
    },
    {
        "$project": {
            "_id": 0,   # Excluir el campo _id del resultado final
            "titulo": 1,
            "precio": 1,
            "stock": 1,
            "autor_info.nombre": 1,
            "autor_info.nacionalidad": 1,
            "cantidad_pedidos": 1,
            "valor_total_pedidos": 1
        }
    },
    {
        "$sort": {"titulo": 1}  # Ordenar por título de manera descendente
    }
    ]

    result = list(db.libros.aggregate(pipeline))
    username = session.get('username')
    return render_template('index.html', libros=result,username=username)

@app.route('/buscar', methods=['POST'])
def buscar():
    busqueda = request.form.get('busqueda')

    pipeline = [
        {
            "$lookup": {
                "from": "autores",
                "localField": "autor_id",
                "foreignField": "_id",
                "as": "autor_info"
            }
        },
        {
            "$unwind": {
                "path": "$autor_info",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$lookup": {
                "from": "pedidos",
                "localField": "_id",
                "foreignField": "libro_id",
                "as": "pedidos_info"
            }
        },
        {
            "$unwind": {
                "path": "$pedidos_info",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$match": {
                "titulo": {
                    "$regex": busqueda,
                    "$options": "i"
                }
            }
        },
        {
            "$group": {
                "_id": "$titulo",
                "titulo": {"$first": "$titulo"},
                "precio": {"$first": "$precio"},
                "stock": {"$first": "$stock"},
                "autor_info": {"$first": "$autor_info"},
                "cantidad_pedidos": {"$sum": "$pedidos_info.cantidad"},
                "valor_total_pedidos": {"$sum": "$pedidos_info.total"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "titulo": 1,
                "precio": 1,
                "stock": 1,
                "autor_info.nombre": 1,
                "autor_info.nacionalidad": 1,
                "cantidad_pedidos": 1,
                "valor_total_pedidos": 1
            }
        },
        
        {
        "$sort": {"titulo": 1}  # Ordenar por título de manera descendente
        }
    ]

    libros_filtrados = list(db.libros.aggregate(pipeline))
    return render_template('index.html', libros=libros_filtrados)

@app.route('/libros', methods=['GET', 'POST'])
# define la ruta para agregar los libros
def manage_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        id = int(request.form['id'])
        autor_id = int(request.form['autor_id'])
        precio = int(request.form['precio'])
        stock = int(request.form['stock'])

        if not titulo or not autor_id or not id:
            return "Por favor, completa todos los campos antes de agregar un libro.", 400

        libros.insert_one({'titulo': titulo,
                           '_id': id,
                           'autor_id': autor_id, 
                           'precio': precio, 
                           'stock': stock})
        return redirect(url_for('manage_libros'))

    all_libros = libros.find()
    username = session.get('username')
    return render_template('libros.html', libros=all_libros,username=username)

@app.route('/libros/delete/<id>', methods=['POST'])
# define la ruta para eliminar un libro
def delete_libro(id):
    libros.delete_one({'_id': int(id)})
    return redirect(url_for('manage_libros'))

@app.route('/libros/edit/<id>', methods=['POST'])
# define la ruta para editar un libro
def edit_libro(id):
    titulo = request.form['titulo']
    id = request.form['id']
    autor_id = int(request.form['autor_id'])
    precio = int(request.form['precio'])
    stock = int(request.form['stock'])
    libros.update_one({'_id': int(id)}, {'$set': {'titulo': titulo, 
                                                  'autor_id': autor_id, 
                                                  'precio': precio, 
                                                  'stock': stock}})
    return redirect(url_for('manage_libros'))

@app.route('/autores', methods=['GET', 'POST'])
# define la ruta para agregar los autores
def manage_autores():
    if request.method == 'POST':
        id = int(request.form['id'])
        nombre = request.form['nombre']
        nacionalidad = request.form['nacionalidad']
        autores.insert_one({'nombre': nombre, 
                            'nacionalidad': nacionalidad, 
                            '_id':id})
        return redirect(url_for('manage_autores'))
    
    all_autores = autores.find()
    username = session.get('username')
    return render_template('autores.html', autores=all_autores,username=username)

@app.route('/autores/delete/<id>', methods=['POST'])
# define la ruta para eliminar un autor
def delete_autor(id):
    autores.delete_one({'_id': int(id)})
    return redirect(url_for('manage_autores'))

@app.route('/autores/edit/<id>', methods=['POST'])
# define la ruta para editar un autor
def edit_autor(id):
    nombre = request.form['nombre']
    nacionalidad = request.form['nacionalidad']
    autores.update_one({'_id': int(id)}, {'$set': {'nombre': nombre, 
                                                   'nacionalidad': nacionalidad}})
    return redirect(url_for('manage_autores'))

@app.route('/clientes', methods=['GET', 'POST'])
# define la ruta para agregar los clientes
def manage_clientes():
    if request.method == 'POST':
        id= int(request.form['id'])
        nombre = request.form['nombre']
        email = request.form['email']
        clientes.insert_one({'nombre': nombre, 
                             'email': email, 
                             '_id':id})
        return redirect(url_for('manage_clientes'))
    
    all_clientes = clientes.find()
    username = session.get('username')
    return render_template('clientes.html', clientes=all_clientes,username=username)

@app.route('/clientes/delete/<id>', methods=['POST'])
# define la ruta para eliminar un cliente
def delete_cliente(id):
    clientes.delete_one({'_id': int(id)})
    return redirect(url_for('manage_clientes'))

@app.route('/clientes/edit/<id>', methods=['POST'])
# define la ruta para editar un cliente
def edit_cliente(id):
    nombre = request.form['nombre']
    email = request.form['email']
    clientes.update_one({'_id': int(id)}, {'$set': {'nombre': nombre, 
                                                    'email': email}})
    return redirect(url_for('manage_clientes'))

@app.route('/pedidos', methods=['GET', 'POST'])
# define la ruta para agregar los pedidos
def manage_pedidos():
    if request.method == 'POST':
        id = int(request.form['id'])
        cliente_id = int(request.form['cliente_id'])
        libro_id = int(request.form['libro_id'])
        cantidad = int(request.form['cantidad'])
        total = int(request.form['total'])
        pedidos.insert_one({'cliente_id': cliente_id, 
                            'libro_id': libro_id, 
                            'cantidad': cantidad, 
                            'total': total, 
                            '_id':id})
        return redirect(url_for('manage_pedidos'))
    
    all_pedidos = pedidos.find()
    username = session.get('username')
    return render_template('pedidos.html', pedidos=all_pedidos,username=username)

@app.route('/pedidos/delete/<id>', methods=['POST'])
# define la ruta para eliminar un pedido
def delete_pedido(id):
    pedidos.delete_one({'_id': int(id)})
    return redirect(url_for('manage_pedidos'))

@app.route('/pedidos/edit/<id>', methods=['POST'])
# define la ruta para editar un pedido
def edit_pedido(id):
    id = int(request.form['id'])
    cliente_id = int(request.form['cliente_id'])
    libro_id = int(request.form['libro_id'])      
    cantidad = int(request.form['cantidad'])
    total = int(request.form['total'])
    pedidos.update_one({'_id': int(id)}, {'$set': {'cliente_id': cliente_id, 
                                                   'libro_id': libro_id, 
                                                   'cantidad': cantidad, 
                                                   'total': total}})
    return redirect(url_for('manage_pedidos'))

@app.route('/usuarios', methods=['GET', 'POST'])
def manage_usuarios():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']
        
        # Generar el hash de la contraseña
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        # Insertar el usuario en la colección
        usuarios.insert_one({'username': username, 'password': hashed_password, 'rol': rol})
        return redirect(url_for('manage_usuarios'))
    
    all_usuarios = usuarios.find()
    username = session.get('username')
    return render_template('usuarios.html', usuarios=all_usuarios,username=username)

@app.route('/usuarios/delete/<id>', methods=['POST'])
def delete_usuario(id):
    usuarios.delete_one({'username': id})
    return redirect(url_for('manage_usuarios'))

@app.route('/usuarios/edit/<id>', methods=['POST'])
def edit_usuario(id):
    username = request.form['username']
    password = request.form['password']
    rol = request.form['rol']
    
    update_fields = {'username': username, 'rol': rol}
    if password:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        update_fields['password'] = hashed_password
    
    usuarios.update_one({'username': id}, {'$set': update_fields})
    return redirect(url_for('manage_usuarios'))


app.secret_key = 'tu_secreto'

def registrar_usuario(username, password, rol):
    # Generar un salt y hashear la contraseña
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # Crear el documento de usuario
    usuario = {
        "username": username,
        "password": hashed_password,
        "rol": rol
    }
    
    # Insertar el usuario en la colección
    usuarios.insert_one(usuario)
    print(f"Usuario {username} registrado correctamente con rol {rol}")

def autenticar_usuario(username, password):
    usuario = usuarios.find_one({"username": username})
    if usuario:
        if bcrypt.checkpw(password.encode('utf-8'), usuario['password']):
            return True
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if autenticar_usuario(username, password):
            session['username'] = username  # Almacenar el usuario en la sesión
            return redirect(url_for('index'))  # Redireccionar al inicio o a otra página protegida
        else:
            error_message = "Usuario o contraseña incorrectos."
            return render_template('login.html', error=error_message)

    return render_template('login.html')  # Renderizar el formulario de inicio de sesión


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        rol = 'user'

        if not username or not password or not rol:
            return "Por favor, completa todos los campos antes de registrar un usuario.", 400

        registrar_usuario(username, password, rol)
        flash('¡Registro exitoso! Ahora puedes iniciar sesión.')
        return redirect(url_for('login'))

    return render_template('register.html')

def generar_hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

@app.route('/protected')
def protected():
    username = session.get('username')
    return render_template('protected.html', username=username)

# ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
