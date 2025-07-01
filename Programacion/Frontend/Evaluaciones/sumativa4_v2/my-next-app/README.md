# My Next App

This is a Next.js project with Tailwind CSS.

## Project Structure

```
my-next-app
├── pages
│   ├── api
│   │   ├── users.js
│   │   └── products.js
│   ├── _app.js
│   ├── index.js
│   └── admin
│       ├── usuarios.js
│       └── productos.js
├── public
│   ├── juegos
│   │   └── [images]
│   └── favicon.ico
├── components
│   ├── header.js
│   ├── footer.js
│   └── layout.js
├── styles
│   ├── global.css
│   └── Home.module.css
├── .env.local
├── package.json
├── tailwind.config.js
├── postcss.config.js
└── README.md
```

## API Endpoints

- `/api/users`: API endpoint for interacting with the user database.
- `/api/products`: API endpoint for interacting with the product database.

## Pages

- `/index.js`: Main page of the application, representing the home page. It includes the catalog and the shopping cart components.
- `/admin/usuarios.js`: CRUD operations for managing user data in the admin section.
- `/admin/productos.js`: CRUD operations for managing product data in the admin section.

## Public Assets

- `/public/juegos`: Folder for storing images of the products.
- `/public/favicon.ico`: Favicon for the application.

## Components

- `components/header.js`: Header component that includes the INACAPLudi corporate image and the login form.
- `components/footer.js`: Footer component that displays the "Creado por INACAPLudi(c) 2024" message.
- `components/layout.js`: Layout component that represents the overall structure of the application. It includes the Header and Footer components.

## Styles

- `styles/global.css`: Global styles that will be applied to all pages of the application.
- `styles/Home.module.css`: Styles specific to the Home page.

## Configuration Files

- `.env.local`: File for storing API URLs and any other secrets.
- `package.json`: Configuration file for npm.
- `tailwind.config.js`: Configuration file for Tailwind CSS.
- `postcss.config.js`: Configuration file for PostCSS.

For more information, please refer to the documentation in the `README.md` file.