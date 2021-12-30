# INVENTORY TRACKER

### Questions:

1. How do I test my class methods if I need to take data out of the Database?

### TO-DO

#### PLANNING
- [x] Choose theme
- [x] Database diagram
- [x] Class diagrams
- [x] User sitemaps
- [x] Wireframes

#### SETUP
- [x] Push to git
- [x] Create directories and files
- [x] README.md

#### DB AND MODELS
- [x] Database
- [x] Models
- [x] Authors repository
- [x] Publishers repository
- [x] Books repository
- [x] Populate database

#### TEMPLATES
- [x] base.html
- [x] style base.html
- [x] Create templates

####  CONTROLLERS
- [x] Create blueprints
- [x] Import blueprint and register them in app.py
- [x] Authors controllers
- [x] Publishers controllers
- [x] Books controllers

#### TEMPLATES
- [x] Display information properly
- [x] Style
- [x] Change ALL urls to absolute paths unless properly tested

#### COMPONENT
- [x] Remove components

#### LAYOUT
- [x] /books/index.html
- [x] /books/view.html
- [x] buttons on top of every view

#### STYLING
- [x] cards.css for colours of cards depending on 
- [x] banner.css for banner that is red or something if low stock it will show stock and other info as per wireframe

### Brainstorming

- Pass title variable into every route
- Make salesperson to be empty if not needed instead of the "no salesperson
ordern from website" thing, and make the app render that into browser 
whenever salesperson == none or something. this will free space from database
and also we'll be able to change publishers_controller clunky bit
- ISBN is integer but it needs to also accept leading 0 so figure that out
- ISBN is a VARCHAR now but will it let it be the id and controllers
accept it as param for searches????

#### SQL

- ON DELETE CASCADE on FOREIGN KEYS only

#### CSS

- Make items have a colour depending on genre

### PACKAGES

- unittest
- flask

### Possible extensions

- When marking publishers as deactivated, maybe there's a html attribute
	for the form so it will appear as an option but won't be selectable?
- Make items active/inactive to show whether they are disctonued or not
- Make ISBN primary key + edition or something other than using ID?
- Make it possible to create an Author when adding a book,
	i.e: Checkbox that says: New author? or something
	Then check if the author is in database by name
	IF by name maybe a screen as in: Are you sure you want to add it?	
		we have another author with the same name and link to the person
	something like that, if it's not new then SELECT options?
- Make an option to update in the Database when to warn the user of lock stock
	by adding a form that updates info somewhere as in like:
	warning_something 	10
	so if book_stock < warning_something:
		add styling for the bordeR??? idk


