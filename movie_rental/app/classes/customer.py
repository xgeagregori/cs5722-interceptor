from .rental import Rental


class Customer:
    def __init__(self, name):
        self.rentals: list[Rental] = []
        self.name: str = name

    def get_name(self) -> str:
        return self.name

    def add_rental(self, arg):
        self.rentals.append(arg)

    def statement(self) -> str:
        result = "Rental Record for " + self.get_name() + "\n"

        for each in self.rentals:
            # show figures for this rental
            result += "\t" + each.get_movie().get_title() + "\t" + \
                str(each.get_charge()) + "\n"

        # add footer lines
        result += "Amount owed is " + str(self.get_total_charge()) + "\n"
        result += "You earned " + \
            str(self.get_total_frequent_renter_points()) + \
            " frequent renter points"

        return result

    def html_statement(self) -> str:
        result = "<h1>Rental Record for <em>" + self.get_name() + "</em></h1>\n"

        result += "<table>\n"
        result += "<tr><th>Movie</th><th>Days</th><th>Amount</th></tr>\n"

        for each in self.rentals:
            # show figures for this rental
            result += "<tr><td>" + each.get_movie().get_title() + "</td><td>" + \
                str(each.get_days_rented()) + "</td><td>" + \
                str(each.get_charge()) + "</td></tr>\n"

        # add footer lines
        result += "</table>\n"
        result += "<p>Amount owed is <em>" + \
            str(self.get_total_charge()) + "</em></p>\n"
        result += "<p>You earned <em>" + \
            str(self.get_total_frequent_renter_points()) + \
            "</em> frequent renter points</p>"

        return result

    def get_total_charge(self) -> float:
        result = 0
        for each in self.rentals:
            result += each.get_charge()
        return result

    def get_total_frequent_renter_points(self) -> int:
        result = 0
        for each in self.rentals:
            result += each.get_frequent_renter_points()
        return result
