from app.framework.movie import Movie


class Rental:
    def __init__(self, movie, days_rented):
        self.movie: Movie = movie
        self.days_rented: int = days_rented

    def get_movie(self) -> Movie:
        """Get movie"""
        return self.movie

    def get_days_rented(self) -> int:
        """Get days rented"""
        return self.days_rented

    def get_charge(self) -> float:
        """Get charge"""
        return self.movie.get_charge(self.days_rented)

    def get_frequent_renter_points(self) -> int:
        """Get frequent renter points"""
        return self.movie.get_frequent_renter_points(self.days_rented)
