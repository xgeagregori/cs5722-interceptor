from app.framework.customer import Customer
from app.framework.movie import Movie
from ..interceptors.dispatcher import Dispatcher


class MovieRentalSystem:
    def __init__(self):
        self.customers: list[Customer] = []
        self.movies: list[Movie] = []
        self.dispatcher = Dispatcher()

    def add_customer(self, customer: Customer):
        """Add a customer to the system"""
        self.customers.append(customer)

    def add_movie(self, movie: Movie):
        """Add a movie to the system"""
        self.movies.append(movie)

    def get_customer(self, name: str) -> Customer:
        """Get customer by name"""
        for customer in self.customers:
            if customer.get_name() == name:
                return customer
        return None

    def get_movie(self, title: str) -> Movie:
        """Get movie by title"""
        for movie in self.movies:
            if movie.get_title() == title:
                return movie
        return None

    def remove_customer(self, customer: Customer):
        """Remove customer from system"""
        self.customers.remove(customer)

    def remove_movie(self, movie: Movie):
        """Remove movie from system"""
        self.movies.remove(movie)

    def get_dispatcher(self) -> Dispatcher:
        """Get dispatcher"""
        return self.dispatcher
