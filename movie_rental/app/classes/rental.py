from .movie import Movie

class Rental:
    def __init__(self, movie, days_rented):
        self.days_rented: int = days_rented
        self.movie: Movie = movie

    def get_days_rented(self) -> int:
        return self.days_rented

    def get_movie(self) -> Movie:
        return self.movie

    def get_charge(self) -> float:
        return self.movie.get_charge(self.days_rented)

    def get_frequent_renter_points(self) -> int:
        return self.movie.get_frequent_renter_points(self.days_rented)