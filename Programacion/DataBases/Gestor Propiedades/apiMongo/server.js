const express = require('express')
const mongoose = require('mongoose')
const Propiedad = require('./Propiedad')

const app = express();
app.use(express.json()) // middleware para parsear Json

//conexion a MongoDB
const mongoURI = 'mongodb+srv://gersoncordero:gerson123456@clusterger.cytglrh.mongodb.net/gestor_propiedades?retryWrites=true&w=majority&appName=ClusterGer'
mongoose.connect(mongoURI)
.then(() => console.log('Conectado a la base de datos'))
.catch(err => console.log(err));

app.get('/', (req, res) => {
    Propiedad.find()
    .then(propiedades => {
        if (propiedades.length > 0){
            res.json(propiedades);
        }else{
            res.json({message: 'No se encontraron datos en la coleccion propiedades.'})
            
        }
    })
    .catch(err => {
        console.error("Error al buscar propiedades", err);
        res.status(500).json({error: 'Error interno del Servidor.'})
    });
});

//Inicializar el Servidor o API
const port = process.env.PORT || 2000;
app.listen(port, () => console.log(`Servidor ejecutado en el puerto ${port}`));


