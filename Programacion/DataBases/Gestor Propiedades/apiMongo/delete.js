const express = require('express')
require('./db')
const Propiedad = require('./Propiedad')

const app = express();
app.use(express.json())

app.post('/delete', async (req, res) => {
    const { index } = req.body;
    
    if (index === undefined) {
        return res.status(400).json({ error: 'Se requiere un índice para eliminar la propiedad.' });
    }

    try {
        // Obtener todas las propiedades
        const propiedades = await Propiedad.find();

        // Verificar si el índice es válido
        if (index < 0 || index >= propiedades.length) {
            return res.status(404).json({ message: 'Índice de propiedad no válido.' });
        }

        // Obtener el ID de la propiedad en el índice especificado
        const propiedadId = propiedades[index]._id;

        // Eliminar la propiedad
        const propiedadEliminada = await Propiedad.findByIdAndDelete(propiedadId);

        if (!propiedadEliminada) {
            return res.status(404).json({ message: 'Propiedad no encontrada.' });
        }

        res.json({ message: 'Propiedad Eliminada Correctamente.' });
    } catch (err) {
        console.error("Error al eliminar la propiedad:", err);
        res.status(500).json({ error: 'Error interno del servidor.' });
    }
});

const port = process.env.PORT || 2004
app.listen(port, () => console.log(`Servidor compilado en el puerto ${port}`))
