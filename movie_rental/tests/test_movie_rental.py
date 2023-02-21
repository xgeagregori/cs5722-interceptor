from app.framework.movie_rental_system import MovieRentalSystem
from app.framework.customer import Customer
from app.framework.movie import Movie
from app.framework.movie_type import MovieType
from app.framework.rental import Rental
from app.interceptors.interceptors import (
    WinterFRPInterceptor,
    LateReturnPenaltyInterceptor,
)

from app.interceptors.context import Context
from app.interceptors.dispatcher import Dispatcher
from datetime import datetime


def test_statement():
    movie_rental_system = MovieRentalSystem()

    # Load data into the system
    customer = Customer("Tony")
    movie_rental_system.add_customer(customer)

    movies = [
        Movie("Avengers Endgame", MovieType.REGULAR),
        Movie("Iron Man", MovieType.REGULAR),
        Movie("Black Panther - Wakanda Forever", MovieType.NEW_RELEASE),
        Movie("Ant Man & The Wasp - Quantumania", MovieType.NEW_RELEASE),
        Movie("Cars", MovieType.CHILDRENS),
        Movie("Toy Story", MovieType.CHILDRENS),
    ]
    for movie in movies:
        movie_rental_system.add_movie(movie)

    # Attach interceptors
    winterFRPInterceptor = WinterFRPInterceptor()
    lateReturnPenaltyInterceptor = LateReturnPenaltyInterceptor()
    movie_rental_system.get_dispatcher().attach(winterFRPInterceptor)
    movie_rental_system.get_dispatcher().attach(lateReturnPenaltyInterceptor)

    # Add rentals
    customer.add_rental(Rental(movies[0], 2))
    customer.add_rental(Rental(movies[1], 3))
    customer.add_rental(Rental(movies[2], 1))
    customer.add_rental(Rental(movies[3], 2))
    customer.add_rental(Rental(movies[4], 3))
    customer.add_rental(Rental(movies[5], 4))

    context = Context(
        date=datetime(2021, 1, 1, 0, 0, 0),
        customer=movie_rental_system.get_customer("Tony"),
    )
    movie_rental_system.get_dispatcher().update(context)

    # Assert
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

def test_statement_winter(capfd):
    movie_rental_system = MovieRentalSystem()

    # Load data into the system
    customer = Customer("Tony")
    movie_rental_system.add_customer(customer)

    movies = [
        Movie("Avengers Endgame", MovieType.REGULAR),
        Movie("Iron Man", MovieType.REGULAR),
        Movie("Black Panther - Wakanda Forever", MovieType.NEW_RELEASE),
        Movie("Ant Man & The Wasp - Quantumania", MovieType.NEW_RELEASE),
        Movie("Cars", MovieType.CHILDRENS),
        Movie("Toy Story", MovieType.CHILDRENS),
    ]
    for movie in movies:
        movie_rental_system.add_movie(movie)

    # Attach interceptors
    winterFRPInterceptor = WinterFRPInterceptor()
    lateReturnPenaltyInterceptor = LateReturnPenaltyInterceptor()
    movie_rental_system.get_dispatcher().attach(winterFRPInterceptor)
    movie_rental_system.get_dispatcher().attach(lateReturnPenaltyInterceptor)

    # Add rentals
    customer.add_rental(Rental(movies[0], 2))
    customer.add_rental(Rental(movies[1], 3))
    customer.add_rental(Rental(movies[2], 1))
    customer.add_rental(Rental(movies[3], 2))
    customer.add_rental(Rental(movies[4], 3))
    customer.add_rental(Rental(movies[5], 4))

    context = Context(
        date=datetime(2021, 12, 1, 0, 0, 0),
        customer=movie_rental_system.get_customer("Tony"),
    )
    movie_rental_system.get_dispatcher().update(context)

    # Check the print statement
    captured = capfd.readouterr()
    assert (
        captured.out
        == "[Bonus]: +2 winter frequent renter points\n"
    )

    # Assert
    expected = "Rental Record for Tony\n"
    expected += "\tAvengers Endgame\t2.0\n"
    expected += "\tIron Man\t3.5\n"
    expected += "\tBlack Panther - Wakanda Forever\t3.0\n"
    expected += "\tAnt Man & The Wasp - Quantumania\t6.0\n"
    expected += "\tCars\t1.5\n"
    expected += "\tToy Story\t3.0\n"
    expected += "Amount owed is 19.0\n"
    expected += "You earned 9 frequent renter points"

    assert expected == customer.statement()

def test_statement_late_return(capfd):
    movie_rental_system = MovieRentalSystem()

    # Load data into the system
    customer = Customer("Tony")
    movie_rental_system.add_customer(customer)

    movies = [
        Movie("Avengers Endgame", MovieType.REGULAR),
        Movie("Iron Man", MovieType.REGULAR),
        Movie("Black Panther - Wakanda Forever", MovieType.NEW_RELEASE),
        Movie("Ant Man & The Wasp - Quantumania", MovieType.NEW_RELEASE),
        Movie("Cars", MovieType.CHILDRENS),
        Movie("Toy Story", MovieType.CHILDRENS),
    ]
    for movie in movies:
        movie_rental_system.add_movie(movie)

    # Attach interceptors
    winterFRPInterceptor = WinterFRPInterceptor()
    lateReturnPenaltyInterceptor = LateReturnPenaltyInterceptor()
    movie_rental_system.get_dispatcher().attach(winterFRPInterceptor)
    movie_rental_system.get_dispatcher().attach(lateReturnPenaltyInterceptor)

    # Add rentals
    customer.add_rental(Rental(movies[0], 2))
    customer.add_rental(Rental(movies[1], 3))
    customer.add_rental(Rental(movies[2], 1))
    customer.add_rental(Rental(movies[3], 2))
    customer.add_rental(Rental(movies[4], 3))
    customer.add_rental(Rental(movies[5], 10))

    context = Context(
        date=datetime(2021, 1, 1, 0, 0, 0),
        customer=movie_rental_system.get_customer("Tony"),
    )
    movie_rental_system.get_dispatcher().update(context)

    # Check the print statement
    captured = capfd.readouterr()
    assert (
        captured.out
        == "[Warning]: Late return penalty +2.0\n"
    )

    # Assert
    expected = "Rental Record for Tony\n"
    expected += "\tAvengers Endgame\t2.0\n"
    expected += "\tIron Man\t3.5\n"
    expected += "\tBlack Panther - Wakanda Forever\t3.0\n"
    expected += "\tAnt Man & The Wasp - Quantumania\t6.0\n"
    expected += "\tCars\t1.5\n"
    expected += "\tToy Story\t12.0\n"
    expected += "Amount owed is 30.0\n"
    expected += "You earned 7 frequent renter points"

    assert expected == customer.statement()


def test_html_statement():
    movie_rental_system = MovieRentalSystem()

    # Load data into the system
    customer = Customer("Tony")
    movie_rental_system.add_customer(customer)

    movies = [
        Movie("Avengers Endgame", MovieType.REGULAR),
        Movie("Iron Man", MovieType.REGULAR),
        Movie("Black Panther - Wakanda Forever", MovieType.NEW_RELEASE),
        Movie("Ant Man & The Wasp - Quantumania", MovieType.NEW_RELEASE),
        Movie("Cars", MovieType.CHILDRENS),
        Movie("Toy Story", MovieType.CHILDRENS),
    ]
    for movie in movies:
        movie_rental_system.add_movie(movie)

    # Attach interceptors
    winterFRPInterceptor = WinterFRPInterceptor()
    lateReturnPenaltyInterceptor = LateReturnPenaltyInterceptor()
    movie_rental_system.get_dispatcher().attach(winterFRPInterceptor)
    movie_rental_system.get_dispatcher().attach(lateReturnPenaltyInterceptor)

    # Add rentals
    customer.add_rental(Rental(movies[0], 2))
    customer.add_rental(Rental(movies[1], 3))
    customer.add_rental(Rental(movies[2], 1))
    customer.add_rental(Rental(movies[3], 2))
    customer.add_rental(Rental(movies[4], 3))
    customer.add_rental(Rental(movies[5], 4))

    context = Context(
        date=datetime(2021, 1, 1, 0, 0, 0),
        customer=movie_rental_system.get_customer("Tony"),
    )
    movie_rental_system.get_dispatcher().update(context)

    # Assert
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

def test_html_statement_winter(capfd):
    movie_rental_system = MovieRentalSystem()

    # Load data into the system
    customer = Customer("Tony")
    movie_rental_system.add_customer(customer)

    movies = [
        Movie("Avengers Endgame", MovieType.REGULAR),
        Movie("Iron Man", MovieType.REGULAR),
        Movie("Black Panther - Wakanda Forever", MovieType.NEW_RELEASE),
        Movie("Ant Man & The Wasp - Quantumania", MovieType.NEW_RELEASE),
        Movie("Cars", MovieType.CHILDRENS),
        Movie("Toy Story", MovieType.CHILDRENS),
    ]
    for movie in movies:
        movie_rental_system.add_movie(movie)

    # Attach interceptors
    winterFRPInterceptor = WinterFRPInterceptor()
    lateReturnPenaltyInterceptor = LateReturnPenaltyInterceptor()
    movie_rental_system.get_dispatcher().attach(winterFRPInterceptor)
    movie_rental_system.get_dispatcher().attach(lateReturnPenaltyInterceptor)

    # Add rentals
    customer.add_rental(Rental(movies[0], 2))
    customer.add_rental(Rental(movies[1], 3))
    customer.add_rental(Rental(movies[2], 1))
    customer.add_rental(Rental(movies[3], 2))
    customer.add_rental(Rental(movies[4], 3))
    customer.add_rental(Rental(movies[5], 4))

    context = Context(
        date=datetime(2021, 12, 1, 0, 0, 0),
        customer=movie_rental_system.get_customer("Tony"),
    )
    movie_rental_system.get_dispatcher().update(context)

    # Check the print statement
    captured = capfd.readouterr()
    assert (
        captured.out
        == "[Bonus]: +2 winter frequent renter points\n"
    )


    # Assert
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
    expected += "<p>You earned <em>9</em> frequent renter points</p>"

    assert expected == customer.html_statement()

def test_html_statement_late_return(capfd):
    movie_rental_system = MovieRentalSystem()

    # Load data into the system
    customer = Customer("Tony")
    movie_rental_system.add_customer(customer)

    movies = [
        Movie("Avengers Endgame", MovieType.REGULAR),
        Movie("Iron Man", MovieType.REGULAR),
        Movie("Black Panther - Wakanda Forever", MovieType.NEW_RELEASE),
        Movie("Ant Man & The Wasp - Quantumania", MovieType.NEW_RELEASE),
        Movie("Cars", MovieType.CHILDRENS),
        Movie("Toy Story", MovieType.CHILDRENS),
    ]
    for movie in movies:
        movie_rental_system.add_movie(movie)

    # Attach interceptors
    winterFRPInterceptor = WinterFRPInterceptor()
    lateReturnPenaltyInterceptor = LateReturnPenaltyInterceptor()
    movie_rental_system.get_dispatcher().attach(winterFRPInterceptor)
    movie_rental_system.get_dispatcher().attach(lateReturnPenaltyInterceptor)

    # Add rentals
    customer.add_rental(Rental(movies[0], 2))
    customer.add_rental(Rental(movies[1], 3))
    customer.add_rental(Rental(movies[2], 1))
    customer.add_rental(Rental(movies[3], 2))
    customer.add_rental(Rental(movies[4], 3))
    customer.add_rental(Rental(movies[5], 10))

    context = Context(
        date=datetime(2021, 1, 1, 0, 0, 0),
        customer=movie_rental_system.get_customer("Tony"),
    )
    movie_rental_system.get_dispatcher().update(context)

    # Check the print statement
    captured = capfd.readouterr()
    assert (
        captured.out
        == "[Warning]: Late return penalty +2.0\n"
    )


    # Assert
    expected = "<h1>Rental Record for <em>Tony</em></h1>\n"
    expected += "<table>\n"
    expected += "<tr><th>Movie</th><th>Days</th><th>Amount</th></tr>\n"
    expected += "<tr><td>Avengers Endgame</td><td>2</td><td>2.0</td></tr>\n"
    expected += "<tr><td>Iron Man</td><td>3</td><td>3.5</td></tr>\n"
    expected += "<tr><td>Black Panther - Wakanda Forever</td><td>1</td><td>3.0</td></tr>\n"
    expected += "<tr><td>Ant Man & The Wasp - Quantumania</td><td>2</td><td>6.0</td></tr>\n"
    expected += "<tr><td>Cars</td><td>3</td><td>1.5</td></tr>\n"
    expected += "<tr><td>Toy Story</td><td>10</td><td>12.0</td></tr>\n"
    expected += "</table>\n"
    expected += "<p>Amount owed is <em>30.0</em></p>\n"
    expected += "<p>You earned <em>7</em> frequent renter points</p>"

    assert expected == customer.html_statement()