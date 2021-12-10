from models.author import Author
from models.book import Book
from models.publisher import Publisher
from repositories import author_repository
from repositories import book_repository
from repositories import publisher_repository

author_repository.delete_all()
publisher_repository.delete_all()
# book_repository.delete_all()

# Authors
burns = Author(name="Charles Burns")
clowes = Author(name="Daniel Clowes")
walden = Author(name="Tillie Walden")
kabi = Author(name="Nagata Kabi")
hanselmann = Author(name="Simon Hanselmann")
moore = Author(name="Alan Moore")
gibbons = Author(name="Dave Gibbons")
otomo = Author(name="Katsuhiro Otomo")

authors = [burns, clowes, walden, kabi, hanselmann, moore, gibbons, otomo]

for author in authors:
    author_repository.save(author)

# Publishers
dc = Publisher(
    name="DC Comics",
    website="www.dc.com",
    salesperson="John Doe",
    contact="john@dc.com"
)
fgraphics = Publisher(
    name="Fantagraphics Books",
    website="www.fgraphics.com"
)
black_horse = Publisher(
    name="Black Horse",
    website="www.blackhorse.com",
    salesperson="Bojack Horseman",
    contact="323-902-1992"
)

publishers = [dc, fgraphics, black_horse]

for publisher in publishers:
    publisher_repository.save(publisher)


for row in author_repository.select_all():
    print(row.__dict__)

for row in publisher_repository.select_all():
    print(row.__dict__)
