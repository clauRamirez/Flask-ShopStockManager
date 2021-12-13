from models.author import Author
from models.book import Book
from models.publisher import Publisher
from repositories import author_repository
from repositories import book_repository
from repositories import publisher_repository

book_repository.delete_all()
author_repository.delete_all()
publisher_repository.delete_all()

# Authors
burns = Author(name="Charles Burns")
clowes = Author(name="Daniel Clowes")
walden = Author(name="Tillie Walden")
kabi = Author(name="Nagata Kabi")
hanselmann = Author(name="Simon Hanselmann")
moore = Author(name="Alan Moore")
gibbons = Author(name="Dave Gibbons")
otomo = Author(name="Katsuhiro Otomo")
spiegelman = Author(name="Art Spiegelman")
satrapi = Author(name="Marjane Satrapi")

authors = [burns, clowes, walden, kabi, hanselmann, moore, gibbons, otomo, spiegelman, satrapi]

for author in authors:
    author_repository.save(author)

# Publishers
dc = Publisher(
    name="DC Comics",
    website="www.dc.com",
    salesperson="Jane Doe",
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
penguin = Publisher(
    name="Penguin Books",
    website="www.penguin.co.uk",
    salesperson="Walter McBeird",
    contact="mcbeird@penguin.co.uk"
)
publishers = [dc, fgraphics, black_horse, penguin]

for publisher in publishers:
    publisher_repository.save(publisher)

# Books
books = [
    Book(
        isbn="9780224090414",
        title="Xed Out",
        genre="Fantasy",
        author=burns,
        illustrator=burns,
        publisher=penguin,
        edition=1,
        cost=6.12,
        price=12.49,
        stock=12
    ),
    Book(
        isbn="9780224096720",
        title="Last Look",
        genre="Fantasy",
        author=burns,
        illustrator=burns,
        publisher=penguin,
        edition=1,
        cost=6.42,
        price=12.49,
        stock=7
    ),
    Book(
        isbn="9780224096744",
        title="Sugar Skull",
        genre="Fantasy",
        author=burns,
        illustrator=burns,
        publisher=penguin,
        edition=1,
        cost=6.72,
        price=12.99,
        stock=9
    ),
    Book(
        isbn="9780224077781",
        title="Black Hole",
        genre="Drama",
        author=burns,
        illustrator=burns,
        publisher=penguin,
        edition=3,
        cost=9.21,
        price=24.99,
        stock=12
    ),
    Book(
        isbn="1910395374",
        title="On a Sunbeam",
        genre="Drama",
        author=walden,
        illustrator=walden,
        publisher=fgraphics,
        edition=1,
        cost=7.21,
        price=19.99,
        stock=4
    ),
    Book(
        isbn="1250207568",
        title="Are You Listening?",
        genre="Romance",
        author=walden,
        illustrator=walden,
        publisher=black_horse,
        edition=1,
        cost=9.21,
        price=19.99,
        stock=9
    ),
    Book(
        isbn="9780141014081",
        title="Maus",
        genre="True Story",
        author=spiegelman,
        illustrator=spiegelman,
        publisher=penguin,
        edition=8,
        cost=7.84,
        price=24.49,
        stock=17
    ),
    Book(
        isbn="9780375714573",
        title="Persepolis",
        genre="True Story",
        author=satrapi,
        illustrator=satrapi,
        publisher=penguin,
        edition=4,
        cost=11.21,
        price=24.99,
        stock=11
    ),
    Book(
        isbn="1401248195",
        title="Watchmen",
        genre="Thriller",
        author=moore,
        illustrator=gibbons,
        publisher=dc,
        edition=9,
        cost=12.21,
        price=22.49,
        stock=7
    ),
    Book(
        isbn="8601400793114",
        title="Akira, vol. 1",
        genre="Manga",
        author=otomo,
        illustrator=otomo,
        publisher=black_horse,
        edition=7,
        cost=11.21,
        price=24.99,
        stock=4
    ),
    Book(
        isbn="871357828",
        title="Akira, vol. 2",
        genre="Manga",
        author=otomo,
        illustrator=otomo,
        publisher=black_horse,
        edition=7,
        cost=11.21,
        price=24.99,
        stock=0
    ),
    Book(
        isbn="784061037137",
        title="Akira, vol. 3",
        genre="Manga",
        author=otomo,
        illustrator=otomo,
        publisher=black_horse,
        edition=7,
        cost=11.21,
        price=24.99,
        stock=2
    ),
    Book(
        isbn="9781935429067",
        title="Akira, vol. 4",
        genre="Manga",
        author=otomo,
        illustrator=otomo,
        publisher=black_horse,
        edition=7,
        cost=11.21,
        price=24.99,
        stock=0
    ),
        Book(
        isbn="1935429078",
        title="Akira, vol. 5",
        genre="Manga",
        author=otomo,
        illustrator=otomo,
        publisher=black_horse,
        edition=7,
        cost=11.21,
        price=24.99,
        stock=0
    ),
    Book(
        isbn="1935429086",
        title="Akira, vol. 6",
        genre="Manga",
        author=otomo,
        illustrator=otomo,
        publisher=black_horse,
        edition=7,
        cost=11.21,
        price=24.99,
        stock=2
    ),
    Book(
        isbn="9781560974277",
        title="Ghost World",
        genre="Manga",
        author=clowes,
        illustrator=clowes,
        publisher=fgraphics,
        edition=3,
        cost=7.21,
        price=14.99,
        stock=5
    ),
    Book(
        isbn="1626926034",
        title="My Lesbian Experience with Loneliness",
        genre="Manga",
        author=kabi,
        illustrator=kabi,
        publisher=black_horse,
        edition=1,
        cost=4.21,
        price=9.99,
        stock=12
    ),
    Book(
        isbn="1683963091",
        title="Seeds and Stems",
        genre="Drama",
        author=hanselmann,
        illustrator=hanselmann,
        publisher=fgraphics,
        edition=1,
        cost=12.21,
        price=19.99,
        stock=6
    )
]


for book in books:
    book_repository.save(book)

for row in author_repository.select_all():
    print(row.__dict__)

for row in publisher_repository.select_all():
    print(row.__dict__)

for row in book_repository.select_all():
    print(row.__dict__)
