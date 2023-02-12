from app.customer import Customer
from app.movie import Movie
from app.rental import Rental


def tests():
    customer = Customer("Tony")
    customer.add_rental(Rental(Movie("Avengers Endgame", Movie.REGULAR), 2))
    customer.add_rental(Rental(Movie("Iron Man", Movie.REGULAR), 3))
    customer.add_rental(Rental(Movie("Black Panther - Wakanda Forever", Movie.NEW_RELEASE), 1))
    customer.add_rental(Rental(Movie("Ant Man & The Wasp - Quantumania", Movie.NEW_RELEASE), 2))
    customer.add_rental(Rental(Movie("Cars", Movie.CHILDRENS), 3))
    customer.add_rental(Rental(Movie("Toy Story", Movie.CHILDRENS), 4))

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
