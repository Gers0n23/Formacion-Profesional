const express = require('express');
const mongoose = require('mongoose');
const Propiedad = require('./Propiedad');

const app = express();
app.use(express.json());

const mongoURI = 'mongodb+srv://gersoncordero:gerson123456@clusterger.cytglrh.mongodb.net/gestor_propiedades?retryWrites=true&w=majority&appName=ClusterGer';
mongoose.connect(mongoURI)
    .then(() => console.log("Conectado a la base de datos."))
    .catch(err => console.log(err));

// Modificar la ruta de búsqueda
app.get('/propiedad/:name', (req, res) => {
    const regex = new RegExp(req.params.name, 'i'); // 'i' para insensible a mayúsculas
    Propiedad.find({ nombrePropiedad: regex })
        .then(propiedades => {
            if (propiedades.length === 0) {
                return res.status(404).json({ message: 'No se encontraron propiedades.' });
            } else {
                res.json(propiedades);
            }
        })
        .catch(err => {
            console.error("Error al buscar la Propiedad:", err);
            res.status(500).json({ error: 'Error interno del servidor.' });
        });
});

const port = process.env.PORT || 2001;
app.listen(port, () => console.log(`Servidor ejecutado en el puerto ${port}`));