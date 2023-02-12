from app.classes.customer import Customer
from app.classes.movie import Movie
from app.classes.movie_type import MovieType
from app.classes.rental import Rental


def test_statement():
    customer = Customer("Tony")
    customer.add_rental(Rental(Movie("Avengers Endgame", MovieType.REGULAR), 2))
    customer.add_rental(Rental(Movie("Iron Man", MovieType.REGULAR), 3))
    customer.add_rental(Rental(Movie("Black Panther - Wakanda Forever", MovieType.NEW_RELEASE), 1))
    customer.add_rental(Rental(Movie("Ant Man & The Wasp - Quantumania", MovieType.NEW_RELEASE), 2))
    customer.add_rental(Rental(Movie("Cars", MovieType.CHILDRENS), 3))
    customer.add_rental(Rental(Movie("Toy Story", MovieType.CHILDRENS), 4))

    expected = "Rental Record for Tony\n"
    expected += "\tAvengers Endgame\t2.0\n"
    expected += "\tIron Man\t3.5\n"
    expected += "\tBlack Panther - Wakanda Forever\t3.0\n"
    expected += "\tAnt Man & The Wasp - Quantumania\t6.0\n"
    expected += "\tCars\t1.5\n"
    expected += "\tToy Story\t3.0\n"
    expected += "Amount owed is 19.0\n"
    expected += "You earned 7 frequent renter points"

    assert expected == customer.statement()

def test_html_statement():
    customer = Customer("Tony")
    customer.add_rental(Rental(Movie("Avengers Endgame", MovieType.REGULAR), 2))
    customer.add_rental(Rental(Movie("Iron Man", MovieType.REGULAR), 3))
    customer.add_rental(Rental(Movie("Black Panther - Wakanda Forever", MovieType.NEW_RELEASE), 1))
    customer.add_rental(Rental(Movie("Ant Man & The Wasp - Quantumania", MovieType.NEW_RELEASE), 2))
    customer.add_rental(Rental(Movie("Cars", MovieType.CHILDRENS), 3))
    customer.add_rental(Rental(Movie("Toy Story", MovieType.CHILDRENS), 4))

    expected = "<h1>Rental Record for <em>Tony</em></h1>\n"    
    expected += "<table>\n"
    expected += "<tr><th>Movie</th><th>Days</th><th>Amount</th></tr>\n"
    expected += "<tr><td>Avengers Endgame</td><td>2</td><td>2.0</td></tr>\n"
    expected += "<tr><td>Iron Man</td><td>3</td><td>3.5</td></tr>\n"
    expected += "<tr><td>Black Panther - Wakanda Forever</td><td>1</td><td>3.0</td></tr>\n"
    expected += "<tr><td>Ant Man & The Wasp - Quantumania</td><td>2</td><td>6.0</td></tr>\n"
    expected += "<tr><td>Cars</td><td>3</td><td>1.5</td></tr>\n"
    expected += "<tr><td>Toy Story</td><td>4</td><td>3.0</td></tr>\n"
    expected += "</table>\n"
    expected += "<p>Amount owed is <em>19.0</em></p>\n"
    expected += "<p>You earned <em>7</em> frequent renter points</p>"

    assert expected == customer.html_statement()

