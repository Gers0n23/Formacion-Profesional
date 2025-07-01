const express = require('express');
require('./db');
const Propiedad = require('./Propiedad');

const app = express();
app.use(express.json());

app.post('/update', async (req, res) => {
    const { index, nombrePropiedad, tipo, comunaUbicacion, precio, metrosCuadrados, habitaciones, banos, estacionamientos, estado } = req.body;

    if (index === undefined) {
        return res.status(400).json({ error: 'Se requiere un índice para actualizar la propiedad.' });
    }

    try {
        const propiedades = await Propiedad.find();

        if (index < 0 || index >= propiedades.length) {
            return res.status(404).json({ message: 'Índice de propiedad no válido.' });
        }

        const propiedadId = propiedades[index]._id;

        const propiedadActualizada = await Propiedad.findByIdAndUpdate(
            propiedadId,
            {
                nombrePropiedad,
                tipo,
                comunaUbicacion,
                precio,
                metrosCuadrados,
                habitaciones,
                banos,
                estacionamientos,
                estado
            },
            { new: true }
        );

        if (!propiedadActualizada) {
            return res.status(404).json({ message: 'Propiedad no encontrada.' });
        }

        res.json({ message: 'Propiedad Actualizada Correctamente.' });
    } catch (err) {
        console.error("Error al Actualizar la propiedad:", err);
        res.status(500).json({ error: 'Error interno del servidor.' });
    }
});

const port = process.env.PORT || 2003;
app.listen(port, () => console.log(`Servidor compilado desde el puerto ${port}.`));
