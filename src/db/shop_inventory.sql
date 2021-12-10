DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS publishers;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE publishers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    website VARCHAR(255) NOT NULL,
    salesperson VARCHAR(255),
    contact VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    ISBN INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    author_id INT REFERENCES authors(id) ON DELETE CASCADE NOT NULL,
    illustrator_id INT REFERENCES authors(id) ON DELETE CASCADE NOT NULL,
    publisher_id INT REFERENCES publishers(id) ON DELETE CASCADE NOT NULL,
    edition INT NOT NULL,
    cost INT NOT NULL,
    price INT NOT NULL,
    stock INT NOT NULL
);