const mongoose = require('mongoose')

const PropiedadShema = new mongoose.Schema({
        nombrePropiedad: {
                type: String,
                required: true
            },
            tipo: String,
            comunaUbicacion: String,
            precio: Number,
            metrosCuadrados: Number,
            habitaciones: Number,
            banos: Number,
            estacionamientos: Number,
            estado: String  
})

const Propiedad = mongoose.model('Propiedad', PropiedadShema, 'propiedades')
module.exports = Propiedad
