const mongoose = require('mongoose')

const mongoURI = 'mongodb+srv://gersoncordero:gerson123456@clusterger.cytglrh.mongodb.net/gestor_propiedades?retryWrites=true&w=majority&appName=ClusterGer'

mongoose.connect(mongoURI, {useNewUrlParser: true, useUnifiedTopology: true})
.then(() => console.log('Conectado a la base de datos.'))
.catch(err => console.log(err))

module.exports = mongoose