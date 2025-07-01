const express = require('express');
require('./db');
const Propiedad = require('./Propiedad');

const app = express();
app.use(express.json());

// Ruta para agregar una nueva propiedad
app.post('/insert', async (req, res) => {
    const { nombrePropiedad, tipo, comunaUbicacion, precio, metrosCuadrados, habitaciones, banos, estacionamientos, estado } = req.body;
    
    console.log(req.body); // Log para verificar los datos recibidos

    const nuevaPropiedad = new Propiedad({
        nombrePropiedad,
        tipo,
        comunaUbicacion,
        precio,
        metrosCuadrados,
        habitaciones,
        banos,
        estacionamientos,
        estado
    });

    try {
        await nuevaPropiedad.save();
        res.status(201).json({ message: 'Propiedad agregada correctamente.' });
    } catch (err) {
        console.error("Error al agregar la propiedad:", err);
        res.status(500).json({ error: 'Error interno del servidor.' });
    }
});

const port = process.env.PORT || 2002;
app.listen(port, () => console.log(`Servidor compilado desde el puerto ${port}.`));
