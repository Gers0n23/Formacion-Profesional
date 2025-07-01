import sqlite3 from 'sqlite3';
import { open } from 'sqlite';

let db = null;

async function getDb() {
  if (db) return db;
  db = await open({
    filename: './database.sqlite',
    driver: sqlite3.Database
  });
  return db;
}

export async function getUsers() {
  const db = await getDb();
  return db.all('SELECT * FROM users');
}

export async function createUser(user) {
  const db = await getDb();
  const { username, password, email, real_name } = user;
  
  const result = await db.run(
    'INSERT INTO users (username, password, email, real_name) VALUES (?, ?, ?, ?)',
    [username, password, email, real_name]
  );
  
  return { id: result.lastID, ...user };
}

// Implementa las funciones updateUser y deleteUser de manera similar

export async function getProducts() {
  const db = await getDb();
  return db.all('SELECT * FROM products');
}

export async function createProduct(product) {
  const db = await getDb();
  const { title, description, availability, location, image } = product;
  const result = await db.run(
    'INSERT INTO products (title, description, availability, location, image) VALUES (?, ?, ?, ?, ?)',
    [title, description, availability, location, image]
  );
  return { id: result.lastID, ...product };
}

// Implementa las funciones updateProduct y deleteProduct de manera similar