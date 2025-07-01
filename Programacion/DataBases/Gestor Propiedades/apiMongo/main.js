const { exec } = require('child_process');

const services = [
  'node delete.js',
  'node insert.js',
  'node search.js',
  'node server.js',
  'node update.js',
  'node Propiedad.js'
];

services.forEach(service => {
  const process = exec(service, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error al ejecutar ${service}:`, error);
      return;
    }
    if (stderr) {
      console.error(`Error en ${service}:`, stderr);
      return;
    }
    console.log(`${service} ejecutado correctamente:\n${stdout}`);
  });

  process.stdout.on('data', (data) => {
    console.log(`${service} stdout: ${data}`);
  });

  process.stderr.on('data', (data) => {
    console.error(`${service} stderr: ${data}`);
  });
});
