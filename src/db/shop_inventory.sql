DELETE TABLE books IF EXISTS
DELETE TABLE publishers IF EXISTS
DELETE TABLE authors IF EXISTS

CREATE TABLE authors (
    id INT SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE publishers (
    id INT SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    website VARCHAR(255) NOT NULL,
    salesperson VARCHAR(255),
    contact VARCHAR(255)
);

CREATE TABLE books (
    id INT SERIAL PRIMARY KEY,
    ISBN INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    author_id INT REFERENCES authors(id) NOT NULL ON DELETE CASCADE,
    illustrator_id INT REFERENCES author(id) NOT NULL ON DELETE CASCADE,
    publisher_id INT REFERENCES publishers(id) NOT NULL ON DELETE CASCADE
    edition INT NOT NULL,
    cost INT NOT NULL,
    price INT NOT NULL,
    stock INT NOT NULL
);