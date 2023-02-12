from app.movie import Movie
from app.rental import Rental


class Customer:
    def __init__(self, name):
        self.rentals = []
        self.name = name

    def get_name(self):
        return self.name

    def add_rental(self, arg):
        self.rentals.append(arg)

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"

        for each in self.rentals:
            this_amount = 0.0

            if each.get_movie().get_price_code() == Movie.REGULAR:
                this_amount += 2
                if each.get_days_rented() > 2:
                    this_amount += (each.get_days_rented() - 2) * 1.5
            elif each.get_movie().get_price_code() == Movie.NEW_RELEASE:
                this_amount += each.get_days_rented() * 3
            elif each.get_movie().get_price_code() == Movie.CHILDRENS:
                this_amount += 1.5
                if each.get_days_rented() > 3:
                    this_amount += (each.get_days_rented() - 3) * 1.5

            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if (each.get_movie().get_price_code() == Movie.NEW_RELEASE) and each.get_days_rented() > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += "\t" + each.get_movie().get_title() + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        # add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + \
            str(frequent_renter_points) + " frequent renter points"

        return result
