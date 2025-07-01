import { useState } from 'react';

export default function ContactForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    gameType: '',
  });
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevData => ({
      ...prevData,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Aquí podrías enviar los datos a una API si lo necesitas
    console.log(formData);
    setSubmitted(true);
  };

  if (submitted) {
    return (
      <div className="bg-green-100 border-l-4 border-green-500 text-green-700 p-4" role="alert">
        <p className="font-bold">Gracias por tu interés, {formData.name}!</p>
        <p>Notamos que te apasionan los Juegos {formData.gameType}.</p>
        <p>Nos contactaremos contigo a la brevedad usando tu dirección {formData.email}.</p>
        <p className="mt-4">
          <a href="https://quejuegosdemesa.com/instrucciones/" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">
            Descarga aquí instrucciones de juegos de mesa
          </a>
        </p>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto">
      <h2 className="text-2xl font-bold mb-4">Únete a la Aventura</h2>
      <p className="mb-4">¿Estás listo para explorar nuevos mundos? Deja tus datos y te contactaremos.</p>
      
      <div className="mb-4">
        <label htmlFor="name" className="block mb-2">Tu nombre:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
          className="w-full px-3 py-2 border rounded"
        />
      </div>

      <div className="mb-4">
        <label htmlFor="email" className="block mb-2">e-mail:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
          className="w-full px-3 py-2 border rounded"
        />
      </div>

      <div className="mb-4">
        <label htmlFor="gameType" className="block mb-2">Me gusta jugar:</label>
        <select
          id="gameType"
          name="gameType"
          value={formData.gameType}
          onChange={handleChange}
          required
          className="w-full px-3 py-2 border rounded"
        >
          <option value="">Selecciona el tipo de juego</option>
          <option value="de Cartas">Juegos de Cartas</option>
          <option value="Cooperativos">Juegos Cooperativos</option>
          <option value="Temáticos">Juegos Temáticos</option>
          <option value="de Estrategia">Juegos de Estrategia</option>
          <option value="de Aventura">Juegos de Aventura</option>
          <option value="de Acertijos">Juegos de Acertijos</option>
          <option value="Tradicionales">Juegos Tradicionales</option>
          <option value="de Rol">Juegos de Rol</option>
        </select>
      </div>

      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
        Enviar
      </button>
    </form>
  );
}