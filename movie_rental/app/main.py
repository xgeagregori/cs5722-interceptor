from app.customer import Customer
from app.movie import Movie
from app.rental import Rental

if __name__ == "__main__":
    customer = Customer("Tony")
    customer.add_rental(Rental(Movie("Avengers Endgame", Movie.REGULAR), 2))
    customer.add_rental(Rental(Movie("Iron Man", Movie.REGULAR), 3))
    customer.add_rental(Rental(Movie("Black Panther - Wakanda Forever", Movie.NEW_RELEASE), 1))
    customer.add_rental(Rental(Movie("Ant Man & The Wasp - Quantumania", Movie.NEW_RELEASE), 2))
    customer.add_rental(Rental(Movie("Cars", Movie.CHILDRENS), 3))
    customer.add_rental(Rental(Movie("Toy Story", Movie.CHILDRENS), 4))
    print(customer.statement())