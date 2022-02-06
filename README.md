![Python](https://img.shields.io/badge/python-v3.5+-blue.svg?style=appveyor)
![Flask](https://img.shields.io/badge/Flask-v2.0.2+-black?style=appveyor&logo=flask&logoColor=white?)
![PostgresQL](https://img.shields.io/badge/PostgreSQL-v14.0-red?style=appveyor&logo=postgresql&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26??style=appveyor&logo=html5&logoColor=white+)
![CSS](https://img.shields.io/badge/CSS3-1572B6??&style=appveyor&logo=css3&logoColor=white)

1. [Project brief](https://github.com/clauRamirez/flask-inventory-manager#project-brief)
2. [Demo](https://github.com/clauRamirez/flask-inventory-manager#demo)
3. [TO-DO](https://github.com/clauRamirez/flask-inventory-manager#to-do)

## Overview

Final project for the Python module at the Professional Software Development Bootcamp by CodeClan.

Full-Stack web application built with Flask, Postgres, Python3, HTML5 and CSS3 with a MVC architecture.

<br>

## 1. Project brief

#### **Shop Inventory**

Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

#### **MVP**

* The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
* The inventory should track manufacturers, including a name and any other appropriate details.
* The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
  * This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
* Show an inventory page, listing all the details for all the products in stock in a single view.
* As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

#### **Rules**

The project must be built using only:

* HTML / CSS
* Python
* Flask
* PostgreSQL and the psycopg

It must **NOT** use:

* Any Object Relational Mapper (e.g. ActiveRecord)
* JavaScript. At all. Don't even think about it.
* Any pre-built CSS libraries, such as Bootstrap.
* Authentication. Assume that the user already has secure access to the app.

<br>

## 2. Demo

To run a demo locally, in your terminal:

1. Clone the repository
```
git clone https://github.com/clauRamirez/flask_inventory_manager
```
2. Go to project directory and cd into /src directory:
```
cd /path/to/project/src
```
3. Install dependencies:
```
pip install psycopg2 flask
```
4. Create database.
```
createdb shop_inventory
```
5. Import tables to database
```
psql -d shop_inventory -f db/shop_inventory.sql
```
6. Populate database
```
python3 populate_db.py
```
7. Run the flask application
```
flask run
```
or
```
python3 -m flask run
```
8. You should see something like this:

```
Serving Flask app 'app.py' (lazy loading)
Environment: development
Debug mode: on
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Restarting with stat
Debugger is active!
```

9. Go to http://127.0.0.1:5000/ or whichever port the 
app is running on in your local machine.

10. Have fun!

<br>

## 3. TO-DO

- [ ] Add setup script
