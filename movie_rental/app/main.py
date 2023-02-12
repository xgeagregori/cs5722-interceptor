from classes.customer import Customer
from classes.movie import Movie
from classes.movie_type import MovieType
from classes.rental import Rental

if __name__ == "__main__":
    customer = Customer("Tony")
    customer.add_rental(Rental(Movie("Avengers Endgame", MovieType.REGULAR), 2))
    customer.add_rental(Rental(Movie("Iron Man", MovieType.REGULAR), 3))
    customer.add_rental(Rental(Movie("Black Panther - Wakanda Forever", MovieType.NEW_RELEASE), 1))
    customer.add_rental(Rental(Movie("Ant Man & The Wasp - Quantumania", MovieType.NEW_RELEASE), 2))
    customer.add_rental(Rental(Movie("Cars", MovieType.CHILDRENS), 3))
    customer.add_rental(Rental(Movie("Toy Story", MovieType.CHILDRENS), 4))
    print(customer.statement())
    print(customer.html_statement())