class Rental:
    def __init__(self, movie, daysRented):
        self.days_rented = daysRented
        self.movie = movie

    def get_days_rented(self):
        return self.days_rented

    def get_movie(self):
        return self.movie
